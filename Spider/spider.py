'''7) THE SPIDER WORKS AS FOLLOWS:
AT SOME POINT WE'LL HAVE A LIST OF LINKS IN THE QUEUE.TXT FILE.
THE SPIDER WILL GO AHEAD AND GRAB ONE OF THOSE LINKS, CONNECT TO THE PAGE,
GRAB THE HTML (CRAWL), AND THROW IT INTO LINK_FINDER.PY.  THEN, IT WILL PUT
THE LINK INTO THE CRAWLED.TXT FILE SO THAT WE DON'T CRAWL THE SAME PAGE TWICE

CALLING SPIDERS BY THEMSELVES WOULD CAUSE EACH TO HAVE THEIR OWN QUEUE
AND CRAWLED LISTS, AND NO ACCESS TO ALL THE OTHER SPIDERS' CRAWLED FILES.
SPIDERS WOULD NEEDLESSLY CRAWL A PREVIOUSLY CRAWLED PAGE AND WASTE TIME.
WE'LL SET IT UP SO THAT THERE CAN BE MULTIPLE SPIDERS THAT SHARE A SINGLE
QUEUE FILE VARIABLE AND SINGLE CRAWLED FILE VARIABLE.'''

from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

# 8) THE SPIDER CLASS OBJECT
class Spider:

    # CLASS VARIABLES THAT ARE SHARED AMONG ALL INSTANCES (ALL SPIDERS)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    # WE DON'T WANT TO WRITE TO A FILE EVERY TIME WE COME ACROSS A LINK.  THAT
    # WOULD BE PAINFULLY SLOW.  INSTEAD, WE'LL USE VARIABLES (A SET TYPE) AS
    # WELL.  SETS ARE STORED IN THE MEMORY, WHICH IS FASTER
    queue_set = set()
    crawled_set = set()

# 9) GIVING THE SPIDER INFORMATION:
# THIS IS A SINGLE SPIDER INSTANCE THE CODE TELLS IT WHAT TO DO.
# FOR EACH SPIDER, THE USER WILL GIVE IT SOME INFORMATION SO IT KNOWS WHAT
# PAGE IT'S SUPPOSED TO BE CRAWLING AND WHAT PROJECT IT'S WORKING ON, ETC
    def __init__(self, projet_name, base_url, domain_name):

        # ALL SPIDERS WILL HAVE THIS INFORMATION (1 OR 100 OR 1000 SPIDERS)
        Spider.project_name = projet_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'  # TIME SAVER
        Spider.crawled_file = Spider.project_name + '/crawled.txt'  # TIME SAVER

        '''WHEN A SPIDER IS CREATED (BOOTED), WE ONLY NEED TO START WITH ONE 
        BECAUSE IT ONLY HAS ONE WEB PAGE (THE HOME PAGE), AND IT WOULD BE 
        POINTLESS TO IMMEDIATELY BEGIN WITH MULTIPLE SPIDERS.  AS THE FIRST, 
        SINGLE SPIDER GATHERS MORE WEB PAGES, WE 'THREAD' THE PROCESS BY 
        CALLING MORE AND MORE SPIDERS TO HELP'''

        #  THESE METHODS GIVE OUR FIRST SPIDER UNIQUE TASKS
        self.boot()  # CREATES THE PROJECT FOLDER, QUEUE FILE, CRAWLED FILE, ETC
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)  # ADDS HOME PAGE TO FILE
        Spider.queue = read_file_to_set(Spider.queue_file)  # NEW SPIDER GETS UPDATED QUEUE AND CRAWLED FILES AND SAVES IT AS A SET
        Spider.crawled = read_file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled '+ str(len(
                Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    '''THIS FUNCTION WILL CONNECT TO A SITE, TAKES THE HTML, CONVERTS IT 
    TO A PROPER HTML FORMAT STRING, SENDS IT TO LINK_FINDER, LINK_FINDER 
    PARSES THROUGH IT, GETS A SET OF ALL OF THE LINKS ON IT (URL'S), 
    AND AS LONG AS THERE ARE NO ISSUES, IT RETURNS A SET OF LINKS TO THE SPIDER 
    '''
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            return set()  #IT NEEDS SOMETHING RETURNED, SO WE JUST RETURN EMPTY
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            # CHECK THAT THEY AREN'T IN THE QUEUE/CRAWL
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            # WE DONT WANT TO CRAWL THE ENTIRE INTERNET (YOUTUBE, FACEBOOK, ETC)
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    # THIS METHOD UPDATES THE FILES WITH THE DATA FROM THE SETS
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)




