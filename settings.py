from os import environ

SESSION_CONFIGS = [
    dict(
        name='deservingness_observable',
        app_sequence=['welcome_and_consent_form','pre_questionnaire','comprehension_check','real_effort_task','decision','end'],
        num_demo_participants=2,
        more_high_wage = True,
        treatment = 1,
        # use_browser_bots=True
    ),
    dict(
        name='deservingness_unobservable',
        app_sequence=['welcome_and_consent_form','pre_questionnaire','comprehension_check','real_effort_task','decision','end'],
        num_demo_participants=2,
        more_high_wage = True,
        treatment = 2,
        # use_browser_bots=True
    ),    
    
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.50, doc="",
    mturk_hit_settings=dict(
    keywords='bonus, study',
    title='Decision-making and effort',
    description='Participate in an experimental research study that involves a group interaction. You could earn $0.5 show-up fee. Bonus payments will be available and will depend on what happens during the study!',
    frame_height=500,
    template='global/mturk_template.html',
    minutes_allotted_per_assignment=60,
    expiration_hours=7 * 24,
    qualification_requirements=[]
    # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
),
)

PARTICIPANT_FIELDS = ['tax_status','consent','more_high_wage','treatment','wage','earning','wait_page_arrival','n_players','is_dropout','dropout_page']
SESSION_FIELDS = []

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
