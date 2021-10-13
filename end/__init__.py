from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'end'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class end_page(Page):
    pass



page_sequence = [end_page]
