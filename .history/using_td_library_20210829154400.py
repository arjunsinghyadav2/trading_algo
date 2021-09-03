from config import CONSUMER_KEY, REDIRECT_URI, JSON_PATH
from arjun import TD_ACCOUNT
from td.client import TDClient

#create a new instance of the client
TDSession = TDClient(client_id = CONSUMER_KEY, redirect_uri = REDIRECT_URI, credentials_path = JSON_PATH)

#login into a new session
TDSession.login()

#get current quotes
quotes_response = TDSession.get_quotes(instruments = ['PENN'])
print(quotes_response)

#positions and orders for a account
orders_and_positions = TDSession.get_accounts(account='all',fields=['orders','positions'])

print(orders_and_positions)