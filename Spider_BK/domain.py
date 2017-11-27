# We created the Spider by followed the these tutorials
# Python Web Crawler Tutorial - 1 - Creating a New Project - https://www.youtube.com/watch?v=F2lbS-F0eTQ
# Python Web Crawler Tutorial - 2 - Queue and Crawled Files - https://www.youtube.com/watch?v=z_vIWoTZm2E
# Python Web Crawler Tutorial - 3 - Adding and Deleting Links - https://www.youtube.com/watch?v=pjkZCQTfneQ
# Python Web Crawler Tutorial - 4 - Speeding Up the Crawler - https://www.youtube.com/watch?v=jCBbxL4BGfU
# Python Web Crawler Tutorial - 5 - Parsing HTML - https://www.youtube.com/watch?v=F2lbS-F0eTQ
# Python Web Crawler Tutorial - 6 - Finding Links - https://www.youtube.com/watch?v=udBt0K7gwLc
# Python Web Crawler Tutorial - 7 - Spider Concept - https://www.youtube.com/watch?v=Eis9vu4XiNI
# Python Web Crawler Tutorial - 8 - Creating the Spider - https://www.youtube.com/watch?v=MpazNSqP4uo
# Python Web Crawler Tutorial - 9 - Giving the Spider Information - https://www.youtube.com/watch?v=QHWy0CXDBl4
# Python Web Crawler Tutorial - 10 - Booting Up the Spider - https://www.youtube.com/watch?v=uTdweD5SCag
# Python Web Crawler Tutorial - 11 - Crawling Pages - https://www.youtube.com/watch?v=luYg1qMVSfY
# Python Web Crawler Tutorial - 12 - Gathering Links - https://www.youtube.com/watch?v=XHIlke_0WnM
# Python Web Crawler Tutorial - 13 - Adding Links to the Queue - https://www.youtube.com/watch?v=rxGUiLcW0cI
# Python Web Crawler Tutorial - 14 - Domain Name Parsing - https://www.youtube.com/watch?v=PPonGS2RZNc
# Python Web Crawler Tutorial - 15 - The First Spider - https://www.youtube.com/watch?v=vKFc3-5Y17U
# Python Web Crawler Tutorial - 16 - Creating Jobs - https://www.youtube.com/watch?v=zfBhpmhXUqM
# Python Web Crawler Tutorial - 17 - Running the Final Program - https://www.youtube.com/watch?v=ciwWSedS1XY&t=331s

from urllib.parse import urlparse

# Return domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    except Exception as e:
        print(e)
        return ''

# Return a sub domain of the url given
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except  Exception as e:
        print(e)
        return ''
