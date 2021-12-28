from os import environ

SESSION_CONFIGS = [
    dict(
        name='Observable',
        app_sequence=['welcome_and_consent_form','pre_questionnaire','comprehension_check','real_effort_task','decision','end'],
        more_high_wage=True,
        treatment=1,
        num_demo_participants=2,
    ),   
    dict(
        name='Unobservable',
        app_sequence=['welcome_and_consent_form','pre_questionnaire','comprehension_check','real_effort_task','decision','end'],
        more_high_wage=True,
        treatment=2,
        num_demo_participants=2,
    ),         
    dict(
        name='randomization',
        app_sequence=['welcome_and_consent_form','pre_questionnaire','comprehension_check','real_effort_task','decision','end'],
        num_demo_participants=2,
    ),
    
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.50, doc="",
)

PARTICIPANT_FIELDS = ['tax_status','consent','more_high_wage','treatment','wage','earning','wait_page_arrival','n_players','is_dropout','dropout_page']
SESSION_FIELDS = ['low_wage_rate','high_wage_rate']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4560738317729'
