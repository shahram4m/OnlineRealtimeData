import requests
import validators

def ValidatUrl(url):
    print(url)
    if validators.url(url):
        print('valid url')
        headers = requests.head(url, allow_redirects=True).headers
        content_type = headers.get('content-type')
        print(content_type)
        if 'csv' in content_type.lower():
            return True
    else:
        return False
