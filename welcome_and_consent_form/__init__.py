from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'welcome_and_consent_form'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tax_status = models.BooleanField()
    consent = models.BooleanField()


# PAGES
class Welcome(Page):
    pass

class Consent_form(Page):
    form_model = 'player'
    form_fields = ['tax_status','consent']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        # add 'tax_status' and 'consent' to PARTICIPANT_FIELDS in setting.py
        participant.tax_status = player.tax_status    
        participant.consent = player.consent    

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if player.consent==False:
            return 'end'        

page_sequence = [Welcome, Consent_form]
