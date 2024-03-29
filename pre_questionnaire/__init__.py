from otree.api import *


doc = """
Pre-game survey
"""


class Constants(BaseConstants):
    name_in_url = 'pre_questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        choices=[
            [0, 'Female'],
            [1, 'Male'],
            [2, 'Other'],
        ],
        widget=widgets.RadioSelect
    )
    year_of_birth = models.IntegerField(min=1921, max=2006)
    household_income = models.IntegerField(min=0)
    education = models.IntegerField(
        choices=[
            [0, 'Less than 12th grade'],
            [1, 'High school graduate - High school diploma or equivalent (for example: GED)'],
            [2, 'Some college but no degree'],
            [3, 'Associate degree in college - Occupational/vocational program'],
            [4, 'Associate degree in college - Academic program'],
            [5, 'Bachelor’s degree (For example: BA, AB, BS)'],
            [6, 'Master’s degree (For example: MA, MS, MEng, MEd, MSW, MBA)'],
            [7, 'Professional school Degree (For example: MD,DDS,DVM,LLB,JD)'],
            [8, 'Doctorate degree (For example: PhD, EdD)'],
        ],
        widget=widgets.RadioSelect
    )
    pid0 = models.IntegerField(
        choices=[
            [0, 'Democrat'],
            [1, 'Republican'],
            [2, 'Independent'],
            [3, 'Other'],
        ],
        widget=widgets.RadioSelect
    )
    pid0others = models.StringField()
    pid1 = models.IntegerField(
        choices=[
            [0, 'Not very strong'],
            [1, 'Strong'],
        ],
        widget=widgets.RadioSelect
    )
    pid6 = models.IntegerField(
        choices=[
            [0, 'Closer to Democratic'],
            [1, 'Neither'],
            [2, 'Closer to Republican'],
        ],
        widget=widgets.RadioSelect
    )
    ideo = models.IntegerField(
        choices=[
            [0, 'Extremely liberal'],
            [1, 'Liberal'],
            [2, 'Slightly liberal'],
            [3, 'Moderate; middle of the road'],
            [4, 'Slightly conservative'],
            [5, 'Conservative'],
            [6, 'Extremely conservative'],
            [-1, 'Haven\'t thought much about this'],
        ],
        widget=widgets.RadioSelect
    )


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['gender', 'year_of_birth', 'household_income', 'education','pid0']

class Page2(Page):
    form_model = 'player'
    form_fields = ['pid0others']
    @staticmethod
    def is_displayed(player):
        return player.pid0 == 3

class Page3(Page):
    form_model = 'player'
    form_fields = ['pid1']
    @staticmethod
    def is_displayed(player):
        return player.pid0 == 0 or player.pid0 == 1
    @staticmethod
    def vars_for_template(player):
        if player.pid0 == 0:
            party = 'Democrat'
        elif player.pid0 == 1:
            party = 'Republican'
        return dict(
            # wording is according to pid0
            pid1_label='Would you call yourself a strong {} or a not very strong {}?'.format(party,party), 
        )            


class Page4(Page):
    form_model = 'player'
    form_fields = ['pid6']
    @staticmethod
    def is_displayed(player):
        return player.pid0 == 2 or player.pid0 == 3

class Page5(Page):
    form_model = 'player'
    form_fields = ['ideo']


page_sequence = [Page1, Page2, Page3, Page4, Page5]
