from otree.api import *



class C(BaseConstants):
    NAME_IN_URL = 'video'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    prolific_id = models.StringField()


class Subsession(BaseSubsession):
    def creating_session(subsession):
        import itertools
        treatment1 = itertools.cycle([True, False])
        for player in subsession.get_players():
            player.treatment1 = next(treatment1)

#treatment1 is the red cross video
class Welcome(Page):
    form_model = 'player'

class GeneralInstructions(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

class Desc(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class Video(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class VA(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class Info_q(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class Task(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']



page_sequence = [Welcome, GeneralInstructions, Desc, Video,  Info_q,VA, Task]