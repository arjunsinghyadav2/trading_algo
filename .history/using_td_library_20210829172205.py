from config import CONSUMER_KEY, REDIRECT_URI, JSON_PATH
from arjun import TD_ACCOUNT
from td.client import TDClient

#create a new instance of the client
TDSession = TDClient(client_id = CONSUMER_KEY, redirect_uri = REDIRECT_URI, credentials_path = JSON_PATH)

#login into a new session
TDSession.login()

# #get current quotes
# quotes_response = TDSession.get_quotes(instruments = ['PENN'])
# print(quotes_response)

# #positions and orders for a account
# orders_and_positions = TDSession.get_accounts(account= TD_ACCOUNT,fields=['orders','positions'])

# print(orders_and_positions)

# #get market hours
# market_hours = TDSession.get_market_hours(markets = ['BOND','FOREX'],date = '2021-08-29')
# print(market_hours)

# #Search Instruments - Symbol 
# search_instruments = TDSession.search_instruments(symbol = 'PENN', projection  = 'symbol-search')
# print(search_instruments)

# #Search Instruments - Description
# search_instruments = TDSession.search_instruments(
#     symbol='tesla', projection='desc-search')
# print(search_instruments)

# #Search Instruments - Fundamentals
# search_instruments = TDSession.search_instruments(
#     symbol='TSLA', projection='fundamental')
# print(search_instruments)

# # Get Movers
# dji_mover = TDSession.get_movers(market = '$DJI', direction = 'up', change = 'value')
# print(dji_mover)

#Get minute data
minute_data = TDSession.get_price_history(
    symbol='MSFT', period_type='day', period=5, frequency_type='minute', frequency=1, extended_hours_data=True)
print(minute_data)
