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
import os
import sys

# Create a directory to hold project's data
def create_proj_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Project directory \'" + directory + "\' created.")
    except Exception as e:
        print("create_proj_directory: ")
        print(e)
        # Print if there is error message
        print(sys.exc_info()[0])

# Create file to hold queued and crawled data
def create_data_file(project, url):
    # Define file name
    queued = project + "/" + project + '_queue_url.txt';
    crawled = project + "/" + project + "_crawled_url.txt"
    # Check whether the file is exist or not
    if not os.path.isfile(queued):
        create_file(queued, url)
        print('File \'' + queued + "\' created.")
    # Check whether the file is exist or not
    if not os.path.isfile(crawled):
        create_file(crawled, '')
        print('File \'' + crawled + "\' created.")

# create file and write the data given
def create_file(file, data):
    try:
        # Open file with Write Mode
        handle = open(file, 'w')
        # Write the data into file
        handle.writelines(data)
    except Exception as e:
        print("create_file: ")
        print(e)
        # Printout if there is any error
        print(sys.exc_info()[0])
    else:
        # Closed the file
        handle.close()

# Write Data into an existing file
def append_to_file(file, data):
    try:
        handle = open(file, 'a')
        handle.write(data + '\n')
    except Exception as e:
        print("append_to_file: ")
        print(e)
        print(sys.exc_info()[0])
    finally:
        handle.close()

# Delete first line of the data
def delete_data_from_file(file):
    open(file, 'w').close()
    #try:
    #    handle = open(file, 'w')
    #    pass
    #    #Do Nothing
    #except  Exception as e:
    #    print("delete_data_from_file: ")
    #    print(e)
    #    print(sys.exc_info()[0])
    #else:
    #    handle.close()

# Read File and convert each line to set item
def convert_to_set(file):
    result_set = set()
    try:
        # Open file with Read Mode
        handle = open(file, 'r')
        # Reaf the data and write to a set
        for line in handle:
            result_set.add(line.rstrip())
    except  Exception as e:
        print("convert_to_set: ")
        print(e)
        # Printout if there is any error
        print("Convert to set: ")
        print(sys.exc_info()[0])
    else:
        # Closed the file
        handle.close()
    return result_set

# Iterate through a set.  Each item will be a new line in the file
def convert_set_to_file(links, file):
    # Delete File's content
    for link in links:
        append_to_file(file, link)
