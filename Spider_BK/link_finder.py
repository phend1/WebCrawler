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

from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    # Constructor for LinkFinder Class
    def __init__(self, url, page):
        super().__init__()
        # Variable initialization
        self.base_url = url
        self.page_url = page
        self.links = set()

    # Handled the start tag of html
    # This will define the tag we are looking for.  In this case, we are looking an 'a' tag
    def handle_starttag(self, tag, attrs):
        # Check whether the tag is <a> or not
        if tag == 'a':
            # Loop each attributes in the tag
            for (attibute, value)  in attrs:
                # Check if the attribute is 'hfre' or not
                if attibute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)


    def page_links(self):
        return self.links

    def error(self, message):
        pass
