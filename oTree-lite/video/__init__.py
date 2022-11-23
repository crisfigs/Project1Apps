from otree.api import *
from otree.models import session


class C(BaseConstants):
    NAME_IN_URL = 'video'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    def creating_session(subsession):
        session = subsession.session
        #for player in subsession.get_players():
         #   participant = player.participant
          #  participant.treatment = session.config['treatment']
        for player in subsession.get_players():
            participant = player.participant
            import random
            participant.treatment = random.choices(["videoA", "videoS"], weights=(50,50), k=1)[0]


    #def creating_session(subsession):
    ##   for player in subsession.get_players():
    #      import random
    #       player.treatment = random.choices(["videoA", "videoS"], weights=(50,50), k=1)[0] #10,90
    #       player.participant.vars["treatment"] = player.treatment

    #def vars_for_all_templates(player):
    #   return {
#       'treatment': player.participant.vars["treatment"]}

class Player(BasePlayer):
    prolific_id = models.StringField()
    treatment = models.CharField(initial='videoA')
    #treatment = models.StringField()


class Welcome(Page):
    form_model = 'player'

class GeneralInstructions(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

class Desc(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class Video(Page):
    def is_displayed(player):
        return player.treatment == 'videoA'

class Video2(Page):
    def is_displayed(player):
        return player.treatment == 'videoS'

class VA(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class Info_q(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class Task(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class InstructionsTask1(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']



page_sequence = [Welcome, GeneralInstructions, Desc, Video,Video2,  Info_q, VA, InstructionsTask1, Task]