URL_PREFIX = 'api'
MONGO_DBNAME = 'nobel_prize'
DOMAIN = {'winners_full': {
    'item_title': 'winners',
    'schema': {
        'country': {'type': 'string'},
        'category': {'type': 'string'},
        'name': {'type': 'string'},
        'year': {'type': 'integer'},
        'gender': {'type': 'string'},
        'mini_bio': {'type': 'string'},
        'bio_image': {'type': 'string'}
    },
    'url': 'winners'
}}

X_DOMAINS = 'http://localhost:8080'
HATEOS = False
PAGINATION = False