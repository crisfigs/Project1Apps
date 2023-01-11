from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'end'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    q_feedback = models.LongStringField(label="This is the end of the survey. "
                                            "In case you have comments, please leave them here.",
                                      blank=True)
    q_feedback_pilot = models.LongStringField(label="If you found any instructions unclear or confusing, please let us know here.",
                                            blank=True)

# FUNCTIONS
# PAGES




class FinalSurvey(Page):
    form_model = 'player'
    form_fields = ['q_feedback', 'q_feedback_pilot']



page_sequence = [Hypo_choice, FinalSurvey]
