from otree import constants
from otree.api import *
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'comprehension_check'
    players_per_group = None
    num_rounds = 1
    instructions = {1:['_templates/global/Instruction_comprehension_questions.html',
    '_templates/global/Instruction_wage_rate_assignment.html',
    '_templates/global/Instruction_counting_zeros.html',
    '_templates/global/Instruction_paired_with_a_partner.html',
    '_templates/global/Instruction_income_transfer_observable.html',
    '_templates/global/Instruction_second_survey.html',
    '_templates/global/Instruction_payments.html'
    ],
    2:['_templates/global/Instruction_comprehension_questions.html',
    '_templates/global/Instruction_wage_rate_assignment.html',
    '_templates/global/Instruction_counting_zeros.html',
    '_templates/global/Instruction_paired_with_a_partner.html',
    '_templates/global/Instruction_income_transfer_unobservable_free.html',
    '_templates/global/Instruction_second_survey.html',
    '_templates/global/Instruction_payments.html'
    ],
    3:['_templates/global/Instruction_comprehension_questions.html',
    '_templates/global/Instruction_wage_rate_assignment.html',
    '_templates/global/Instruction_counting_zeros_nofree.html',
    '_templates/global/Instruction_paired_with_a_partner.html',
    '_templates/global/Instruction_income_transfer_unobservable_nonfree.html',
    '_templates/global/Instruction_second_survey.html',
    '_templates/global/Instruction_payments.html'
    ],}

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    failed_too_many = models.BooleanField(initial=False)
    more_high_wage = models.BooleanField()
    treatment = models.IntegerField() # 1: observable, 2: unobservable_free_effort, 3: unobservable
    cc1 = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [2, 'No'],
        ],
        label="Does everyone who joins the study have the same wage per table by completing each table in the counting task stage?",
        widget=widgets.RadioSelect
    )  
    cc2 = models.IntegerField(
        choices=[
            [1, '10 cents'],
            [2, '20 cents'],
            [3, '10 cents or 20 cents, which will be randomly assigned in the wage rate assignment stage.'],
        ],
        label="How much is the wage per table in the counting task stage?",
        widget=widgets.RadioSelect
    )  
    cc3 = models.IntegerField(
        choices=[
            [1, '25%'],
            [2, '50%'],
            [3, '75%'],
        ],
        label="What is the probability of being assigned 10 cents as the bonus per table in the counting task stage?",
        widget=widgets.RadioSelect
    )  
    cc4 = models.IntegerField(
        choices=[
            [1, '$1'],
            [2, '$1.5'],
            [3, '$2'],
            [4, '$2.5'],
        ],
        label="If your wage rate is 20 cents per table, what is the maximum bonus you could earn from the counting task?",
        widget=widgets.RadioSelect
    )  
    cc4_nonfree = models.IntegerField(
        choices=[
            [1, '$1'],
            [2, '$1.5'],
            [3, '$2'],
            [4, 'It depends on what I am assigned.'],
        ],
        label="If your wage rate is 20 cents per table, what is the maximum bonus you could earn from the counting task?",
        widget=widgets.RadioSelect
    )        

    cc1_correct = models.IntegerField(initial=0)
    cc2_correct = models.IntegerField(initial=0)
    cc3_correct = models.IntegerField(initial=0)
    cc4_correct = models.IntegerField(initial=0)

 

def creating_session(subsession):
    # randomize to treatments
    import itertools
    treatments = itertools.cycle(
        itertools.product([True, False], [1, 2])
    )    
    for player in subsession.get_players():
        if 'treatment' in player.session.config:
            player.more_high_wage = player.session.config['more_high_wage']
            player.treatment = player.session.config['treatment']
            player.participant.more_high_wage = player.more_high_wage
            player.participant.treatment = player.treatment            
        else:
            treatment_set = next(treatments)
            player.more_high_wage = treatment_set[0]
            player.treatment = treatment_set[1]
            player.participant.more_high_wage = player.more_high_wage
            player.participant.treatment = player.treatment
    

# PAGES
class Instruction(Page):
    @staticmethod
    def vars_for_template(player):
        if player.more_high_wage == True:
            p_lowwage = '25%'
            p_highwage = '75%'
        elif player.more_high_wage == False:
            p_lowwage = '75%'
            p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=p_lowwage, p_highwage=p_highwage, treatment=treatment,
        )    


class ComprehensiveQuestions(Page):
    form_model = 'player'
    form_fields = ['cc1','cc2','cc3','cc4']  
    @staticmethod
    def error_message(player, values):
        solutions = dict(
            cc1=2,
            cc2=3,
            cc3=1 if player.more_high_wage == True else 3,
            cc4=3
        )

        error_messages_list = dict(
            cc1='Everyone who joins the study does have the same wage per table by completing each table in the counting task stage.',
            cc2='The wage per table in the counting task stage can be 10 cents or 20 cents, which will be randomly assigned in the wage rate assignment stage.',
            cc3='The probability of being assigned 10 cents as the bonus per table in the counting task stage is 25%.' if player.more_high_wage == True else 'The probability of being assigned 10 cents as the bonus per table in the counting task stage is 75%.',
            cc4='If your wage rate is 20 cents per table, the maximum bonus you could earn from the counting task is $2.' )
        error_messages = dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = error_messages_list[field_name]
                if field_name == 'cc1':
                    player.cc1_correct += 1
                elif field_name == 'cc2':
                    player.cc2_correct += 1
                elif field_name == 'cc3':
                    player.cc3_correct += 1
                elif field_name == 'cc4':
                    player.cc4_correct += 1 

                if  player.cc1_correct+player.cc2_correct+player.cc3_correct+player.cc4_correct>2:
                    player.failed_too_many = True   

        return error_messages

class Failed(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if player.consent==False:
            return 'end'     

page_sequence = [Instruction, ComprehensiveQuestions, Failed]
