import requests
from utils.conf import PROSPECTIN_API_TOKEN
from utils.clean_data import get_linkedin_url_id_from_linkedin_url


def prospectin_get_campaigns():
  headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'x-client-version': 'x.x.x',
    'Authorization': 'Bearer {}'.format(PROSPECTIN_API_TOKEN),
    'Origin': 'https://app.prospectin.fr',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://app.prospectin.fr/',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
  }

  response = requests.get('https://prospectin-api.herokuapp.com/api/campaigns', headers=headers)

  return response.json()


def prospectin_create_prospect(campaign_id, linkedin_url):
  linkedin_url_id = get_linkedin_url_id_from_linkedin_url(linkedin_url)

  headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': 'Bearer {}'.format(PROSPECTIN_API_TOKEN),
    'x-client-version': '1.6.15',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'chrome-extension://ohmpcdmgbjhkhnljkaeeahndchboiici',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
  }

  json = {
    "prospect": {
      "publicIdentifier": linkedin_url_id,
      "state": "unknown"
    },
    "shouldNotOverride": False
  }

  response = requests.post('https://prospectin-api.herokuapp.com/api/campaigns/{}/prospects'.format(campaign_id), headers=headers, json=json)

  return response.json()


def prospectin_get_campaign(name):
  prospectin_campaigns = prospectin_get_campaigns()
  current_campaign = None
  for campaign in prospectin_campaigns:
    if campaign['name'] == name:
      return campaign

  raise Exception('Campaign does not exist')
