#!/usr/bin/python

import pandas
import requests
import logging
import math
import os
import sqlite3
import time

# Main Class for currecy crawler
class currency_crawler:
    # Variables which stored the website where we can get the data
    bank_website = {'BOT':'http://rate.bot.com.tw/xrt?Lang=zh-TW',
                    'CHINATRUST':'https://www.ctbcbank.com/CTCBPortalWeb/toPage;EBANKSID=3vyrT5KhHp1y9Gh2WhQ6XmR2ZvnRhhnTP7JsQPJTZH5TJhGWgLyT!-457167339?id=TW_RB_CM_ebank_018001',
                    'ESUN':'https://www.esunbank.com.tw/bank/Layouts/esunbank/Accessibility/rate_exchange.aspx',
                    'HSBC':'https://www.hsbc.com.tw/1/2/Misc/popup-tw/currency-calculator'}

    # This methods returns the page from the link supplied
    def get_bank_content(self, bank_name, bank_url):
        # Using request to get a web page based on the url supplied
        result = requests.get(bank_url)
        # Get the content from the website retrived
        content = result.content
        # Parse the content using pandas library
        content = pandas.read_html(content)
        # Since the content of each bank is not same, we need to get the content based on their characteristic
        if bank_name == 'BOT' or bank_name == 'ESUN':
            content = content[0]
            return content
        elif bank_name == 'CHINATRUST' or bank_name == 'HSBC':
            content = content[1]
            return content
        else:
            print('Bank ' + bank_name + ' is not supported in this website.\n')
            #Raise error

    # This page clean and reformat the data based on our needs
    def clean_up_data(self, bank_name, content):
        if bank_name == 'BOT':
            # This method can extract the data we need based on the location
            currencies = content.iloc[0:,0:3]
            # Reformate the columns name
            currencies.columns=[u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出']
            # Reformate the currency
            currencies[u'幣別'] = currencies[u'幣別'].str.extract('\((\w+)\)')
            # Return Data
            return currencies
        elif bank_name == 'CHINATRUST':
            # This method can extract the data we need based on the location
            currencies = content.iloc[1:,0:3]
            # Reformate the columns name
            currencies.columns=[u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出']
            # Reformate the currency
            currencies[u'幣別'] = currencies[u'幣別'].str.extract('(\\ \w+)')
            # Return Data
            return currencies
        elif bank_name == 'ESUN':
            # This method can extract the data we need based on the location
            currencies = content.iloc[1:]
            # Reformate the columns name
            currencies.columns=[u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出']
            # Reformate the currency
            currencies[u'幣別'] = currencies[u'幣別'].str.extract('\((\w+)\)')
            # Return Data
            return currencies
        elif bank_name == 'HSBC':
            # This method can extract the data we need based on the location
            currencies = content.iloc[3:,[0,3,4]]
            # Reformate the columns name
            currencies.columns=[u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出']
            # Reformate the currency
            currencies[u'幣別'] = currencies[u'幣別'].str.extract('\((\w+)\)')
            # Return Data
            return currencies
        else:
            print('Bank ' + bank_name + ' is not supported in this website.\n')
            #Raise error

    # This will print out the data in the way we formatted
    def print_data(self, bank_name, currencies):
        for count in range(0, currencies.count()[0]):
            print(time.strftime("%Y/%m/%d") + '\t' + '%10s' % bank_name + '\t' + currencies.iloc[count][0] + '\t' + '%8s' % str(currencies.iloc[count][1]) + '\t' + '%8s' % str(currencies.iloc[count][2]))

    # This will write the data to the file
    def write_data_to_file(self, bank_name, currencies):
        try:
            # Open the file for append mode
            handle = open('/home/ubuntu/WebCrawler/WebCrawler/currencies.txt', 'a')
        except IOError:
            #print("File is not exist.  Please check your file name.")
            logging.info('File is not exist.  Please check your file name.')
        else:
            # Iterate the data
            for count in range(0, currencies.count()[0]):
                if bank_name == 'CHINATRUST':
                    bank_name = 'CT'
                elif bank_name == 'ESUN':
                    bank_name = 'ES'
                # Write the data to the file in the way we want
                handle.write(time.strftime("%Y/%m/%d") + '\t' + '%10s' % bank_name + '\t' + currencies.iloc[count][
                    0] + '\t' + '%8s' % str(currencies.iloc[count][1]).strip() + '\t' + '%8s' % str(
                    currencies.iloc[count][2]).strip() + '\n')
            handle.close()

    # Write the data to the database
    def write_data_to_db(self, bank_name, currencies):
        # Define the database's  path
        db_name = '/home/ubuntu/WebCrawler/db.sqlite3'
        # Connect to Database
        db = sqlite3.connect(db_name)
        # Prepared SQL Statement
        sql_statement = 'INSERT INTO Currency (date, bank_short_name, currency, buy, sell) VALUES(?, ?, ?, ?, ?)'
        # Iterate the data and reformatted the bank_name
        for count in range (0, currencies.count()[0]):
            if bank_name == 'CHINATRUST':
                bank_name = 'CT'
            elif bank_name == 'ESUN':
                bank_name = 'ES'
            # Reformatted the data
            date = time.strftime("%Y/%m/%d")
            currency = currencies.iloc[count][0].strip()
            buy = currencies.iloc[count][1]
            if isinstance(buy, float) and math.isnan(buy):
                buy = 0
            sell = currencies.iloc[count][2]
            if isinstance(sell, float) and math.isnan(sell):
                sell = 0.00;
            # Execute the sql statement and insert data
            db.execute(sql_statement, (date, bank_name, currency, buy, sell))
            # Commit the changes
            db.commit()
        # close db connection
        db.close()

if __name__ == '__main__':
    crawler = currency_crawler()
    for key in crawler.bank_website.keys():
        content = crawler.get_bank_content(key, crawler.bank_website[key])
        currencies = crawler.clean_up_data(key, content)
        #print_data(key, currencies)
        crawler.write_data_to_file(key, currencies)
        crawler.write_data_to_db(key, currencies)
    print('END')
