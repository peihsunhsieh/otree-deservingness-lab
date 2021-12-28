from otree import constants
from otree.api import *
import random

doc = """
This app includes the instruction and the comprehension check.
"""


class Constants(BaseConstants):
    name_in_url = 'instruction_and_quiz'
    players_per_group = None
    num_rounds = 1
    low_wage_rate = 0.1
    high_wage_rate = 0.2
    # 1 is the instruction for the obervble condition, 2 is the instruction for the unobervble condition
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
    ],}

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    failed_too_many = models.BooleanField(initial=False) # if a subject failed more than 3 questions in a quiz
    more_high_wage = models.BooleanField() # False: 75% of the low-wage and 25% of the high-wage; True: 25% of the low-wage and 25% of the high-wage
    treatment = models.IntegerField() # 1: observable, 2: unobservable_free_effort, 3: unobservable
    # Comprehension check questions
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
            [1, f'${Constants.low_wage_rate}'],
            [2, f'${Constants.high_wage_rate}'],
            [3, f'${Constants.low_wage_rate} or ${Constants.high_wage_rate}, which will be randomly assigned in the wage rate assignment stage.'],
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
        label="What is the probability of being assigned $0.1 as the bonus per table in the counting task stage?",
        widget=widgets.RadioSelect
    )  
    cc4 = models.IntegerField(
        choices=[
            [1, '$1'],
            [2, '$1.5'],
            [3, '$2'],
            [4, '$2.5'],
        ],
        label="If your wage rate is $0.2 per table, what is the maximum bonus you could earn from the counting task?",
        widget=widgets.RadioSelect
    )      

    # If a subject answers a question "wrong"
    cc1_correct = models.IntegerField(initial=0)
    cc2_correct = models.IntegerField(initial=0)
    cc3_correct = models.IntegerField(initial=0)
    cc4_correct = models.IntegerField(initial=0)

 

def creating_session(subsession):
    subsession.session.low_wage_rate = Constants.low_wage_rate
    subsession.session.high_wage_rate = Constants.high_wage_rate
    # block randomization for more_highwage X observability
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
    

def vars_for_wage_distribution(more_high_wage):
    # Show different percentages of the low wage and high wage, respectively
    if more_high_wage == True:
        p_lowwage = '25%'
        p_highwage = '75%'
    elif more_high_wage == False:
        p_lowwage = '75%'
        p_highwage = '25%'
    return dict(
            p_lowwage=p_lowwage, p_highwage=p_highwage,
        )    

# PAGES
class Instruction(Page):
    @staticmethod
    def vars_for_template(player):
        # Show different percentages of the low wage and high wage, respectively
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )    

class Instruction_comprehension_questions(Page):
    @staticmethod
    def vars_for_template(player):
        # Show different percentages of the low wage and high wage, respectively
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )    

class Instruction_wage_rate_assignment(Page):
    @staticmethod
    def vars_for_template(player):
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )    
class Instruction_counting_zeros(Page):
    @staticmethod
    def vars_for_template(player):
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )    

class Instruction_paired_with_a_partner(Page):
    @staticmethod
    def vars_for_template(player):
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )   

class Instruction_income_transfer(Page):
    @staticmethod
    def vars_for_template(player):
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )    

class Instruction_second_survey(Page):
    @staticmethod
    def vars_for_template(player):
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )    

class Instruction_payments(Page):
    @staticmethod
    def vars_for_template(player):
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
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
            cc2='The wage per table in the counting task stage can be $0.1 or $0.2, which will be randomly assigned in the wage rate assignment stage.',
            cc3='The probability of being assigned $0.1 as the bonus per table in the counting task stage is 25%.' if player.more_high_wage == True else 'The probability of being assigned $0.1 as the bonus per table in the counting task stage is 75%.',
            cc4='If your wage rate is $0.2 per table, the maximum bonus you could earn from the counting task is $2.' )
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
    @staticmethod
    def vars_for_template(player):
        # if player.more_high_wage == True:
        #     p_lowwage = '25%'
        #     p_highwage = '75%'
        # elif player.more_high_wage == False:
        #     p_lowwage = '75%'
        #     p_highwage = '25%'

        treatment = 1 if player.treatment == 1 else 2
        
        return dict(
            p_lowwage=vars_for_wage_distribution(player.more_high_wage)['p_lowwage'], p_highwage=vars_for_wage_distribution(player.more_high_wage)['p_highwage'], treatment=treatment,
        )           

class Failed(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return 'end'     

page_sequence = [Instruction, Instruction_comprehension_questions, Instruction_wage_rate_assignment, Instruction_counting_zeros, Instruction_paired_with_a_partner, Instruction_income_transfer, Instruction_second_survey, Instruction_payments, ComprehensiveQuestions, Failed]
