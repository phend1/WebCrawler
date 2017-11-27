'''EXTRACT A DOMAIN NAME (.MAIL,.COM,.GOV, .EDU, ETC)SO THAT WE DON'T
ACCIDENTALLY START CRAWLING THE ENTIRE INTERNET'''

from urllib.parse import urlparse

# GET DOMAIN NAME (RETURNS:  EXAMPLE.WHATEVER)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# GET SUB DOMAIN NAME (NAME.EXAMPLE.WHATEVER)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

print(get_sub_domain_name('http://thenewboston.com/index.php'))
