from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'video'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    link1 = "https://www.dropbox.com/s/ea7kwk5wowrqse9/mostshocking2day.mp4?raw=1"
    link2 = "https://www.dropbox.com/s/ik6xpzehvmef0qb/loveyou_video.mp4?raw=1"


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField()
    treatment = models.CharField(initial='video1')
    infoq = models.IntegerField(label="Did the video provide any new information than the information proided in the description?", choices = [[1,"Yes"],[0,"No"]])
    controlq = models.IntegerField( label="Control question1",choices = [[1,"Option1"],[2, "Option2"], [ 3, "Option3"]], widget=widgets.RadioSelect)
    openq = models.LongStringField(label="Explain in the space below your thoughts and feelings after the video ")

class Welcome(Page):
    form_model = 'player'


class GeneralInstructions(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

class Desc(Page):
    form_model = 'player'

class Video(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        link = C.link1
        return dict(
            link = link
         )

    #def is_displayed(player: Player):
     #   return player.participant.treatment == 1



    #def vars_for_template(player: Player):
        #if player.participant.treatment == True:
        #if player.participant.treatment == True:
        #    link = C.link1
        #else:
        #   link = C.link2
        #return dict(
        #    link = link
        #)

class Video2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.treatment == 0

class Openq(Page):
    form_model = 'player'
    form_fields = ['openq']

class Control(Page):
    form_model = 'player'
    form_fields = ['controlq','infoq']

class Info_q(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class Task(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']

class InstructionsTask1(Page):
    form_model = 'player'
  #  form_fields = ['erq_1','erq_2', 'erq_3','erq_4','erq_5','erq_6','erq_7','erq_8','erq_9','erq_10']


page_sequence = [Welcome, GeneralInstructions, Desc, Video, Openq, Control]
#page_sequence = [Welcome, GeneralInstructions, Desc, Video,Video2 Info_q,  InstructionsTask1, Task]