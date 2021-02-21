def get_linkedin_url_id_from_linkedin_url(linkedin_url):
    if 'http' in linkedin_url:
        full_linkedin_url = linkedin_url
    else:
        full_linkedin_url = 'https://{}'.format(linkedin_url)

    return full_linkedin_url.replace('https://www.linkedin.com/in/', '').replace('http://www.linkedin.com/in/', '')
