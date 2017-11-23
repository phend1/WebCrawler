from django.shortcuts import render
from WebCrawler.datamanipulator import read_data_from_file
from WebCrawler.datamanipulator import read_data_from_db
from WebCrawler import database

# Create your views here.
# For index.html
def index(request):
    # This will redirect the user to index.html
    return render(request, 'index.html')

# For search_currency.html initialization
def search_currency(request):
    # Get the currencies from Database
    currencies = database.get_currencies()
    no_data = False
    return render(request, 'search_currency.html',
                  {'currencies':currencies,
                   'no_data':no_data})

# For search_currency.html's search button
def search_currency_action(request):
    # Variables initialization
    error = False
    msg = []
    currencies = database.get_currencies()
    from_date = ''
    to_date = ''
    currency = ''
    no_data = False

    # Get User's input - From Date
    if 'from' in request.GET:
        from_date = request.GET['from']
    # Get User's input - To Date
    if 'to' in request.GET:
        to_date = request.GET['to']
    # Get User's input - Currency
    if 'currency' in request.GET:
        currency = request.GET['currency']

    # Input Validation
    if from_date is None or from_date.strip() == '' or len(from_date.strip()) == 0:
        error = True
        msg.append('Please input From as your search condition')
    if to_date is None or to_date.strip() == '' or len(to_date.strip()) == 0:
        error = True
        msg.append('Please input To as your search condition')
    if currency is None or currency.strip() == '' or len(currency.strip()) == 0:
        error = True
        msg.append('Please input Currency as your search condition')

    # If error is true, then return to the page with an error msg
    if error:
        return render(request, 'search_currency.html',
                      {'error':error,
                       'msg':msg,
                       'from_date':from_date,
                       'to_date':to_date,
                       'currency':currency,
                       'currencies': currencies})

    # Search the target currency from the file
    data_list = read_data_from_file(currency, from_date, to_date)
    if (not data_list == None) and len(data_list) == 0:
        no_data = True

    # Return the result and redirect user to search_currency.html with the data
    return render(request, 'search_currency.html',
                  {'from_date':from_date,
                   'to_date':to_date,
                   'currency':currency,
                   'currencies':currencies,
                   'data_list':data_list,
                   'no_data': no_data})

# For search_bank.html initialization
def search_bank(request):
    # Get currency from Database
    currencies = database.get_currencies()
    # Get bank's name from Database
    bank = database.get_bank_name()
    # Redirect user to search_bank.html with the data
    return render(request, 'search_bank.html',
                  {'currencies':currencies,
                   'bank':bank})

# For search_bank.html's action
def search_bank_action(request):
    # Variable Initialization
    bank = ''
    bank_selected = ''
    currency = ''
    currency_selected = ''
    error = False
    msg = []
    data_list = []

    # Get currencies and bank name from Database
    currencies = database.get_currencies()
    bank = database.get_bank_name()

    # Get User's input
    if 'bank' in request.GET:
        bank_selected = request.GET['bank']

    if 'currency' in request.GET:
        currency_selected = request.GET['currency']

    # Validate user's input
    if bank_selected == None or bank_selected.strip() == '' or len(bank_selected.strip()) == 0:
        error = True
        msg.append('Please select Bank you want to look for')

    if currency_selected == None or currency_selected.strip() == '' or len(currency_selected.strip()) == 0:
        error = True
        msg.append('Please select Currency you want to look for')

    # Return to the search_bank.html and data if there is error with user's input
    if error:
        return render(request, 'search_bank.html',
                      {'currencies': currencies,
                       'currency_selected':currency_selected,
                       'bank': bank,
                       'bank_selected':bank_selected,
                       'error': error,
                       'msg': msg,
                       'data_list': data_list})

    # Retrived data from database base fron user's input.
    data_list = read_data_from_db(bank_selected, currency_selected)

    # Return the result and redirect user to search_bank.html
    return render(request, 'search_bank.html',
                  {'currencies': currencies,
                   'currency_selected': currency_selected,
                   'bank': bank,
                   'bank_selected': bank_selected,
                   'data_list': data_list})
