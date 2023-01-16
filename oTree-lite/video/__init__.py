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
    consent = models.BooleanField()
    task1 = models.StringField(blank=True)
    treatment = models.CharField(initial='video1')
    infoq = models.IntegerField(label="Did the video provide any new information other than the one previously provided in the video description?", choices = [[1,"Yes"],[0,"No"]])
    openq = models.LongStringField(label="Explain in the space below other thoughts and feelings associated to watching the video ")

    def make_field(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
            label=label,
            widget=widgets.RadioSelect,
        )
    happy = make_field(label="Happy")
    sad = make_field(label="Sad")
    fear = make_field(label="Fear")
    disgust = make_field(label="Disgust")
    anger = make_field(label="Anger")
    compassion = make_field(label="Compassion")
    guilt = make_field(label="Guilt")
    boredom = make_field(label="Boredom")

    q_number = models.IntegerField(
        choices=[1,2,3,4,5],
        label="Control question",
        widget=widgets.RadioSelect,
    )
    q_feedback = models.LongStringField(label="This is the end of the survey. "
                                            "In case you have comments, please leave them here.",
                                      blank=True)
    q_feedback_pilot = models.LongStringField(label="If you found any instructions unclear or confusing, please let us know here.",
                                            blank=True)


class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

class Desc(Page):
    form_model = 'player'

class Attention1(Page):
    form_model = 'player'
    form_fields = ["q_number"]

class FailedAttention(Page):
        form_model = 'player'
        form_fields = ["q_number"]

        @staticmethod
        def is_displayed(player: Player):
            return player.q_number != 2

        @staticmethod
        def error_message(player, values):
            solutions = dict(
                q_number=2)

            error_message=dict()

            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'
                return 'Error. You did not select any option. Please select an option'
            return error_message

        def js_vars(player):
            error_code = player.session.config["error_code"]
            link = "https://app.prolific.co/submissions/complete?cc=" + str(error_code)
            return dict(
                errorlink=link
                 )
        pass

class Survey1(Page):
    form_model = 'player'
    form_fields = ["happy","sad", "fear", "disgust","anger", "compassion", "guilt", "boredom"]

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

class Survey2(Page):
    form_model = 'player'

    form_fields = ["happy","sad", "fear", "disgust","anger", "compassion", "guilt", "boredom"]


class Openq(Page):
    form_model = 'player'
    form_fields = ['openq']

class Hypo_choice(Page):
    form_model = 'player'
    form_fields = ['task1']

class FinalSurvey(Page):
    form_model = 'player'
    form_fields = ['q_feedback', 'q_feedback_pilot']

page_sequence = [Welcome, Desc, Survey1, Attention1,FailedAttention, Video, Survey2,  Openq, Hypo_choice, FinalSurvey]
