from otree.api import *
import random

doc = """
Many things. The sortable ranking is based on: "Widget to rank/reorder items". See http://sortablejs.github.io/Sortable/
for more examples.
"""


class C(BaseConstants):
    NAME_IN_URL = 'SimpleRanking_g'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES = ['Choose A and then watch the video.', 'Choose B and then watch the video.', 'Watch the video first and then choose between A and B.']
    #careful, elem in choices is without "".
    link1 = "https://www.dropbox.com/s/iebfy6fzuewtk34/grass.mp4?raw=1"









class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    finalRanking1 = models.StringField()
    finalRanking2 = models.StringField(blank=True)
    finalRanking3 = models.StringField(blank=True)
    pref1_1 = models.StringField()
    pref1_2 = models.StringField(blank=True)
    pref1_3 = models.StringField(blank=True)
    pref2_1 = models.StringField(blank=True)
    pref2_2 = models.StringField(blank=True)
    pref3_1 = models.StringField(blank=True)
    imp = models.StringField()
    length = models.IntegerField()
    length2 = models.IntegerField()
    length3 = models.IntegerField()
    sum_correct = models.IntegerField()
    number = models.IntegerField()
    payment_number = models.IntegerField()
    payment= models.IntegerField()

    #Comprehension questions
    q1A = models.IntegerField(label="1. Option A pays: ", choices = [[0,'(me: 0, charity: 5)'],[1,'(me: 5, charity: 0)'],[2,'(me: 1, charity: 4)'],[3,'(me: 1, charity: 8)'],[4,'(me: 4, charity: 0)']])
    q1B = models.IntegerField(label="2. Option B pays: ", choices = [[0,'(me: 0, charity: 8)'],[1,'(me: 1, charity: 8)'],[2,'(me: 0, charity: 5)'],[3,'(me: 4, charity: 0)'],[4,'(me: 1, charity: 4)']])
    q_change = models.IntegerField(label="3. After watching the video I can make a choice between A and B in:",
                                   choices=[[0, 'In none of the alternatives.'], [1, 'In all of the alternatives.'], [2, 'In one of the alternatives.']])
    q_video = models.IntegerField(label="4. Please state whether the following is True or False. The video is an excerpt from a promotional video by 'Lawn Solutions Australia.'", choices=[[1, 'True'], [0, 'False']])
    task1 = models.StringField(blank=True)

    def make_field(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
            label=label,
            widget=widgets.RadioSelect,
        )
    def make_field2agree(label):
        return models.IntegerField(
            choices=[0, 0, 1, 2],
            label=label,
            widget=widgets.RadioSelect,
        )
    def make_field2disagree(label):
        return models.IntegerField(
            choices=[2, 1, 0, 0],
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

    ##Questions on emotion and donation behavior
    happy2 = make_field(label="Happy")
    sad2 = make_field(label="Sad")
    fear2 = make_field(label="Fear")
    disgust2 = make_field(label="Disgust")
    anger2 = make_field(label="Anger")
    compassion2 = make_field(label="Compassion")
    guilt2 = make_field(label="Guilt")
    boredom2 = make_field(label="Boredom")
    donationq = models.IntegerField(label="1. Are you already a donor for Save the Children?",
                                        choices=[[1, "Yes"], [0, "No"]])
    donationqother = models.IntegerField(label="2. Are you already a donor for any other charity?",
                                             choices=[[1, "Yes"], [0, "No"]])
    charityq = models.IntegerField(label="3. Do you think Save the Children is a charity worth donating to?",
                                       choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    temptationqA = models.IntegerField(label="4. How tempting did the video made Option A (me:£5, charity:£0) seem?", blank=True)
    temptationqB = models.IntegerField(label="5. How tempting did the video made Option B (me:£1, charity:£8) seem?", blank=True)
    emotions_ant = models.IntegerField(label="1. To what extent did you anticipate these emotions before watching the video?", blank=True)
    openq = models.LongStringField(label="2. Explain in the space below other thoughts and feelings associated to watching the video ")
    random_q = models.IntegerField(label="6a. Sometimes you could be faced with an alternative irrespective of your ranking, namely “Watch the video first and then choose between A and B”. Did the possibility of randomnly facing that alternative affect the way you ranked your alternatives?", choices=[[1, "Yes"], [0, "No"], [2, "Unsure"]])
    random_openq = models.LongStringField(label="6b. If you answered yes to the previous question, could you elaborate why?", blank=True)

    ##Beliefs
    qa = models.IntegerField(label= "Suppose that there is someone who has provided the same ranking as you have and he/she ends up facing the alternative: 'Watch the video first and then choose between A and B.'. How likely do you think it is that she/he chooses option A?", blank=True)

    ##Attention questions video
    controlq_presenter = make_field3(label="...a male presenter.")
    controlq_drawing = make_field3(label="...a drawing.")
    controlq_woman = models.IntegerField(
        choices=[
            [1, 'False'],
            [0, 'True']],
        label="...a woman.",
        widget=widgets.RadioSelect)

    ##Empathy questionaire
    qemp1 = make_field2agree(label="I can easily tell if someone else wants to enter a conversation.")
    qemp3 = make_field2agree(label="I really enjoy caring for other people.")
    qemp4 = make_field2disagree(label="I find it hard to know what to do in a social situation.")
    qemp8 = make_field2disagree(label="I often find it difficult to judge if something is rude or polite.")
    qemp9 = make_field2disagree(label="In a conversation, I tend to focus on my own thoughts rather than on what my listener might be thinking.")
    qemp11 = make_field2agree(label="I can pick up quickly if someone says one thing but means another.")
    qemp12 = make_field2disagree(label="It is hard for me to see why some things upset people so much.")
    qemp13 = make_field2agree(label="I find it easy to put myself in somebody else’s shoes.")
    qemp14 = make_field2agree(label="I am good at predicting how someone will feel.")
    qemp15 = make_field2agree(label="I am quick to spot when someone in a group is feeling awkward or uncomfortable.")
    qemp18 = make_field2disagree(label="I can’t always see why someone should have felt offended by a remark.")
    qemp21 = make_field2agree(label="I don’t tend to find social situations confusing.")
    qemp22 = make_field2agree(
        label="Other people tell me I am good at understanding how they are feeling and what they are thinking.")
    qemp26 = make_field2agree(label="I can easily tell if someone else is interested or bored with what I am saying.")
    qemp28 = make_field2agree(
        label="Friends usually talk to me about their problems as they say that I am very understanding.")
    qemp29 = make_field2agree(label="I can sense if I am intruding, even if the other person doesn’t tell me.")
    qemp31 = make_field2disagree(label="Other people often say that I am insensitive, though I don’t always see why.")
    qemp34 = make_field2agree(label="I can tune into how someone else feels rapidly and intuitively.")
    qemp35 = make_field2agree(label="I can easily work out what another person might want to talk about.")
    qemp36 = make_field2agree(label="I can tell if someone is masking their true emotion.")
    qemp38 = make_field2agree(label="I am good at predicting what someone will do.")
    qemp39 = make_field2agree(label="I tend to get emotionally involved with a friend’s problems.")

    #Feedback questions
    q_feedback = models.LongStringField(label="This is the end of the survey. "
                                            "In case you have comments, please leave them here.",
                                      blank=True)
    q_feedback_pilot = models.LongStringField(label="If you found any instructions unclear or confusing, please let us know here.",
                                            blank=True)


    def set_error_message(player, value):
        correct_answers = {
                        'q1A': 1,
                        'q1B': 1,
                        'q_change': 2,
                        'q_video': 1}
        list_answers = list(value.items())[0:]
        list_correct_answers = list(correct_answers.items())
        if list_answers != list_correct_answers:
            Text = 'You did not answer all questions correctly. Please go back to the instructions and revise your answers.'
            return Text

###PAGES

class Part2_Instruction_Page(Page):
  form_model = 'player'
  form_fields = ['q1A', 'q1B', 'q_change', 'q_video']

  def error_message(player,value):
      return player.set_error_message(value)


class Ranking1(Page):
    form_model = 'player'
    form_fields = ['finalRanking1','finalRanking2','finalRanking3']

    def before_next_page(player: Player, timeout_happened):
        li = list(player.finalRanking1.split(","))
        player.length = len(list(player.finalRanking1.split(",")))

        if len(li)==1:
            player.pref1_1 = li[0]
            #weights=(40, 60)
            player.imp = random.choices([li[0],"'Watch the video first and then choose between A and B.'"], weights=(40,60), k=1)[0]
        elif len(li) == 2:
            player.pref1_1 = li[0]
            player.pref1_2 = li[1]
            #weights=(30,30,40)
            player.imp = random.choices([li[0],li[1], "'Watch the video first and then choose between A and B.'"], weights=(30,30,40), k=1)[0]
        elif len(li) == 3:
            player.pref1_1 = li[0]
            player.pref1_2 = li[1]
            player.pref1_3 = li[2]
            player.imp = random.choices([li[0],li[1],li[2], "'Watch the video first and then choose between A and B.'"], weights=(20,20,20,40), k=1)[0]
        else:
            player.pref1_1 = "Error"
            player.imp= "Error"

        player.length2 = len(list(player.finalRanking2.split(",")))
        li2 = list(player.finalRanking2.split(","))
        if len(li2) == 1:
            player.pref2_1 = li2[0]
        elif len(li2) == 2:
            player.pref2_1 = li2[0]
            player.pref2_2 = li2[1]
        else:
            player.pref2_1 = "Error"

        player.length3 = len(list(player.finalRanking3.split(",")))
        li3 = list(player.finalRanking3.split(","))
        if len(li2) == 1:
            player.pref3_1 = li3[0]
        else:
            player.pref3_1 = "Error"



    @staticmethod
    def vars_for_template(player: Player):
        menu = [
                { "text": C.CHOICES[0], "id": 'Choose A and then watch the video.' },
                {"text": C.CHOICES[1], "id":'Choose B and then watch the video.'},
                {"text": C.CHOICES[2], "id": "Watch the video first and then choose between A and B."}
            ]
        random.shuffle(menu)
        return dict(
            CHOICES = menu
        )




class Part3_Intro(Page):
    form_model = 'player'
    form_fields = []

    def before_next_page(player: Player, timeout_happened):
        if player.imp == "'Choose A and then watch the video.'":
            player.task1 = "A"
            player.participant.vars["task1"] = "A"
        elif player.imp == "'Choose B and then watch the video.'":
            player.task1 = "B"
            player.participant.vars["task1"] = "B"
        else:
            pass

class qa(Page):
    form_model = 'player'
    form_fields = ['qa']


class Video_alert(Page):
    pass

class Part3_Video(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod

    def vars_for_template(player):
       link = C.link1
       return dict(
            link = link)



class survey2(Page):
    form_model = 'player'

    def get_form_fields(player):
        e = ["happy2","sad2", "fear2", "disgust2","anger2", "compassion2", "guilt2", "boredom2"]
        random.shuffle(e)
        return e



class Attention1(Page):
    form_model = 'player'
    form_fields = ["controlq_presenter", "controlq_drawing","controlq_woman"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.sum_correct = player.controlq_presenter + player.controlq_drawing + player.controlq_woman
        player.number = random.choices([1,0], weights=(1, 99), k=1)[0]


class FailedAttention(Page):
        form_model = 'player'
        form_fields = ["controlq_presenter", "controlq_drawing", "controlq_woman"]

        @staticmethod
        def is_displayed(player: Player):
            return player.sum_correct <= 2 and player.number==1


        def js_vars(player):
            error_code = player.session.config["error_code"]
            link = "https://app.prolific.co/submissions/complete?cc=" + str(error_code)
            return dict(
                errorlink=link
                 )
        pass
class Hypo_choice(Page):
    form_model = 'player'
    form_fields = ['task1']

    @staticmethod
    def is_displayed(player: Player):
      return player.imp == "'Watch the video first and then choose between A and B.'"

class Hypo_choiceq(Page):
    form_model = 'player'
    form_fields = ['donationq','donationqother','charityq','temptationqA','temptationqB','random_q','random_openq']

class Openq(Page):
    form_model = 'player'
    form_fields = ['openq','emotions_ant']
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

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.payment_number = random.choices([1,0], weights=(20, 80), k=1)[0]

class Back(Page):
    form_model = 'player'
    form_fields = []

    def js_vars(player):
        cc_code = player.session.config["cc_code"]
        link = "https://app.prolific.co/submissions/complete?cc=" + str(cc_code)
        return dict(
            completionlink=link
        )

    def vars_for_template(player):
        #if selected for payment and chose A
        if player.payment_number == 1 and player.task1 == "A":
            player.payment = 5
        elif player.payment_number == 1 and player.task1 == "B":
            player.payment = 1
        else:
            pass

page_sequence = [Part2_Instruction_Page, Ranking1, Part3_Intro, Video_alert, Part3_Video, Hypo_choice, Hypo_choiceq, qa, survey2, Openq, Attention1, FailedAttention,EQ, Feedback, Back]
