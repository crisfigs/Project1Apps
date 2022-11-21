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
    erq_1 = models.StringField(label="When I want to feel more positive emotion (such as joy or amusement), I change what I’m thinking about.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"] ,widget=widgets.RadioSelectHorizontal)
    erq_2 = models.StringField(label="I keep my emotions to myself.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_3 = models.StringField(label="When I want to feel less negative emotion (such as sadness or anger), I change what I’m thinking about.",
                               choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_4 = models.StringField(label="When I am feeling positive emotions, I am careful not to express them.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_5 = models.StringField(label="When I’m faced with a stressful situation, I make myself think about it in a way that helps me stay calm.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_6 = models.StringField(label="I control my emotions by not expressing them.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_7 = models.StringField(label="When I want to feel more positive emotion, I change the way I’m thinking about the situation.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_8 = models.StringField(label="I control my emotions by changing the way I think about the situation I’m in.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_9 = models.StringField(label="When I am feeling negative emotions, I make sure not to express them.",
                                choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)
    erq_10 = models.StringField(label="When I want to feel less negative emotion, I change the way I’m thinking about the situation.",
                                 choices=["(Strongly disagree) 1", "2", "3", "4", "5"," 6", "(Strongly Agree) 7"],widget=widgets.RadioSelectHorizontal)

# FUNCTIONS
# PAGES

class ERQ(Page):
    form_model = 'player'
    form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class DT(Page):
    form_model = 'player'
    #form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']


page_sequence = [ERQ, DT]
