from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.CharField(initial='survey')
    erq_1 = models.StringField(label="When I want to feel more positive emotion (such as joy or amusement), I change what I’m thinking about.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"] ,widget=widgets.RadioSelectHorizontal)

# FUNCTIONS
# PAGES

class ERQ(Page):
    form_model = 'player'
    form_fields = ['erq_1']

page_sequence = [ERQ]#scale2, scale3
