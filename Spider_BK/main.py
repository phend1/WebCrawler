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

import threading
from queue import Queue
from domain import *
from general import *
from Spider import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/' + PROJECT_NAME +  '_queue_url.txt'
CRAWLED_FILE = PROJECT_NAME + '/' + PROJECT_NAME +  '_crawled_url.txt'
NUMBER_OF_THREADS = 8 # There are a lot of factors for this one
thread_queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create Worker Threads
# Threads will die when main exit
def create_spiders():
    # just loop 8 time, using _ to disregards the values
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=crawl)
        thread.daemon = True
        thread.start()

# Execute next in the queue
def crawl():
    while True:
        url = thread_queue.get()
        result = Spider.crawl_page(threading.current_thread().name, url)
        thread_queue.task_done()
        if not result == None and result == "FOUND":
            print("FOUND: " + url)
            break;


# Each link is a new job
def create_spider_jobs():
    for link in convert_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl_page()

# Check if there are link in a queue wait to craw or not
def crawl_page():
    queued_links = convert_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue waiting to craw.')
        create_spider_jobs()
    else:
        print("Nothing on the QUEUE for crawl.")


create_spiders()
crawl_page()
