from utils.conf import (
  PIPEDRIVE_LINKEDIN_PERSONFIELD_NAME
)
from utils.pipedrive.api import (
    get_pipedrive_personfields
)


def get_linkedin_personfield():
    personfields = get_pipedrive_personfields()
    linkedin_personfield = None
    for personfield in personfields:
        if personfield['name'] == PIPEDRIVE_LINKEDIN_PERSONFIELD_NAME:
            return personfield

    raise Exception('Cannot find linkedin personfield')
