from otree.api import *
import random
import math


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'decision'
    players_per_group = None
    num_rounds = 1
    dictator_role = 'role A'
    recipient_role = 'role B'
    low_wage = 1
    high_wage = 2
    choice_interval = 1

    all_possible_earnings = list(set([round(1*i,1) for i in range(0,11)]+[round(2*i,1) for i in range(0,11)]))
    all_possible_earnings.sort()    

    # The two following dictionaries are the dictionaries for all the wgae-income combinations and incomes.
    yo_dic = {0:{'wage':low_wage,'income':round(low_wage*0,1)},
    1:{'wage':low_wage,'income':round(low_wage*1,1)},
    2:{'wage':low_wage,'income':round(low_wage*2,1)},
    3:{'wage':low_wage,'income':round(low_wage*3,1)},
    4:{'wage':low_wage,'income':round(low_wage*4,1)},
    5:{'wage':low_wage,'income':round(low_wage*5,1)},
    6:{'wage':low_wage,'income':round(low_wage*6,1)},
    7:{'wage':low_wage,'income':round(low_wage*7,1)},
    8:{'wage':low_wage,'income':round(low_wage*8,1)},
    9:{'wage':low_wage,'income':round(low_wage*9,1)},
    10:{'wage':low_wage,'income':round(low_wage*10,1)},
    11:{'wage':high_wage,'income':round(high_wage*0,1)},
    12:{'wage':high_wage,'income':round(high_wage*1,1)},
    13:{'wage':high_wage,'income':round(high_wage*2,1)},
    14:{'wage':high_wage,'income':round(high_wage*3,1)},
    15:{'wage':high_wage,'income':round(high_wage*4,1)},
    16:{'wage':high_wage,'income':round(high_wage*5,1)},
    17:{'wage':high_wage,'income':round(high_wage*6,1)},
    18:{'wage':high_wage,'income':round(high_wage*7,1)},
    19:{'wage':high_wage,'income':round(high_wage*8,1)},
    20:{'wage':high_wage,'income':round(high_wage*9,1)},
    21:{'wage':high_wage,'income':round(high_wage*10,1)}}

    no_dic = {0:{'income':all_possible_earnings[0]},
    1:{'income':all_possible_earnings[1]},
    2:{'income':all_possible_earnings[2]},
    3:{'income':all_possible_earnings[3]},
    4:{'income':all_possible_earnings[4]},
    5:{'income':all_possible_earnings[5]},
    6:{'income':all_possible_earnings[6]},
    7:{'income':all_possible_earnings[7]},
    8:{'income':all_possible_earnings[8]},
    9:{'income':all_possible_earnings[9]},
    10:{'income':all_possible_earnings[10]},
    11:{'income':all_possible_earnings[11]},
    12:{'income':all_possible_earnings[12]},
    13:{'income':all_possible_earnings[13]},
    14:{'income':all_possible_earnings[14]},
    15:{'income':all_possible_earnings[15]}}    


class Subsession(BaseSubsession):
    pass
        
def creating_session(subsession): 
    for player in subsession.get_players():
        player.low_wage_first = random.choice([True,False])

class Group(BaseGroup):
    pass


def make_transfer_field(wage,income,treatment,role): # The function for implementing the role A's decision.
    if treatment==1 and role==1:
        label=f'If the participant paired with you has earned ${income} with a wage of ${wage} per table from the counting task, how much do you want to give to the participant?'
    elif treatment==2 and role==1:
        label=f'If the participant paired with you has earned ${income}, how much do you want to give to the participant?'
    elif treatment==1 and role==2:
        label=f'If the participant paired with you has earned ${income} with a wage of ${wage} per table from the counting task, how much do you think the participant will give you?'
    elif treatment==2 and role==2:
        label=f'If the participant paired with you has earned ${income}, how much do you think the participant will give you?'

    if role==1:
        return models.CurrencyField(
            label=label,
            widget=widgets.RadioSelect
        )
    elif role==2:
        return models.CurrencyField(
            choices = currency_range(0,cu(income),Constants.choice_interval),
            label=label,
            widget=widgets.RadioSelect
        )              

############################################################
def make_belief_field(income): # This function set the arguments of belief variables
    return models.IntegerField(
        min=0,
        max=100,
        label=f'What percentage of participants who earned ${income} do you think were assigned a wage of $2 per table? (from 0 to 100)',
    )    

class Player(BasePlayer):
    low_wage_first = models.BooleanField()

    treatment = models.IntegerField()
    more_high_wage = models.BooleanField()
    yo_l_00 = make_transfer_field(Constants.low_wage,Constants.yo_dic[0]['income'],1,1)
    yo_l_01 = make_transfer_field(Constants.low_wage,Constants.yo_dic[1]['income'],1,1)
    yo_l_02 = make_transfer_field(Constants.low_wage,Constants.yo_dic[2]['income'],1,1)
    yo_l_03 = make_transfer_field(Constants.low_wage,Constants.yo_dic[3]['income'],1,1)
    yo_l_04 = make_transfer_field(Constants.low_wage,Constants.yo_dic[4]['income'],1,1)
    yo_l_05 = make_transfer_field(Constants.low_wage,Constants.yo_dic[5]['income'],1,1)
    yo_l_06 = make_transfer_field(Constants.low_wage,Constants.yo_dic[6]['income'],1,1)
    yo_l_07 = make_transfer_field(Constants.low_wage,Constants.yo_dic[7]['income'],1,1)
    yo_l_08 = make_transfer_field(Constants.low_wage,Constants.yo_dic[8]['income'],1,1)
    yo_l_09 = make_transfer_field(Constants.low_wage,Constants.yo_dic[9]['income'],1,1)
    yo_l_10 = make_transfer_field(Constants.low_wage,Constants.yo_dic[10]['income'],1,1)
    yo_h_00 = make_transfer_field(Constants.high_wage,Constants.yo_dic[11]['income'],1,1)
    yo_h_01 = make_transfer_field(Constants.high_wage,Constants.yo_dic[12]['income'],1,1)
    yo_h_02 = make_transfer_field(Constants.high_wage,Constants.yo_dic[13]['income'],1,1)
    yo_h_03 = make_transfer_field(Constants.high_wage,Constants.yo_dic[14]['income'],1,1)
    yo_h_04 = make_transfer_field(Constants.high_wage,Constants.yo_dic[15]['income'],1,1)
    yo_h_05 = make_transfer_field(Constants.high_wage,Constants.yo_dic[16]['income'],1,1)
    yo_h_06 = make_transfer_field(Constants.high_wage,Constants.yo_dic[17]['income'],1,1)
    yo_h_07 = make_transfer_field(Constants.high_wage,Constants.yo_dic[18]['income'],1,1)
    yo_h_08 = make_transfer_field(Constants.high_wage,Constants.yo_dic[19]['income'],1,1)
    yo_h_09 = make_transfer_field(Constants.high_wage,Constants.yo_dic[20]['income'],1,1)
    yo_h_10 = make_transfer_field(Constants.high_wage,Constants.yo_dic[21]['income'],1,1)

    # All role B's decisions in the observable condition.
    g_yo_l_00 = make_transfer_field(Constants.low_wage,Constants.yo_dic[0]['income'],1,2)
    g_yo_l_01 = make_transfer_field(Constants.low_wage,Constants.yo_dic[1]['income'],1,2)
    g_yo_l_02 = make_transfer_field(Constants.low_wage,Constants.yo_dic[2]['income'],1,2)
    g_yo_l_03 = make_transfer_field(Constants.low_wage,Constants.yo_dic[3]['income'],1,2)
    g_yo_l_04 = make_transfer_field(Constants.low_wage,Constants.yo_dic[4]['income'],1,2)
    g_yo_l_05 = make_transfer_field(Constants.low_wage,Constants.yo_dic[5]['income'],1,2)
    g_yo_l_06 = make_transfer_field(Constants.low_wage,Constants.yo_dic[6]['income'],1,2)
    g_yo_l_07 = make_transfer_field(Constants.low_wage,Constants.yo_dic[7]['income'],1,2)
    g_yo_l_08 = make_transfer_field(Constants.low_wage,Constants.yo_dic[8]['income'],1,2)
    g_yo_l_09 = make_transfer_field(Constants.low_wage,Constants.yo_dic[9]['income'],1,2)
    g_yo_l_10 = make_transfer_field(Constants.low_wage,Constants.yo_dic[10]['income'],1,2)
    g_yo_h_00 = make_transfer_field(Constants.high_wage,Constants.yo_dic[11]['income'],1,2)
    g_yo_h_01 = make_transfer_field(Constants.high_wage,Constants.yo_dic[12]['income'],1,2)
    g_yo_h_02 = make_transfer_field(Constants.high_wage,Constants.yo_dic[13]['income'],1,2)
    g_yo_h_03 = make_transfer_field(Constants.high_wage,Constants.yo_dic[14]['income'],1,2)
    g_yo_h_04 = make_transfer_field(Constants.high_wage,Constants.yo_dic[15]['income'],1,2)
    g_yo_h_05 = make_transfer_field(Constants.high_wage,Constants.yo_dic[16]['income'],1,2)
    g_yo_h_06 = make_transfer_field(Constants.high_wage,Constants.yo_dic[17]['income'],1,2)
    g_yo_h_07 = make_transfer_field(Constants.high_wage,Constants.yo_dic[18]['income'],1,2)
    g_yo_h_08 = make_transfer_field(Constants.high_wage,Constants.yo_dic[19]['income'],1,2)
    g_yo_h_09 = make_transfer_field(Constants.high_wage,Constants.yo_dic[20]['income'],1,2)
    g_yo_h_10 = make_transfer_field(Constants.high_wage,Constants.yo_dic[21]['income'],1,2)  

    # All role A's decisions in the unobservable condition.
    no_00 = make_transfer_field(0.1,Constants.no_dic[0]['income'],2,1)
    no_01 = make_transfer_field(0.1,Constants.no_dic[1]['income'],2,1)
    no_02 = make_transfer_field(0.1,Constants.no_dic[2]['income'],2,1)
    no_03 = make_transfer_field(0.1,Constants.no_dic[3]['income'],2,1)
    no_04 = make_transfer_field(0.1,Constants.no_dic[4]['income'],2,1)
    no_05 = make_transfer_field(0.1,Constants.no_dic[5]['income'],2,1)
    no_06 = make_transfer_field(0.1,Constants.no_dic[6]['income'],2,1)
    no_07 = make_transfer_field(0.1,Constants.no_dic[7]['income'],2,1)
    no_08 = make_transfer_field(0.1,Constants.no_dic[8]['income'],2,1)
    no_09 = make_transfer_field(0.1,Constants.no_dic[9]['income'],2,1)
    no_10 = make_transfer_field(0.1,Constants.no_dic[10]['income'],2,1)
    no_12 = make_transfer_field(0.1,Constants.no_dic[11]['income'],2,1)
    no_14 = make_transfer_field(0.1,Constants.no_dic[12]['income'],2,1)
    no_16 = make_transfer_field(0.1,Constants.no_dic[13]['income'],2,1)
    no_18 = make_transfer_field(0.1,Constants.no_dic[14]['income'],2,1)
    no_20 = make_transfer_field(0.1,Constants.no_dic[15]['income'],2,1)

    # All role B's decisions in the unobservable condition.
    g_no_00 = make_transfer_field(0.1,Constants.no_dic[0]['income'],2,2)
    g_no_01 = make_transfer_field(0.1,Constants.no_dic[1]['income'],2,2)
    g_no_02 = make_transfer_field(0.1,Constants.no_dic[2]['income'],2,2)
    g_no_03 = make_transfer_field(0.1,Constants.no_dic[3]['income'],2,2)
    g_no_04 = make_transfer_field(0.1,Constants.no_dic[4]['income'],2,2)
    g_no_05 = make_transfer_field(0.1,Constants.no_dic[5]['income'],2,2)
    g_no_06 = make_transfer_field(0.1,Constants.no_dic[6]['income'],2,2)
    g_no_07 = make_transfer_field(0.1,Constants.no_dic[7]['income'],2,2)
    g_no_08 = make_transfer_field(0.1,Constants.no_dic[8]['income'],2,2)
    g_no_09 = make_transfer_field(0.1,Constants.no_dic[9]['income'],2,2)
    g_no_10 = make_transfer_field(0.1,Constants.no_dic[10]['income'],2,2)
    g_no_12 = make_transfer_field(0.1,Constants.no_dic[11]['income'],2,2)
    g_no_14 = make_transfer_field(0.1,Constants.no_dic[12]['income'],2,2)
    g_no_16 = make_transfer_field(0.1,Constants.no_dic[13]['income'],2,2)
    g_no_18 = make_transfer_field(0.1,Constants.no_dic[14]['income'],2,2)
    g_no_20 = make_transfer_field(0.1,Constants.no_dic[15]['income'],2,2)        

    believe_income_00 = make_belief_field(Constants.no_dic[0]['income'])
    believe_income_01 = make_belief_field(Constants.no_dic[1]['income'])
    believe_income_02 = make_belief_field(Constants.no_dic[2]['income'])
    believe_income_03 = make_belief_field(Constants.no_dic[3]['income'])
    believe_income_04 = make_belief_field(Constants.no_dic[4]['income'])
    believe_income_05 = make_belief_field(Constants.no_dic[5]['income'])
    believe_income_06 = make_belief_field(Constants.no_dic[6]['income'])
    believe_income_07 = make_belief_field(Constants.no_dic[7]['income'])
    believe_income_08 = make_belief_field(Constants.no_dic[8]['income'])
    believe_income_09 = make_belief_field(Constants.no_dic[9]['income'])
    believe_income_10 = make_belief_field(Constants.no_dic[10]['income'])
    believe_income_12 = make_belief_field(Constants.no_dic[11]['income'])
    believe_income_14 = make_belief_field(Constants.no_dic[12]['income'])
    believe_income_16 = make_belief_field(Constants.no_dic[13]['income'])
    believe_income_18 = make_belief_field(Constants.no_dic[14]['income'])
    believe_income_20 = make_belief_field(Constants.no_dic[15]['income'])

    post_q1 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=list(range(1,11)),
    )

    post_q2 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=list(range(1,11)),
    )    
    
    feedback = models.LongStringField(label='Please let us know how do you make your decisions.')
    confirmation_code = models.StringField()

#############################################
# This functions serves the multiple choices for role A based on their earning
def transfer_choices_function(player):
    choices = currency_range(0,player.participant.earning,Constants.choice_interval)
    return choices

yo_l_00_choices = transfer_choices_function
yo_l_01_choices = transfer_choices_function
yo_l_02_choices = transfer_choices_function
yo_l_03_choices = transfer_choices_function
yo_l_04_choices = transfer_choices_function
yo_l_05_choices = transfer_choices_function
yo_l_06_choices = transfer_choices_function
yo_l_07_choices = transfer_choices_function
yo_l_08_choices = transfer_choices_function
yo_l_09_choices = transfer_choices_function
yo_l_10_choices = transfer_choices_function
yo_h_00_choices = transfer_choices_function
yo_h_01_choices = transfer_choices_function
yo_h_02_choices = transfer_choices_function
yo_h_03_choices = transfer_choices_function
yo_h_04_choices = transfer_choices_function
yo_h_05_choices = transfer_choices_function
yo_h_06_choices = transfer_choices_function
yo_h_07_choices = transfer_choices_function
yo_h_08_choices = transfer_choices_function
yo_h_09_choices = transfer_choices_function
yo_h_10_choices = transfer_choices_function     

no_00_choices = transfer_choices_function 
no_01_choices = transfer_choices_function 
no_02_choices = transfer_choices_function 
no_03_choices = transfer_choices_function 
no_04_choices = transfer_choices_function 
no_05_choices = transfer_choices_function 
no_06_choices = transfer_choices_function 
no_07_choices = transfer_choices_function 
no_08_choices = transfer_choices_function 
no_09_choices = transfer_choices_function 
no_10_choices = transfer_choices_function 
no_12_choices = transfer_choices_function 
no_14_choices = transfer_choices_function 
no_16_choices = transfer_choices_function 
no_18_choices = transfer_choices_function 
no_20_choices = transfer_choices_function 
   

class Decision_instruction(Page):
    pass


class Decision_roleA_yo(Page): # role A in the observable condition
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        low_wage_form = ['yo_l_00', 'yo_l_01', 'yo_l_02', 'yo_l_03', 'yo_l_04', 'yo_l_05', 'yo_l_06', 'yo_l_07', 'yo_l_08', 'yo_l_09', 'yo_l_10']
        high_wage_form = ['yo_h_00', 'yo_h_01', 'yo_h_02', 'yo_h_03', 'yo_h_04', 'yo_h_05', 'yo_h_06', 'yo_h_07', 'yo_h_08', 'yo_h_09', 'yo_h_10']
        if player.low_wage_first == True:
            form_fields = low_wage_form+high_wage_form
        else:
            form_fields = high_wage_form+low_wage_form

        return form_fields  
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == Constants.dictator_role and player.participant.treatment == 1
    # @staticmethod
    # def get_timeout_seconds(player):
    #     # participant = player.participant
    #     if player.is_dropout:
    #         return 1  # instant timeout, 1 second
    #     else:
    #         return 10*60   
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        earning = participant.earning
        if participant.more_high_wage == True:
            p_lowwage = '25%'
            p_highwage = '75%'
        elif participant.more_high_wage == False:
            p_lowwage = '75%'
            p_highwage = '25%'        
        return dict(
            earning=earning, p_lowwage=p_lowwage,p_highwage=p_highwage
        )                    
                    

class Decision_roleB_yo(Page): # role B in the observable condition
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        low_wage_form = ['g_yo_l_00', 'g_yo_l_01', 'g_yo_l_02', 'g_yo_l_03', 'g_yo_l_04', 'g_yo_l_05', 'g_yo_l_06', 'g_yo_l_07', 'g_yo_l_08', 'g_yo_l_09', 'g_yo_l_10']
        high_wage_form = ['g_yo_h_00', 'g_yo_h_01', 'g_yo_h_02', 'g_yo_h_03', 'g_yo_h_04', 'g_yo_h_05', 'g_yo_h_06', 'g_yo_h_07', 'g_yo_h_08', 'g_yo_h_09', 'g_yo_h_10']
        if player.low_wage_first == True:
            form_fields = low_wage_form+high_wage_form
        else:
            form_fields = high_wage_form+low_wage_form    
        return form_fields     
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == Constants.recipient_role and player.participant.treatment == 1
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        if participant.more_high_wage == True:
            p_lowwage = '25%'
            p_highwage = '75%'
        elif participant.more_high_wage == False:
            p_lowwage = '75%'
            p_highwage = '25%'        
        return dict(
            p_lowwage=p_lowwage,p_highwage=p_highwage
        )                                    

class Decision_roleA_no(Page): # role A in the unobservable condition
    form_model = 'player'
    form_fields = ['no_00','no_01','no_02','no_03','no_04','no_05','no_06','no_07','no_08','no_09','no_10','no_12','no_14','no_16','no_18','no_20']
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == Constants.dictator_role and player.participant.treatment == 2
  
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        earning = participant.earning
        if participant.more_high_wage == True:
            p_lowwage = '25%'
            p_highwage = '75%'
        elif participant.more_high_wage == False:
            p_lowwage = '75%'
            p_highwage = '25%'          
        return dict(
            earning=earning,p_lowwage=p_lowwage,p_highwage=p_highwage
        )        
          

class Decision_roleB_no(Page): # role B in the unobservable condition
    form_model = 'player'
    form_fields = ['g_no_00','g_no_01','g_no_02','g_no_03','g_no_04','g_no_05','g_no_06','g_no_07','g_no_08','g_no_09','g_no_10','g_no_12','g_no_14','g_no_16','g_no_18','g_no_20']
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.role == Constants.recipient_role  and player.participant.treatment == 2
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        if participant.more_high_wage == True:
            p_lowwage = '25%'
            p_highwage = '75%'
        elif participant.more_high_wage == False:
            p_lowwage = '75%'
            p_highwage = '25%'          
        return dict(
            p_lowwage=p_lowwage,p_highwage=p_highwage
        )           


class Belief(Page):
    form_model = 'player'
    form_fields = ['believe_income_00','believe_income_01','believe_income_02','believe_income_03','believe_income_04','believe_income_05','believe_income_06','believe_income_07','believe_income_08','believe_income_09','believe_income_10','believe_income_12','believe_income_14','believe_income_16','believe_income_18','believe_income_20']
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        if participant.more_high_wage == True:
            p_lowwage = '25%'
            p_highwage = '75%'
        elif participant.more_high_wage == False:
            p_lowwage = '75%'
            p_highwage = '25%'          
        return dict(
            p_lowwage=p_lowwage,p_highwage=p_highwage
        )    


class Post_survey(Page):
    form_model = 'player'
    form_fields = ['post_q1','post_q2']

class Feedback(Page): # The page for the open-ended feedback
    form_model = 'player'
    form_fields = ['feedback']


class RM(Page): # The page for the confirmation code
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        label = participant.label
        return dict(
            label=label,
        )    



page_sequence = [Decision_instruction, Decision_roleA_yo, Decision_roleB_yo, Decision_roleA_no, Decision_roleB_no,  Belief, Post_survey, Feedback, RM]
