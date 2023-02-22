from otree import settings
from otree.api import *
import time
from .image_utils import encode_image
import random

doc = """
The sortable ranking based on: "Widget to rank/reorder items". See http://sortablejs.github.io/Sortable/
for more examples.
"""


class C(BaseConstants):
    NAME_IN_URL = 'rank_widget'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES = ['Choose A and  I watch the video after.', 'Choose B and  I watch the video after. ', 'Watch the video and decide between A and B after.' ]
    captcha_length = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    finalRanking = models.StringField()
    iteration = models.IntegerField(initial=0)
    num_trials = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)
    num_failed = models.IntegerField(initial=0)
    #Comprehension questions
    q1A = models.IntegerField(label="1. Option A pays: ", choices = [[0,'(me: 0, charity: 5)'],[1,'(me: 5, charity: 0)'],[2,'(me: 1, charity: 4)'],[3,'(me: 1, charity: 8)'],[4,'(me: 4, charity: 0)']])
    q1B = models.IntegerField(label="2. Option B pays: ", choices = [[0,'(me: 1, charity: 8)'],[1,'(me: 1, charity: 8)'],[2,'(me: 0, charity: 5)'],[3,'(me: 4, charity: 0)'],[4,'(me: 1, charity: 4)']])
    q_change = models.IntegerField(label="3. After watching the I can still change my choice in:",
                                   choices=[[0, 'Case 1'], [1, 'Case 2'], [2, 'Case 3']])
    q_imp = models.IntegerField(label="4. Select the correct answer. My choice is implemented:",
                                   choices=[[0, 'Always'], [2, 'with a 40% chance and the computer chooses option three with 60%'],  [1, 'with a 60% chance and the computer chooses option three with 40%'],[3, 'Never']])

    q_video = models.IntegerField(label="5. Comprehension question on the video. ", choices=[[0, 'X'], [1, 'Y'], [2, 'Z']])
    ranking2 = models.StringField()
    ranking2_1 = models.StringField()
    ranking2_2 = models.StringField()
    ranking2_3 = models.StringField()
    q_ranking2 = models.StringField(blank=True)
    task2 = models.IntegerField(label="Would you be willing to accept an extra 0.10 pence for substituting your top 1st  choice with your top 2nd?",
                                   choices=[[0, 'No'], [1, 'Yes']])
    task1 = models.StringField(blank=True)
    q_beliefs = models.StringField(blank=True)
    favopt = models.StringField()
    impopt = models.StringField()

    def set_error_message(player, value):
        correct_answers = {
                        'q1A': 1,
                        'q1B': 1,
                        'q_change': 2,
                        'q_imp': 1,
                        'q_video': 0}
        list_answers = list(value.items())[0:]
        list_correct_answers = list(correct_answers.items())
        if list_answers != list_correct_answers:
            Text = 'You did not answer all questions correctly. Please read the instructions again and correct your answers.'
            return Text



def get_task_module(player):
    """
    This function is only needed for demo mode, to demonstrate all the different versions.
    You can simplify it if you want.
    """
    from . import task_matrix

    session = player.session
    task = session.config.get("task")
    if task == "matrix":
        return task_matrix
    if task == "transcription":
        return task_transcription
    if task == "decoding":
        return task_decoding
    # default
    return task_matrix











# puzzle-specific stuff


class Puzzle(ExtraModel):
    """A model to keep record of all generated puzzles"""

    player = models.Link(Player)
    iteration = models.IntegerField(initial=0)
    attempts = models.IntegerField(initial=0)
    timestamp = models.FloatField(initial=0)
    # can be either simple text, or a json-encoded definition of the puzzle, etc.
    text = models.LongStringField()
    # solution may be the same as text, if it's simply a transcription task
    solution = models.LongStringField()
    response = models.LongStringField()
    response_timestamp = models.FloatField()
    is_correct = models.BooleanField()


def generate_puzzle(player: Player) -> Puzzle:
    """Create new puzzle for a player"""
    task_module = get_task_module(player)
    fields = task_module.generate_puzzle_fields()
    player.iteration += 1
    return Puzzle.create(
        player=player, iteration=player.iteration, timestamp=time.time(), **fields
    )


def get_current_puzzle(player):
    puzzles = Puzzle.filter(player=player, iteration=player.iteration)
    if puzzles:
        [puzzle] = puzzles
        return puzzle


def encode_puzzle(puzzle: Puzzle):
    """Create data describing puzzle to send to client"""
    task_module = get_task_module(puzzle.player)  # noqa
    # generate image for the puzzle
    image = task_module.render_image(puzzle)
    data = encode_image(image)
    return dict(image=data)


def get_progress(player: Player):
    """Return current player progress"""
    return dict(
        num_trials=player.num_trials,
        num_correct=player.num_correct,
        num_incorrect=player.num_failed,
        iteration=player.iteration,
    )


def play_game(player: Player, message: dict):
    """Main game workflow
    Implemented as reactive scheme: receive message from vrowser, react, respond.

    Generic game workflow, from server point of view:
    - receive: {'type': 'load'} -- empty message means page loaded
    - check if it's game start or page refresh midgame
    - respond: {'type': 'status', 'progress': ...}
    - respond: {'type': 'status', 'progress': ..., 'puzzle': data} -- in case of midgame page reload

    - receive: {'type': 'next'} -- request for a next/first puzzle
    - generate new puzzle
    - respond: {'type': 'puzzle', 'puzzle': data}

    - receive: {'type': 'answer', 'answer': ...} -- user answered the puzzle
    - check if the answer is correct
    - respond: {'type': 'feedback', 'is_correct': true|false, 'retries_left': ...} -- feedback to the answer

    If allowed by config `attempts_pre_puzzle`, client can send more 'answer' messages
    When done solving, client should explicitely request next puzzle by sending 'next' message

    Field 'progress' is added to all server responses to indicate it on page.

    To indicate max_iteration exhausted in response to 'next' server returns 'status' message with iterations_left=0
    """
    session = player.session
    my_id = player.id_in_group
    params = session.params
    task_module = get_task_module(player)

    now = time.time()
    # the current puzzle or none
    current = get_current_puzzle(player)

    message_type = message['type']

    # page loaded
    if message_type == 'load':
        p = get_progress(player)
        if current:
            return {
                my_id: dict(type='status', progress=p, puzzle=encode_puzzle(current))
            }
        else:
            return {my_id: dict(type='status', progress=p)}

    if message_type == "cheat" and settings.DEBUG:
        return {my_id: dict(type='solution', solution=current.solution)}

    # client requested new puzzle
    if message_type == "next":
        if current is not None:
            if current.response is None:
                raise RuntimeError("trying to skip over unsolved puzzle")
            if now < current.timestamp + params["puzzle_delay"]:
                raise RuntimeError("retrying too fast")
            if current.iteration == params['max_iterations']:
                return {
                    my_id: dict(
                        type='status', progress=get_progress(player), iterations_left=0
                    )
                }
        # generate new puzzle
        z = generate_puzzle(player)
        p = get_progress(player)
        return {my_id: dict(type='puzzle', puzzle=encode_puzzle(z), progress=p)}

    # client gives an answer to current puzzle
    if message_type == "answer":
        if current is None:
            raise RuntimeError("trying to answer no puzzle")

        if current.response is not None:  # it's a retry
            if current.attempts >= params["attempts_per_puzzle"]:
                raise RuntimeError("no more attempts allowed")
            if now < current.response_timestamp + params["retry_delay"]:
                raise RuntimeError("retrying too fast")

            # undo last updation of player progress
            player.num_trials -= 1
            if current.is_correct:
                player.num_correct -= 1
            else:
                player.num_failed -= 1

        # check answer
        answer = message["answer"]

        if answer == "" or answer is None:
            raise ValueError("bogus answer")

        current.response = answer
        current.is_correct = task_module.is_correct(answer, current)
        current.response_timestamp = now
        current.attempts += 1

        # update player progress
        if current.is_correct:
            player.num_correct += 1
        else:
            player.num_failed += 1
        player.num_trials += 1

        retries_left = params["attempts_per_puzzle"] - current.attempts
        p = get_progress(player)
        return {
            my_id: dict(
                type='feedback',
                is_correct=current.is_correct,
                retries_left=retries_left,
                progress=p,
            )
        }

    raise RuntimeError("unrecognized message from client")


def creating_session(subsession: Subsession):
    session = subsession.session
    defaults = dict(
        retry_delay=1.0, puzzle_delay=1.0, attempts_per_puzzle=1, max_iterations=None
    )
    session.params = {}
    for param in defaults:
        session.params[param] = session.config.get(param, defaults[param])



###PAGES
class InstructionsGame(Page):
    pass

class Game(Page):
    timeout_seconds = 90
    live_method = play_game

    @staticmethod
    def js_vars(player: Player):
        return dict(params=player.session.params)

    @staticmethod
    def vars_for_template(player: Player):
        task_module = get_task_module(player)
        return dict(DEBUG=settings.DEBUG,
                    input_type=task_module.INPUT_TYPE,
                    placeholder=task_module.INPUT_HINT)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if not timeout_happened and not player.session.params['max_iterations']:
            raise RuntimeError("malicious page submission")


class Part2_Instruction_Page(Page):
  form_model = 'player'
  form_fields = ['q1A', 'q1B', 'q_change', 'q_imp', 'q_video']

  def error_message(player,value):
      return player.set_error_message(value)



class ResultsGame(Page):
    pass


class Ranking1(Page):
    form_model = 'player'
    form_fields = ['finalRanking']

    @staticmethod
    def vars_for_template(player: Player):
        menu = [
                { "text": C.CHOICES[0], "id": "Choose A and  I watch the video after." },
                {"text": C.CHOICES[1], "id": "Choose B and  I watch the video after."},
                {"text": C.CHOICES[2], "id": "Watch the video and decide between A and B after."}
            ]
        random.shuffle(menu)
       # print(menu)
        return dict(
            CHOICES = menu,

        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        a = list(player.finalRanking.split(","))
        player.ranking2_1 = a[0]
        player.ranking2_2 = a[1]
        player.ranking2_3 = a[2]

class Ranking2(Page):
    form_model = 'player'
    form_fields = ['q_ranking2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
                     ranking2_1= player.ranking2_1,
                     ranking2_2= player.ranking2_2,
                     ranking2_3=player.ranking2_3)


class Ranking2_switch(Page):
    form_model = 'player'
    form_fields = []

    @staticmethod
    def is_displayed(player: Player):
        return player.q_ranking2 == "Yes"

    def vars_for_template(player: Player):
        return dict(ranking_expost = f"{player.ranking2_2},{player.ranking2_1},{player.ranking2_3}",
                     ranking2_1 = player.ranking2_2,
                     ranking2_2 = player.ranking2_1,
                     ranking2_3 = player.ranking2_3)

    def before_next_page(player, timeout_happened):
        player.favopt = player.ranking2_2
        player.impopt = random.choices([player.favopt,C.CHOICES[2]], weights=(1,0), k=1)[0]

class Ranking2_noswitch(Page):
    form_model = 'player'
    form_fields = ['q_ranking2']

    @staticmethod
    def is_displayed(player: Player):
        return player.q_ranking2 == "No"

    def vars_for_template(player: Player):
        return dict(
                     ranking2_1 = player.ranking2_1,
                     ranking2_2 = player.ranking2_2,
                     ranking2_3 = player.ranking2_3,
                     ranking_expost= f"{player.ranking2_1},{player.ranking2_2},{player.ranking2_3}",)

    def before_next_page(player, timeout_happened):
        player.favopt = player.ranking2_1
        player.impopt = random.choices([player.favopt,C.CHOICES[2]], weights=(0,1), k=1)[0]


class Part3_Intro(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod
    def vars_for_template(player: Player):
        return dict( favopt = player.favopt,
                     impopt = player.impopt)


class Hypo_choice(Page):
    form_model = 'player'
    form_fields = ['task1']

page_sequence = [ Ranking1, Ranking2, Ranking2_noswitch, Ranking2_switch, Part3_Intro]
#InstructionsGame, Game, ResultsGame, Part2_Instruction_Page,