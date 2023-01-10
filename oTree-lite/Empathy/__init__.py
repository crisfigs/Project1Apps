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

    #compassion (sympathy)
    #pity  (sympathy)
    #sorry (sympathy)
    #I can put myself in ....shoes (empathy)
    #Empathy means that you feel what a person is feeling (suffering/happiness).Sympathy means you can understand what the person is feeling (feel sorry for others pain or celebratory for others happiness). Compassion is the willingness to relieve the suffering of another.
    #for the videos all related to suffering because the video protray suffering
    #for the neutral video: if you had an empathy scale from 0 to 10. how empathtic did the video make you feel?
    #Def of sympathy. If you had a scale...how sympathetic did the video make you feel?
    #Def of compassion.If you had a scale...how compassionate did the video make you feel?
    #em-pathy  in pathos
    #sym-pathy with pathos
    #compassion con pasion suffer together
#if we do not see differences in sec it may  be because of norms experimenter demand effect etc if we find that, we can simply make another relative wise.Where we provide all of the videos and then just randomize the order.
#delte the control q
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
