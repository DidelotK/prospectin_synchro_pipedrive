from utils.conf import PROSPECTIN_CURRENT_CAMPAIN
from utils.pipedrive.api import get_pipedrive_persons
from utils.pipedrive.keltio import get_linkedin_personfield
from utils.prospectin.api import (
  prospectin_get_campaign,
  prospectin_create_prospect,
)
from utils.utils import bcolors


def add_all_persons_with_linkedin_in_prospectin():
  # 1. Get all persons in pipedrive
  persons = get_pipedrive_persons()
  linkedin_personfield = get_linkedin_personfield() 
  current_campaign = prospectin_get_campaign(name=PROSPECTIN_CURRENT_CAMPAIN)

  # For each person
  for person in persons:
  # 1. Check if person has a linkedin url
    linkedin_url = person[linkedin_personfield['key']]
    if not linkedin_url:
  #   If no: CONTINUE TO NEXT PERSON
      print(bcolors.WARNING + '    [NO ACTION] No linkedin found for {}: so no action to do in prospectin'.format(person['name']) + bcolors.ENDC)
      continue
  #   Else: continue to next step

  # 2. Import all persons in the current prospectin campain if there are not in the crm
    result = prospectin_create_prospect(current_campaign['_id'], linkedin_url)
    if 'message' in result and result['message'] == 'prospect_duplicated':
      print(bcolors.WARNING + '    [NO ACTION] Person {} already in prospectin'.format(person['name']) + bcolors.ENDC)
    else:
      print(bcolors.OKGREEN + '    [ADD PERSON] Add {} in campaign {}'.format(person['name'], current_campaign['name']) + bcolors.ENDC)
