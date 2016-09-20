__author__ = 'Bradley'

## OECD RESTful API
OECD_ROOT_URL = "http://stats.oecd.org/sdmx-json/data"

def make_OECD_request(dsname, dimensions, params=None, root_dir=OECD_ROOT_URL):
    if not params:
        params = {}

    dim_args = ['+'.join(d) for d in dimensions]
    dim_str = '.'.join(dim_args)

    url = root_dir + '/' + dsname + '/' +dim_str + '/all'

    print('Requestiong URL: ' + url)
    return requests.get(url, params=params)

response = make_OECD_request('QNA', (('USA', 'AUS'), ('GDP', 'B1_GE'), ('CUR', 'VOBARSA'), ('Q')), {'startTime':'2009-Q1', 'endTime':'2010-Q1'})

if response.status_code == 200:
    json = response.json()
    json.keys()

## REST countries API

REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"

def REST_country_request(field='all', name=None, params=None):

    headers={'User-Agent': 'Mozilla/5.0'}

    if not params:
        params = {}

    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')

    url = '%s/%s/%s'%(REST_EU_ROOT_URL, field, name)
    print('Requesting URL: ' + url)
    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception('Request failed with status code ' + str(response.status_code))

    return response

response = REST_country_request('currency', 'usd')

response.json()

db_nobel = get_mongo_database('nobel_prize')
col = db_nobel['country_data']

response = REST_country_request()
country_data = response.json()
col.insert(country_data)

res = col.find({'currencies':{'$in':['USD']}})
list(res)