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

from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
import ssl
import requests
from bs4 import BeautifulSoup

class Spider:

    # Definition of C (This will be shared amoung all instances)
    project_name = ''
    url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    # Constructor of the Spider
    # @param project - Project Name
    # @param url - Top page of the website you want to crawl
    # @param domain - Domain of the website you want tp crawl
    def __init__(self, project, url, domain):
        # Spider
        Spider.project_name = project
        Spider.url = url
        Spider.domain_name = domain
        Spider.queue_file = Spider.project_name + "/" + Spider.project_name + "_queue_url.txt"
        Spider.crawled_file = Spider.project_name + "/" + Spider.project_name + "_crawled_url.txt"
        self.boot()
        self.crawl_page('First Spider', Spider.url)

    # This will prepared the project environment
    @staticmethod
    def boot():
        # Create Project Directory
        create_proj_directory(Spider.project_name)
        # Craete files for the project
        create_data_file(Spider.project_name, Spider.url)
        # Convert the QUEUED file's content into QUEUE's set
        Spider.queue = convert_to_set(Spider.queue_file)
        # Convert the CRAWLED file's content into CRAWLED's set
        Spider.crawled = convert_to_set(Spider.crawled_file)

    # crawl_page method
    # Crawl the page and gather all links of the page givem
    # @param thread_name - Name of the Spider
    # @param page_url - The page which spider will crawl
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            result = Spider.gather_links(page_url)
            if not result == None:
                Spider.add_links_to_queue(result)
                Spider.queue.remove(page_url)
                Spider.crawled.add(page_url)
                Spider.update_files()
                return None
            else:
                print("FOUND")
                return "FOUND"

    # Check the title of the page.
    # This will serve as a signal tro tell spider that the page crawling is the target or not
    # This method will parse the html and extract the title of the page
    # @param page_url
    @staticmethod
    def check_title(page_url):
        source = requests.get(page_url)
        plain_text = source.text
        soup = BeautifulSoup(plain_text, "lxml")
        if (not soup == None) and (not soup.title == None):
            if '牌告匯率' in soup.title.string:
                return True
        return False


    # Get links from the page given
    # @param page_url - target page
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        if Spider.check_title(page_url):
            return None
        else:
            try:
                context = ssl._create_unverified_context()
                response = urlopen(page_url, context=context)
                if response.getheader('Content-Type') == 'text/html'or\
                    response.getheader('Content-Type') == 'text/html; charset=utf-8':

                    html_bytes = response.read();
                    # Might be here to decide if the spider will stop or not
                    html_string = html_bytes.decode('utf-8')
                finder = LinkFinder(Spider.url, page_url)
                finder.feed(html_string)
            except Exception as e:
                print("gather_links: ")
                print(e)
                print('Error: Cannot crawled the page given. URL: ' + page_url)
                return set()

            return finder.page_links()

    # Add the url to queue file
    # This method will check first of the link is already crawled or already in the queue.
    # If not, then it will added to the queue
    # @param links - the url which will be added to queue file
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            # Checked whether the url is in the queue or not
            if url in Spider.queue:
                continue
            # Check whether the url is in the crawled or not
            if url in Spider.crawled:
                continue
            # Check
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    # Update file method
    @staticmethod
    def update_files():
        convert_set_to_file(Spider.queue, Spider.queue_file)
        convert_set_to_file(Spider.crawled, Spider.crawled_file)


