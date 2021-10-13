from otree.api import Currency as c, currency_range, expect, Bot
from . import *

class PlayerBot(Bot):
    def play_round(self):
        yield Page1, dict(gender=0,year_of_birth=1992,household_income=60000,education=6,pid0=0)
        yield Page2, dict(pid0others='')
        yield Page3, dict(pid1=0)
        yield Page4, dict(pid6=1)
        yield Page5, dict(ideo=4)