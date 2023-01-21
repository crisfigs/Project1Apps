from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'video'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    link1 = "https://www.dropbox.com/s/ea7kwk5wowrqse9/mostshocking2day.mp4?raw=1"
    link2 = "https://www.dropbox.com/s/ik6xpzehvmef0qb/loveyou_video.mp4?raw=1"
    correct_answers = {"controlq_cake": 1,
                       "controlq_flute": 1,
                       "controlq_star": 1,
                       "controlq_airplane": 0}


class Group(BaseGroup):
    pass


class Subsession(BaseSubsession):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField()
    sum_correct = models.IntegerField()
    task1 = models.StringField(blank=True)
    treatment = models.CharField(initial='video1')

    openq = models.LongStringField(label="Explain in the space below other thoughts and feelings associated to watching the video ")
    def make_field(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
            label=label,
            widget=widgets.RadioSelect,
        )
    def make_field2(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4],
            label=label,
            widget=widgets.RadioSelect,
        )
    def make_field3(label):
        return models.IntegerField(
            choices=[
                [0, 'False'],
                [1, 'True']],
            label=label,
            widget=widgets.RadioSelect,
        )
    happy1 = make_field(label="Happy")
    sad1 = make_field(label="Sad")
    fear1 = make_field(label="Fear")
    disgust1 = make_field(label="Disgust")
    anger1 = make_field(label="Anger")
    compassion1 = make_field(label="Compassion")
    guilt1 = make_field(label="Guilt")
    boredom1 = make_field(label="Boredom")
    happy2 = make_field(label="Happy")
    sad2 = make_field(label="Sad")
    fear2 = make_field(label="Fear")
    disgust2 = make_field(label="Disgust")
    anger2 = make_field(label="Anger")
    compassion2 = make_field(label="Compassion")
    guilt2 = make_field(label="Guilt")
    boredom2 = make_field(label="Boredom")
    controlq_cake = make_field3(label="...a girl blowing some candles.")
    controlq_flute = make_field3(label="...a flute.")
    controlq_star = make_field3(label="...a firework.")
    controlq_airplane = models.IntegerField(
            choices=[
                [1, 'False'],
                [0, 'True']],
            label="...a girl on an airplane.",
            widget=widgets.RadioSelect)

    qemp1 = make_field2(label="I can easily tell if someone else wants to enter a conversation.")
    qemp3 = make_field2(label="I really enjoy caring for other people.")
    qemp4 = make_field2(label="I find it hard to know what to do in a social situation.")
    qemp8 = make_field2(label="I often find it difficult to judge if something is rude or polite.")
    qemp9 = make_field2(label="In a conversation, I tend to focus on my own thoughts rather than on what my listener might be thinking.")
    qemp11 = make_field2(label="I can pick up quickly if someone says one thing but means another.")
    qemp12 = make_field2(label="It is hard for me to see why some things upset people so much.")
    qemp13 = make_field2(label="I find it easy to put myself in somebody else’s shoes.")
    qemp14 = make_field2(label="I am good at predicting how someone will feel.")
    qemp15 = make_field2(label="I am quick to spot when someone in a group is feeling awkward or uncomfortable.")
    qemp18 = make_field2(label="I can’t always see why someone should have felt offended by a remark.")
    qemp21 = make_field2(label="I don’t tend to find social situations confusing.")
    qemp22 = make_field2(label="Other people tell me I am good at understanding how they are feeling and what they are thinking.")
    qemp26 = make_field2(label="I can easily tell if someone else is interested or bored with what I am saying.")
    qemp28 = make_field2(label="Friends usually talk to me about their problems as they say that I am very understanding.")
    qemp29 = make_field2(label="I can sense if I am intruding, even if the other person doesn’t tell me.")
    qemp31 = make_field2(label="Other people often say that I am insensitive, though I don’t always see why.")
    qemp34 = make_field2(label="I can tune into how someone else feels rapidly and intuitively.")
    qemp35 = make_field2(label="I can easily work out what another person might want to talk about.")
    qemp36 = make_field2(label="I can tell if someone is masking their true emotion.")
    qemp38 = make_field2(label="I am good at predicting what someone will do.")
    qemp39 = make_field2(label="I tend to get emotionally involved with a friend’s problems.")

    q_feedback = models.LongStringField(label="This is the end of the survey. "
                                            "In case you have comments, please leave them here.",
                                      blank=True)
    q_feedback_pilot = models.LongStringField(label="If you found any instructions unclear or confusing, please let us know here.",
                                            blank=True)
    donationq = models.IntegerField(label="Are you already a donor for Save the Children?", choices = [[1,"Yes"],[0,"No"]])
    donationqother = models.IntegerField(label="Are you already a donor for any other charity?", choices=[[1, "Yes"], [0, "No"]])
    charityq = models.IntegerField(label="Do you think Save the Children is a good charity?", choices = [[1,"Yes"],[0,"No"]])



class Welcome(Page):
    form_model = 'player'
    form_fields = ['prolific_id']

class Desc(Page):
    form_model = 'player'

class Attention1(Page):
    form_model = 'player'
    form_fields = ["controlq_cake", "controlq_flute", "controlq_star","controlq_airplane"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.sum_correct = player.controlq_cake + player.controlq_flute + player.controlq_star + player.controlq_airplane

class FailedAttention(Page):
        form_model = 'player'
        form_fields = ["controlq_cake", "controlq_flute", "controlq_star","controlq_airplane"]

        @staticmethod
        def is_displayed(player: Player):
            return player.sum_correct <= 3


        def js_vars(player):
            error_code = player.session.config["error_code"]
            link = "https://app.prolific.co/submissions/complete?cc=" + str(error_code)
            return dict(
                errorlink=link
                 )
        pass

class Survey1(Page):
    form_model = 'player'
    form_fields = ["happy1","sad1", "fear1", "disgust1","anger1", "compassion1", "guilt1", "boredom1"]

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

    form_fields = ["happy2","sad2", "fear2", "disgust2","anger2", "compassion2", "guilt2", "boredom2"]


class Openq(Page):
    form_model = 'player'
    form_fields = ['openq']

class Hypo_choice(Page):
    form_model = 'player'
    form_fields = ['task1']

class Hypo_choiceq(Page):
    form_model = 'player'
    form_fields = ['donationq','donationqother','charityq']

class EQ(Page):
    form_model='player'
    form_fields = ["qemp1", "qemp3", "qemp4","qemp8",
                   "qemp9" , "qemp11", "qemp12","qemp13",
                   "qemp14","qemp15","qemp18","qemp21", "qemp22",
                   "qemp26", "qemp28", "qemp29", "qemp31", "qemp34",
                    "qemp35", "qemp36", "qemp38", "qemp39"]

class Feedback(Page):
    form_model = 'player'
    form_fields = ['q_feedback', 'q_feedback_pilot']


page_sequence = [Welcome, Desc, Survey1, Video, Survey2, Openq, Attention1,FailedAttention, Hypo_choice,Hypo_choiceq, EQ, Feedback]

