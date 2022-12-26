from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'sam'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.CharField(initial='survey')
    valence = models.StringField(label="Please, make your selection below:",
                                choices=["1", "2", "3", "4", "5"," 6", "7", "8","9"] ,widget=widgets.RadioSelectHorizontal)
    arousal = models.StringField(label="Please, make your selection below:",
                                choices=["1", "2", "3", "4", "5"," 6", "7","8","9"] ,widget=widgets.RadioSelectHorizontal)
    dominance = models.StringField(label="Please, make your selection below:",
                                choices=["1", "2", "3", "4", "5"," 6", "7","8","9"] ,widget=widgets.RadioSelectHorizontal)
# FUNCTIONS
# PAGES
class Instructions(Page):
    form_model = 'player'
    form_fields = []

class Scale1(Page):
    form_model = 'player'
    form_fields = ['valence']

class Scale2(Page):
    form_model = 'player'
    form_fields = ['arousal']

class Scale3(Page):
    form_model = 'player'
    form_fields = ['dominance']


page_sequence = [Instructions, Scale1, Scale2,Scale3]
