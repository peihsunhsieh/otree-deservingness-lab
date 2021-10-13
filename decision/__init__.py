from otree.api import *
import numpy
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'decision'
    players_per_group = 2
    num_rounds = 1
    dictator_role = 'role A'
    recipient_role = 'role B'
    low_wage = 0.1
    high_wage = 0.2
    yo_dic = {0:{'wage':low_wage,'income':0},
    1:{'wage':low_wage,'income':0.1},
    2:{'wage':low_wage,'income':0.2},
    3:{'wage':low_wage,'income':0.3},
    4:{'wage':low_wage,'income':0.4},
    5:{'wage':low_wage,'income':0.5},
    6:{'wage':low_wage,'income':0.6},
    7:{'wage':low_wage,'income':0.7},
    8:{'wage':low_wage,'income':0.8},
    9:{'wage':low_wage,'income':0.9},
    10:{'wage':low_wage,'income':1},
    11:{'wage':high_wage,'income':0},
    12:{'wage':high_wage,'income':0.2},
    13:{'wage':high_wage,'income':0.4},
    14:{'wage':high_wage,'income':0.6},
    15:{'wage':high_wage,'income':0.8},
    16:{'wage':high_wage,'income':1},
    17:{'wage':high_wage,'income':1.2},
    18:{'wage':high_wage,'income':1.4},
    19:{'wage':high_wage,'income':1.6},
    20:{'wage':high_wage,'income':1.8},
    21:{'wage':high_wage,'income':2}}

    no_dic = {0:{'income':0},
    1:{'income':0.1},
    2:{'income':0.2},
    3:{'income':0.3},
    4:{'income':0.4},
    5:{'income':0.5},
    6:{'income':0.6},
    7:{'income':0.7},
    8:{'income':0.8},
    9:{'income':0.9},
    10:{'income':1},
    11:{'income':1.2},
    12:{'income':1.4},
    13:{'income':1.6},
    14:{'income':1.8},
    15:{'income':2}}    


class Subsession(BaseSubsession):
    pass

def make_transfer_field(wage,income,treatment,role):
    if treatment==1 and role==1:
        label=f'If the participant paired with you has earned ${income} with ${wage} per table, how much do do you want to give to the participant?'
    elif treatment==2 and role==1:
        label=f'If the participant paired with you has earned ${income}, how much do do you want to give to the participant?'
    elif treatment==1 and role==2:
        label=f'If the participant paired with you has earned ${income} with ${wage} per table, how much do you think the participant will give you?'
    elif treatment==2 and role==2:
        label=f'If the participant paired with you has earned ${income}, how much do you think the participant will give you?'

    if role==1:
        return models.CurrencyField(
            label=label,
            widget=widgets.RadioSelect
        )
    elif role==2:
        return models.CurrencyField(
            choices = currency_range(0,cu(income),0.1),
            label=label,
            widget=widgets.RadioSelect
        )              
        

class Group(BaseGroup):
    treatment = models.IntegerField()
    more_high_wage = models.BooleanField()
    n_players = models.IntegerField()

    yo_l_00 = make_transfer_field(Constants.low_wage,0,1,1)
    yo_l_01 = make_transfer_field(Constants.low_wage,0.1,1,1)
    yo_l_02 = make_transfer_field(Constants.low_wage,0.2,1,1)
    yo_l_03 = make_transfer_field(Constants.low_wage,0.3,1,1)
    yo_l_04 = make_transfer_field(Constants.low_wage,0.4,1,1)
    yo_l_05 = make_transfer_field(Constants.low_wage,0.5,1,1)
    yo_l_06 = make_transfer_field(Constants.low_wage,0.6,1,1)
    yo_l_07 = make_transfer_field(Constants.low_wage,0.7,1,1)
    yo_l_08 = make_transfer_field(Constants.low_wage,0.8,1,1)
    yo_l_09 = make_transfer_field(Constants.low_wage,0.9,1,1)
    yo_l_10 = make_transfer_field(Constants.low_wage,1,1,1)
    yo_h_00 = make_transfer_field(Constants.high_wage,0,1,1)
    yo_h_01 = make_transfer_field(Constants.high_wage,0.2,1,1)
    yo_h_02 = make_transfer_field(Constants.high_wage,0.4,1,1)
    yo_h_03 = make_transfer_field(Constants.high_wage,0.6,1,1)
    yo_h_04 = make_transfer_field(Constants.high_wage,0.8,1,1)
    yo_h_05 = make_transfer_field(Constants.high_wage,1,1,1)
    yo_h_06 = make_transfer_field(Constants.high_wage,1.2,1,1)
    yo_h_07 = make_transfer_field(Constants.high_wage,1.4,1,1)
    yo_h_08 = make_transfer_field(Constants.high_wage,1.6,1,1)
    yo_h_09 = make_transfer_field(Constants.high_wage,1.8,1,1)
    yo_h_10 = make_transfer_field(Constants.high_wage,2,1,1)



    g_yo_l_00 = make_transfer_field(Constants.low_wage,0,1,2)
    g_yo_l_01 = make_transfer_field(Constants.low_wage,0.1,1,2)
    g_yo_l_02 = make_transfer_field(Constants.low_wage,0.2,1,2)
    g_yo_l_03 = make_transfer_field(Constants.low_wage,0.3,1,2)
    g_yo_l_04 = make_transfer_field(Constants.low_wage,0.4,1,2)
    g_yo_l_05 = make_transfer_field(Constants.low_wage,0.5,1,2)
    g_yo_l_06 = make_transfer_field(Constants.low_wage,0.6,1,2)
    g_yo_l_07 = make_transfer_field(Constants.low_wage,0.7,1,2)
    g_yo_l_08 = make_transfer_field(Constants.low_wage,0.8,1,2)
    g_yo_l_09 = make_transfer_field(Constants.low_wage,0.9,1,2)
    g_yo_l_10 = make_transfer_field(Constants.low_wage,1,1,2)
    g_yo_h_00 = make_transfer_field(Constants.high_wage,0,1,2)
    g_yo_h_01 = make_transfer_field(Constants.high_wage,0.2,1,2)
    g_yo_h_02 = make_transfer_field(Constants.high_wage,0.4,1,2)
    g_yo_h_03 = make_transfer_field(Constants.high_wage,0.6,1,2)
    g_yo_h_04 = make_transfer_field(Constants.high_wage,0.8,1,2)
    g_yo_h_05 = make_transfer_field(Constants.high_wage,1,1,2)
    g_yo_h_06 = make_transfer_field(Constants.high_wage,1.2,1,2)
    g_yo_h_07 = make_transfer_field(Constants.high_wage,1.4,1,2)
    g_yo_h_08 = make_transfer_field(Constants.high_wage,1.6,1,2)
    g_yo_h_09 = make_transfer_field(Constants.high_wage,1.8,1,2)
    g_yo_h_10 = make_transfer_field(Constants.high_wage,2,1,2)    

    no_00 = make_transfer_field(0.1,0,2,1)
    no_01 = make_transfer_field(0.1,0.1,2,1)
    no_02 = make_transfer_field(0.1,0.2,2,1)
    no_03 = make_transfer_field(0.1,0.3,2,1)
    no_04 = make_transfer_field(0.1,0.4,2,1)
    no_05 = make_transfer_field(0.1,0.5,2,1)
    no_06 = make_transfer_field(0.1,0.6,2,1)
    no_07 = make_transfer_field(0.1,0.7,2,1)
    no_08 = make_transfer_field(0.1,0.8,2,1)
    no_09 = make_transfer_field(0.1,0.9,2,1)
    no_10 = make_transfer_field(0.1,1,2,1)
    no_12 = make_transfer_field(0.1,1.2,2,1)
    no_14 = make_transfer_field(0.1,1.4,2,1)
    no_16 = make_transfer_field(0.1,1.6,2,1)
    no_18 = make_transfer_field(0.1,1.8,2,1)
    no_20 = make_transfer_field(0.1,2,2,1)

    g_no_00 = make_transfer_field(0.1,0,2,2)
    g_no_01 = make_transfer_field(0.1,0.1,2,2)
    g_no_02 = make_transfer_field(0.1,0.2,2,2)
    g_no_03 = make_transfer_field(0.1,0.3,2,2)
    g_no_04 = make_transfer_field(0.1,0.4,2,2)
    g_no_05 = make_transfer_field(0.1,0.5,2,2)
    g_no_06 = make_transfer_field(0.1,0.6,2,2)
    g_no_07 = make_transfer_field(0.1,0.7,2,2)
    g_no_08 = make_transfer_field(0.1,0.8,2,2)
    g_no_09 = make_transfer_field(0.1,0.9,2,2)
    g_no_10 = make_transfer_field(0.1,1,2,2)
    g_no_12 = make_transfer_field(0.1,1.2,2,2)
    g_no_14 = make_transfer_field(0.1,1.4,2,2)
    g_no_16 = make_transfer_field(0.1,1.6,2,2)
    g_no_18 = make_transfer_field(0.1,1.8,2,2)
    g_no_20 = make_transfer_field(0.1,2,2,2)    

    dictator_earning = models.CurrencyField()
    dictator_wage = models.CurrencyField()
    recipient_earning = models.CurrencyField()
    recipient_wage = models.CurrencyField()    
    final_transfer = models.CurrencyField()


def transfer_choices_function(group):
    choices = currency_range(0,group.dictator_earning,0.1)
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


def make_belief_field(income):
    return models.IntegerField(
        min=0,
        max=100,
        label=f'What percentage of participants\' wage per table is $0.1 of those earned ${income} from the counting zeros task?',
    )    

class Player(BasePlayer):
    is_dropout = models.BooleanField(initial=False)
    dropout_page = models.StringField(initial='')

    believe_income_00 = make_belief_field(0)
    believe_income_01 = make_belief_field(0.1)
    believe_income_02 = make_belief_field(0.2)
    believe_income_03 = make_belief_field(0.3)
    believe_income_04 = make_belief_field(0.4)
    believe_income_05 = make_belief_field(0.5)
    believe_income_06 = make_belief_field(0.6)
    believe_income_07 = make_belief_field(0.7)
    believe_income_08 = make_belief_field(0.8)
    believe_income_09 = make_belief_field(0.9)
    believe_income_10 = make_belief_field(1)
    believe_income_12 = make_belief_field(1.2)
    believe_income_14 = make_belief_field(1.4)
    believe_income_16 = make_belief_field(1.6)
    believe_income_18 = make_belief_field(1.8)
    believe_income_20 = make_belief_field(2)

    post_q1 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=list(range(1,11))
    )

    post_q2 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=list(range(1,11))
    )    


def waiting_too_long(player):
    participant = player.participant
    import time
    # assumes you set wait_page_arrival in PARTICIPANT_FIELDS.
    return time.time() - participant.wait_page_arrival > 10*60


def group_by_arrival_time_method(subsession, waiting_players):
    # print('in group_by_arrival_time_method')
    observable_high_players = [p for p in waiting_players if p.participant.more_high_wage == True and p.participant.treatment == 1]
    observable_low_players = [p for p in waiting_players if p.participant.more_high_wage == False and p.participant.treatment == 1]
    unobservable_high_players = [p for p in waiting_players if p.participant.more_high_wage == True and p.participant.treatment == 2]
    unobservable_low_players = [p for p in waiting_players if p.participant.more_high_wage == False and p.participant.treatment == 2]

    if len(observable_high_players)>=2:
        return [observable_high_players[0], observable_high_players[1]]
    if len(observable_low_players)>=2:
        return [observable_low_players[0], observable_low_players[1]]
    if len(unobservable_high_players)>=2:
        return [unobservable_high_players[0], unobservable_high_players[1]]
    if len(unobservable_low_players)>=2:
        return [unobservable_low_players[0], unobservable_low_players[1]]   
    
    for player in waiting_players:
        if waiting_too_long(player):
            # make a single-player group.
            player.participant.single_group = True
            return [player]             

def set_payoffs(group):
    dictator = group.get_player_by_role(Constants.dictator_role)
    recipient = group.get_player_by_role(Constants.recipient_role)

    if group.treatment==1:
        decision_matrix = [group.yo_l_00, group.yo_l_01, group.yo_l_02, group.yo_l_03, group.yo_l_04, group.yo_l_05, group.yo_l_06, group.yo_l_07, group.yo_l_08, group.yo_l_09, group.yo_l_10,\
            group.yo_h_00, group.yo_h_01, group.yo_h_02, group.yo_h_03, group.yo_h_04, group.yo_h_05, group.yo_h_06, group.yo_h_07, group.yo_h_08, group.yo_h_09, group.yo_h_10]        
        for ind, info in Constants.yo_dic.items():
            if info['wage']==recipient.participant.wage and info['income']==recipient.participant.earning:
                matched_ind = ind
        transfer_income = decision_matrix[matched_ind]

    elif group.treatment==2:
        decision_matrix = [group.no_00, group.no_01, group.no_02, group.no_03, group.no_04, group.no_05, group.no_06, group.no_07, group.no_08, group.no_09, group.no_10, group.no_12, group.no_14, group.no_16, group.no_18, group.no_20]        
        for ind, info in Constants.no_dic.items():
            if info['income']==recipient.participant.earning:
                matched_ind = ind
        transfer_income = decision_matrix[matched_ind]
    
    group.final_transfer = transfer_income

    dictator.participant.payoff = dictator.participant.earning - transfer_income
    recipient.participant.payoff = recipient.participant.earning + transfer_income

# PAGES
class GroupPage(WaitPage):
    group_by_arrival_time = True
     
    title_text = "We are matching you with another participant."
    body_text = "Please wait..."  

    def after_all_players_arrive(group: Group):
        dictator = group.get_player_by_role(Constants.dictator_role)
        recipient = group.get_player_by_role(Constants.recipient_role)
        group.treatment = dictator.participant.treatment
        group.more_high_wage = dictator.participant.more_high_wage
        group.dictator_earning = dictator.participant.earning
        group.dictator_wage = dictator.participant.wage
        group.recipient_earning = recipient.participant.earning
        group.recipient_wage = recipient.participant.wage
        group.n_players = len(group.get_players())
        # for player in group.get_players():
        #     player.participant.is_dropout = False  
            

class Decision_instruction(Page):
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant

        if player.is_dropout:
            return 1  # instant timeout, 1 second
        else:
            return 1*60  
           

class Decision_roleA_yo(Page):
    form_model = 'group'
    form_fields = ['yo_l_00', 'yo_l_01', 'yo_l_02', 'yo_l_03', 'yo_l_04', 'yo_l_05', 'yo_l_06', 'yo_l_07', 'yo_l_08', 'yo_l_09', 'yo_l_10',\
        'yo_h_00', 'yo_h_01', 'yo_h_02', 'yo_h_03', 'yo_h_04', 'yo_h_05', 'yo_h_06', 'yo_h_07', 'yo_h_08', 'yo_h_09', 'yo_h_10']
    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role and player.group.treatment == 1
    @staticmethod
    def get_timeout_seconds(player):
        # participant = player.participant
        if player.is_dropout:
            return 1  # instant timeout, 1 second
        else:
            return 10*60   
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        earning = participant.earning
        return dict(
            earning=earning,
        )                    
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            choice_set = random.choice([round(i,1) for i in list(numpy.arange (0, player.participant.earning+0.1, 0.1))])
            player.yo_l_00 = random.choice(choice_set)
            player.yo_l_01 = random.choice(choice_set)
            player.yo_l_02 = random.choice(choice_set)
            player.yo_l_03 = random.choice(choice_set)
            player.yo_l_04 = random.choice(choice_set)
            player.yo_l_05 = random.choice(choice_set)
            player.yo_l_06 = random.choice(choice_set)
            player.yo_l_07 = random.choice(choice_set)
            player.yo_l_08 = random.choice(choice_set)
            player.yo_l_09 = random.choice(choice_set)
            player.yo_l_10 = random.choice(choice_set)
            player.yo_h_00 = random.choice(choice_set)
            player.yo_h_01 = random.choice(choice_set)
            player.yo_h_02 = random.choice(choice_set)
            player.yo_h_03 = random.choice(choice_set)
            player.yo_h_04 = random.choice(choice_set)
            player.yo_h_05 = random.choice(choice_set)
            player.yo_h_06 = random.choice(choice_set)
            player.yo_h_07 = random.choice(choice_set)
            player.yo_h_08 = random.choice(choice_set)
            player.yo_h_09 = random.choice(choice_set)
            player.yo_h_10 = random.choice(choice_set)
            if player.is_dropout == False:
                player.dropout_page = 'Decision'
                player.is_dropout = True      

class Decision_roleB_yo(Page):
    form_model = 'group'
    form_fields = ['g_yo_l_00', 'g_yo_l_01', 'g_yo_l_02', 'g_yo_l_03', 'g_yo_l_04', 'g_yo_l_05', 'g_yo_l_06', 'g_yo_l_07', 'g_yo_l_08', 'g_yo_l_09', 'g_yo_l_10',\
        'g_yo_h_00', 'g_yo_h_01', 'g_yo_h_02', 'g_yo_h_03', 'g_yo_h_04', 'g_yo_h_05', 'g_yo_h_06', 'g_yo_h_07', 'g_yo_h_08', 'g_yo_h_09', 'g_yo_h_10']
    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role  and player.group.treatment == 1
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant

        if player.is_dropout:
            return 1  # instant timeout, 1 second
        else:
            return 10*60          
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            if player.is_dropout == False:
                player.dropout_page = 'Decision'
                player.is_dropout = True              

class Decision_roleA_no(Page):
    form_model = 'group'
    form_fields = ['no_00','no_01','no_02','no_03','no_04','no_05','no_06','no_07','no_08','no_09','no_10','no_12','no_14','no_16','no_18','no_20']
    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.dictator_role and player.group.treatment == 2
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant

        if player.is_dropout:
            return 1  # instant timeout, 1 second
        else:
            return 10*60    
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        earning = participant.earning
        return dict(
            earning=earning,
        )                    
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            choice_set = random.choice([round(i,1) for i in list(numpy.arange (0, player.participant.earning+0.1, 0.1))])
            player.no_00 = random.choice(choice_set)
            player.no_01 = random.choice(choice_set)
            player.no_02 = random.choice(choice_set)
            player.no_03 = random.choice(choice_set)
            player.no_04 = random.choice(choice_set)
            player.no_05 = random.choice(choice_set)
            player.no_06 = random.choice(choice_set)
            player.no_07 = random.choice(choice_set)
            player.no_08 = random.choice(choice_set)
            player.no_09 = random.choice(choice_set)
            player.no_10 = random.choice(choice_set)
            player.no_12 = random.choice(choice_set)
            player.no_14 = random.choice(choice_set)
            player.no_16 = random.choice(choice_set)
            player.no_18 = random.choice(choice_set)
            player.no_20 = random.choice(choice_set)
            if player.is_dropout == False:
                player.dropout_page = 'Decision'
                player.is_dropout = True             

class Decision_roleB_no(Page):
    form_model = 'group'
    form_fields = ['g_no_00','g_no_01','g_no_02','g_no_03','g_no_04','g_no_05','g_no_06','g_no_07','g_no_08','g_no_09','g_no_10','g_no_12','g_no_14','g_no_16','g_no_18','g_no_20']
    @staticmethod
    def is_displayed(player: Player):
        return player.role == Constants.recipient_role  and player.group.treatment == 2  
    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant

        if player.is_dropout:
            return 1  # instant timeout, 1 second
        else:
            return 10*60          
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            if player.is_dropout == False:
                player.dropout_page = 'Decision'
                player.is_dropout = True                     

class Wait_for_decision(WaitPage):
    title_text = "Your partner is making theie decision"
    body_text = "Thank you for your patient."     
    
    after_all_players_arrive = 'set_payoffs'

class Belief(Page):
    form_model = 'player'
    form_fields = ['believe_income_00','believe_income_01','believe_income_02','believe_income_03','believe_income_04','believe_income_05','believe_income_06','believe_income_07','believe_income_08','believe_income_09','believe_income_10','believe_income_12','believe_income_14','believe_income_16','believe_income_18','believe_income_20']

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant

        if player.is_dropout:
            return 1  # instant timeout, 1 second
        else:
            return 10*60          
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            if player.is_dropout == False:
                player.dropout_page = 'Belief'
                player.is_dropout = True   

class Post_survey(Page):
    form_model = 'player'
    form_fields = ['post_q1','post_q2']

    @staticmethod
    def get_timeout_seconds(player):
        participant = player.participant

        if player.is_dropout:
            return 1  # instant timeout, 1 second
        else:
            return 5*60          
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            if player.is_dropout == False:
                player.dropout_page = 'Post_survey'
                player.is_dropout = True           
    
class Results(Page):
    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        payoff_real_cu = participant.payoff
        total_earning = participant.payoff_plus_participation_fee()
        return dict(
            payoff_real_cu=payoff_real_cu,
            total_earning=total_earning,
        )        


page_sequence = [GroupPage, Decision_instruction, Decision_roleA_yo, Decision_roleB_yo, Decision_roleA_no, Decision_roleB_no, Wait_for_decision, Belief, Post_survey, Results]
