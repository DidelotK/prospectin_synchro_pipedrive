import requests
from datetime import datetime
from utils.conf import PIPEDRIVE_COMPANE_NAME, PIPEDRIVE_API_TOKEN


def get_pipedrive_personfields():
    personfields_url = 'https://{}.pipedrive.com/api/v1/personFields?api_token={}&limit=500'.format(
        PIPEDRIVE_COMPANE_NAME, PIPEDRIVE_API_TOKEN)

    res = requests.get(personfields_url)

    return res.json()['data']

def get_pipedrive_persons():
    persons = []
    should_search_for_persons = True
    start = 0
    limit = 500
    while should_search_for_persons == True:
      person_url = 'https://{}.pipedrive.com/api/v1/persons?start={}&status=open&limit={}&api_token={}'.format(
        PIPEDRIVE_COMPANE_NAME,
        start,
        limit,
        PIPEDRIVE_API_TOKEN
      )

      res = requests.get(person_url)
      new_persons = res.json()['data']

      if not new_persons:
        should_search_for_persons = False
      else:
        persons += new_persons
        start += limit

    return persons
