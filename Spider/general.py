'''WEB CRAWLING IS THE ACT OF AUTOMATICALLY DOWNLOADING A WEB PAGE'S DATA
AND EXTRACTING VERY SPECIFIC INFORMATION FROM IT.  THE EXTRACTED
INFORMATION CAN BE STORED PRETTY MUCH ANYWHERE (DATABASE, FILE, ETC).

THIS MODULE CONTAINS GENERAL FUNCTIONS THAT:
-CREATE A PROJECT DIRECTORY
-CREATE A WAITING/DONE LIST OF WEB ADDRESSES (URL LINKS)
-WRITE DATA TO A FILE
-APPEND DATA TO A FILE
-DELETE DATA FROM A FILE
-READ EACH LINE OF A FILE AND CONVERT EACH LINE TO A SET{} OF ITEMS
-ITERATE THROUGH A SET AND EACH ITEM WILL BE A NEW LINE IN A FILE'''

import os

# 1) CREATE A SEPARATE PROJECT (DIRECTORY FOLDER) FOR EACH WEBSITE CRAWLED
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)

# 2) CREATE QUEUE AND CRAWLED FILES (URL LINKS)
# IT WILL CHECK FOR FILES THAT ALREADY EXIST (SO THAT WE DON'T WASTE TIME)
# TO GO EVEN FASTER, WE'LL THREAD THE PROCESS AND CRAWL 8-16 PAGES AT A TIME
def create_data_files(project_name, base_url):  # EVERY TIME A LINK IS FOUND
    queue = project_name + '/queue.txt'  # ...IT ADDS IT TO THE QUEUE LIST
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):  # IF THE URL IS NOT IN THE QUEUE LIST...
        write_file(queue, base_url)  # ...WRITE IT TO THE LIST USING OUR FUNC
    if not os.path.isfile(crawled):  # IF THE URL HASN'T BEEN CRAWLED...
        write_file(crawled, '')  # ...WRITE IT TO THE LIST USING OUR FUNCTION

# CREATES/OPENS AND WRITES WHATEVER TO A NEW FILE
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# 3) ADDING AND DELETING LINKS
#create_project_dir('thenewboston')
#create_data_files('thenewboston', 'http://thenewboston.com/')

# ADD DATA ONTO AN EXISTING TEXT FILE
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# DELETE DATA ON A FILE (ACTUALLY JUST RECREATES AN EMPTY FILE)
def delete_file_content(path):
    with open(path, 'w'):
        pass  # KEYWORD THAT MEANS 'DO NOTHING

'''4) WE SPEED UP THE CRAWLER BY STORING EACH LINE IN A SET (UNIQUE, UNORDERED 
ELEMENTS) AND PERIODICALLY, WE'LL SAVE IT TO THE FILE.  THIS WAY, WE GET THE 
SPEED OF USING VARIABLES, BUT THE SAFETY OF 'BACKING UP' THE DATA AS WE CRAWL'''

# READ A FILE AND CONVERT EACH LINE TO A SET OF ITEMS
def read_file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))  #REPLACES \N WITH NOTHING
    return results


# ITERATE THROUGH A SET, EACH ITEM WILL BE A NEW LINE IN THE FILE
def set_to_file(links, file):
    delete_file_content(file)  # DELETE OLD FILE FOR TO MAKE WAY FOR NEW LINKS
    for link in sorted(links):  # FOR EACH LINK IN THE ALPHABETIZED LINKS...
        append_to_file(file, link)







