from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'emp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.CharField(initial='survey')
    empathyq = models.StringField(label="I feel empathic.",
        choices=["0","1", "2", "3", "4", "5"," 6", "7", "8","9","10"] ,widget=widgets.RadioSelectHorizontal)
    sympathyq = models.StringField(
        label="I feel sympathetic.",
        choices=["0","1", "2", "3", "4", "5"," 6", "7", "8","9","10"] ,widget=widgets.RadioSelectHorizontal)
    compassionq = models.StringField(
        label="I feel compassionate.",
        choices=["0","1", "2", "3", "4", "5"," 6", "7", "8","9","10"], widget=widgets.RadioSelectHorizontal)


# FUNCTIONS
# PAGES
class instructions(Page):
    form_model = 'player'
    form_fields = []

class empathy(Page):
    form_model = 'player'
    form_fields = ['empathyq']

class sympathy(Page):
    form_model = 'player'
    form_fields = ['sympathyq']

class compassion(Page):
    form_model = 'player'
    form_fields = ['compassionq']




page_sequence = [instructions, empathy, sympathy,compassion]
