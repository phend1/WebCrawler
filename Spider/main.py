# IN THIS MAIN() MODULE, THE SPIDER IS CALLED OVER AND OVER AGAIN.  WHILE
# THERE ARE LINKS AVAILABLE, KEEP GOING.  THE PROGRAM WILL BE RUN
# ON MULTIPLE THREADS AND MULTIPLE SPIDERS WILL WORK AT THE SAME
# TIME

import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'thenewboston'  # THE PROGRAM WILL PROMPT A USER TO ENTER THIS
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)  # CALLS THE FIRST, SPECIAL SPIDER


# CREATE THE SPIDERS, AKA WORKER THREADS (THEY WILL DIE WHEN MAIN EXITS)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# DO THE NEXT JOB IN THE QUEUE
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# EACH QUEUED LINK IS A NEW JOB
def create_jobs():
    for link in read_file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# CHECKS FOR ITEMS IN THE QUEUE.  IF SO, THEN CRAWL THEM
def crawl():
    queued_links = read_file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()

