The five modules in this folder are my web crawler.  I used tutorials from the internet, particularly TheNewBoston, to 
help me write a basic web crawler program.  The only system needed to run this program is Python 3.6

All of the code is very well commented.

The five .py modules consist of:

1) main.py - Run the main web crawler from this module.  It utilizes the other modules in the same project folder.  
   There is a website already hardcoded in side the module.  Simply run to test.  In the module, the spider object is 
   called over and over again.  If there are links available, it keeps going.  It runs on multiple threads and multiple 
   spiders will work at the same time.  I have set the limit to 8 spiders
 
2) general.py - This module contains basic functions that do simple tasks. Tasks like read/write info into a file, create a 
   folder for a web crawl project,    append data to text files, etc.  It makes a file of web sites waiting to be 
   crawled ('queue') and sites that have previously been crawled ('crawled')
   
3) domain.py - This module contains two functions that will extract a domain name (like .com, .gov, .edu, etc...)
   so that it doesn't crawl the entire internet.
   
4) link_finder.py - is an object that takes the HTML sent to it from the spider object, parses through the HTML, 
   and finds all the links.

5) spider.py - This was my favorite module.  spider.py is an object class.  The spider object grabs a link from the queue 
   file, connects to the page, crawls it (grabs the HTML), and hands it over to the link_finder object.  Finally, it takes 
   the link it just crawled, deletes it from the 'queue' file, and adds it to the 'crawled' file.
