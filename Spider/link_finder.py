'''5) HERE, WE PARSE THE HTML (Hypertext Markup Language).
HTML IS THE STANDARD LANGUAGE FOR CREATING WEB PAGES AND WEB APPS.  THE
PAGES AND APPS ARE FANCY DOCUMENTS MADE OF HTML CODE.

THE SPIDER NEEDS LINKS TO PROGRESS.  THIS MODULE CONTAINS A CLASS OBJECT CALLED
LINK_FINDER THAT LOOKS AT THE HTML SENT FROM SPIDER.PY, SIFTS THROUGH IT
(PARSES),AND FINDS ALL OF THE LINKS.  LUCKILY FOR US, PYTHON ALREADY COMES
WITH ITS OWN CLASS CALLED 'HTML PARSER' AND DOES 90% OF THE WORK FOR US'''

from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):  #BASE/PAGE_URL REPRESENT FULL URL
        super().__init__()
        self.base_url = base_url
        self.page_url = base_url
        self.links = set()  #STORES THE LINKS IN A SET (NO REPEATS, UNORDERED)


    def handle_starttag(self, tag, attrs):
        if tag == 'a':  # IF WE FIND A LINK...(a IS AN HTML TAG)
            for (attribute, value) in attrs:  #ATTRIBUTES -> 'HREF' OR 'CLASS', VALUE -> 'URL ADDRESS' OR 'USER-NAME'
                if attribute == 'href':  # ...AND WE FIND THE HREF ATTRUBUTE...
                    url = parse.urljoin(self. base_url, value)  # ...WE JOIN
                    #  THE HOME BASE URL AND RELATIVE URL TOGETHER TO GET THE
                    # PROPERLY FORMATTED, FULL URL.  IF IT'S FULL ALREADY,
                    # THEN WE JUST LEAVE IT ALONE
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass




