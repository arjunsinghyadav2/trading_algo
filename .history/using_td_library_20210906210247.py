from config import CONSUMER_KEY, REDIRECT_URI, JSON_PATH
from arjun import TD_ACCOUNT
from td.client import TDClient
import pprint
from datetime import datetime, timedelta

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
    symbol='MSFT', period_type='day', period=10, frequency_type='minute', frequency=30)
pprint.pprint(minute_data)

# # Six month worth of daily data
# daily_data = TDSession.get_price_history(
#     symbol='MSFT', period_type='month', period=6, frequency_type='daily', frequency=1)
# pprint.pprint(daily_data)

# # Custom date period
# # Look back period
# lookback_period = 31

# # define today
# today_00 = datetime.now()

# # define days ago
# today_ago = today_00 - timedelta(days=lookback_period)

# # the TD API only accepts dates in the format YYYY-MM-DD
# today_00 = str(int(round(today_00.timestamp()*1000)))
# today_ago = str(int(round(today_ago.timestamp()*1000)))

# histStartDate = today_ago
# histEndDate = today_00

# histPeriodType = 'day'
# histFrequencyType = 'minute'
# histFrequency = 1

# # make the request
# custom_data = TDSession.get_price_history(symbol = 'PENN',
#                                         period_type = histPeriodType,
#                                         frequency_type = histFrequencyType,
#                                         frequency = histFrequency,
#                                         start_date = histStartDate,
#                                         end_date = histEndDate)
# pprint.pprint(custom_data)
