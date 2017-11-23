import datetime
import os
import sqlite3
import WebCrawler.currency as c

# This methods reads from File and return the data based on the User inputted condition.
def read_data_from_file(currency, start=None, end=None):
    # Format the start date into python date object
    d_start = ''
    if '-' in start:
        d_start = datetime.datetime.strptime(start, '%Y-%m-%d')
    elif '/' in start:
        d_start = datetime.datetime.strptime(start, '%Y/%m/%d')
    # Format the end date into python date object
    d_end = ''
    if '-' in end:
        d_end = datetime.datetime.strptime(end, '%Y-%m-%d')
    elif '/' in end:
        d_end = datetime.datetime.strptime(end, '%Y/%m/%d')
    # Create an object (list) to be return
    data_list = []

    try:
        # Open the file
        handle = open('/home/ubuntu/WebCrawler/WebCrawler/currencies.txt', 'r')
    except IOError:
        # Catch exception for File opening
        print("File is not exist.  Please check your file name.")
    else:
        # If there are lines read from file
        for line in handle:
            # Check whther the currency is the one which entered by the user
            if currency in line:
                # Get the data from line
                date, bank_name, cur, buy, sell = line.split('\t')
                # Convert the date from file to python7s data object
                d_date = datetime.datetime.strptime(date, '%Y/%m/%d')
                # Check whther the date is in the range given by the user:
                if d_date >= d_start and d_date <= d_end:
                    # Reformatted the bank_name (removing tailing spaces)
                    bank_name = bank_name.strip(' ')
                    # Reformatted the bank name - Get Whole Bank Name
                    if bank_name == 'BOT':
                        bank_name = 'Bank of Taiwan'
                        #bot.append(date.strip(' ') + ':' + buy.strip(' ') + ':' + sell.rstrip('\n').strip(' '))
                    elif bank_name == 'CT':
                        bank_name = 'Chinatrust Commercial Bank'
                        #ct.append(date.strip(' ') + ':' + buy.strip(' ') + ':' + sell.rstrip('\n').strip(' '))
                    elif bank_name == 'ES':
                        bank_name = 'E\'SUN Bank'
                        #es.append(date.strip(' ') + ':' + buy.strip(' ') + ':' + sell.rstrip('\n').strip(' '))
                    elif bank_name == 'HSBC':
                        bank_name = 'HSBC Bank (Taiwan) Limited.'
                        #hsbc.append(date.strip(' ') + ':' + buy.strip(' ') + ':' + sell.rstrip('\n').strip(' '))
                    # Display the data only if buy or sell is either nan(not a number) or 0,
                    if (not buy.strip() == 'nan') and (not sell.strip() == 'nan') and (not sell.strip() == '-'):
                        object = c.currency(date, bank_name, buy, sell)
                        data_list.append(object)
        # Close the file
        handle.close()
        # Return data_list
        return data_list

#  This method reads the database and return the data based on User inputted condition
def read_data_from_db(bank, currency):
    # Defined DB Path
    db_name = '/home/ubuntu/WebCrawler/db.sqlite3'
    # Connect to DB
    db = sqlite3.connect(db_name)
    # Prepared SQL Statement
    sql_statement = 'SELECT main.Currency.date, main.Bank.bank_name, main.Currency.buy, main.Currency.sell from main.Currency, main.Bank WHERE main.Currency.bank_short_name=main.Bank.bank_short_name AND main.Currency.bank_short_name=? AND main.Currency.currency=?'
    # Execute SQL Statement with the condition supplied
    cursor = db.execute(sql_statement, (bank, currency))
    # Object (list) to be return
    data_list = []

    # Iterate the cursor if there is return from db execution
    for item in cursor:
        # Create an object to fold a data
        object = c.currency(item[0], item[1], item[2], item[3])
        # Add data to the list
        data_list.append(object)

    # Return data_list
    return data_list
