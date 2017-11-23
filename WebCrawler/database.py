import datetime
import logging
import os
import sqlite3
import sys

# This will parse the data from text file and insert the data to db
def read_text_file_to_db():
    try:
        # Defined DB's path
        db_name = '/home/ubuntu/WebCrawler/db.sqlite3'
        # Connect to DB
        db = sqlite3.connect(db_name)
        # Prepared SQL Statement
        sql_statement = 'INSERT INTO Currency (date, bank_short_name, currency, buy, sell) VALUES(?, ?, ?, ?, ?)'
        # Open the file
        handle = open('currencies.txt', 'r')
        # Iterate each line in the file
        for line in handle:
            # format the data
            line = line.rstrip()
            date, bank, currency, buy, sell = line.split("\t")
            date = datetime.datetime.strptime(date.strip(), "%Y/%m/%d").date()
            bank = bank.strip()
            currency = currency.strip()
            if buy.strip() == '-' or buy.strip() == 'nan':
                buy = '0.0'
            if sell.strip() == '-' or sell.strip() == 'nan':
                sell = '0.0'
            buy = float(buy.strip())
            sell = float(sell.strip())
            # Execute the SQL Statement
            db.execute(sql_statement, (date, bank, currency, buy, sell))
            # Commit the changes
            db.commit()
    except:
        # Print out an error
        print(sys.exc_info()[0])
    else:
        # Close DB's connection
        db.close()

# Methods used for retrived currencies from DB
def get_currencies():
    #sys.stderr.write((os.getcwd())
    # Define DB's file path
    db_name = '/home/ubuntu/WebCrawler/db.sqlite3'
    logging.info(db_name)
    # Connect to database
    db = sqlite3.connect(db_name)
    # Prepared SQL statement
    sql_statement1 = 'SELECT DISTINCT(currency) FROM Currency ORDER BY currency'
    # Initialization of variable
    currencies = []
    # Execute the prepared sql statement
    cursor = db.execute(sql_statement1)
    # Iterate the result
    for item in cursor:
        # Add result to the list
        currencies.append(item[0])
    # Cloised the DB connection
    db.close()
    # Return currencies
    return currencies

# Methods used for retrived bank's name from database
def get_bank_name():
    # Define DB's file path
    db_name = '/home/ubuntu/WebCrawler/db.sqlite3'
    # Connect to database
    db = sqlite3.connect(db_name)
    # Prepared SQL statement
    sql_statement1 = 'SELECT DISTINCT(Currency.bank_short_name), Bank.bank_name FROM Currency, Bank WHERE Currency.bank_short_name = Bank.bank_short_name'
    # Initialization of variable
    bank = []
    # Execute the prepared sql statement
    cursor = db.execute(sql_statement1)
    # Iterate the result
    for item in cursor:
        # Add result to the list
        bank.append((item[0], item[1]))
    # Cloised the DB connection
    db.close()
    # Return result
    return bank


