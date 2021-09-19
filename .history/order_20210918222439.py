from td.client import TDClient
import pprint
from datetime import datetime, timedelta
from configparser import ConfigParser

# Grab configuration values.
config = ConfigParser()
config.read('configs/config.ini')

CONSUMER_KEY = config.get('main', 'CLIENT_ID')
REDIRECT_URI = config.get('main', 'REDIRECT_URI')
CREDENTIALS_PATH = config.get('main', 'JSON_PATH')
TD_ACCOUNT = config.get('main', 'TD_ACCOUNT')

#create a new instance of the client
TDSession = TDClient(client_id=CONSUMER_KEY,
                     redirect_uri=REDIRECT_URI, credentials_path=CREDENTIALS_PATH)

#login into a new session
TDSession.login()

limit_order = {
    "orderType" : "LIMIT",
    "session" : "NORMAL",
    "duration" : "DAY",
    "price" : 8.,
    "orderStrategyType" : "SINGLE",
    "orderLegCollection" : [
        {
            "instruction" : "BUY",
            "quantity" : 1,
            "instrument" : {
                "symbol" : "PENN",
                "assetType" : "EQUITY"
            }
        }
    ]
}

new_limit_order = {
    "orderType" : "LIMIT",
    "session" : "NORMAL",
    "duration" : "DAY",
    "price" : 8.2,
    "orderStrategyType" : "SINGLE",
    "orderLegCollection" : [
        {
            "instruction" : "BUY",
            "quantity" : 1,
            "instrument" : {
                "symbol" : "PENN",
                "assetType" : "EQUITY"
            }
        }
    ]
}

#Place the order and grab the order id
order_response = TDSession.place_order(account=TD_ACCOUNT, order = limit_order)
order_id = order_response['order_id']
pprint.pprint(order_response)

#Modify an existing order
modified_order_response = TDSession.modify_order(account=TD_ACCOUNT, order = new_limit_order,order_id=order_id)
modified_order_id = modified_order_response['order_id']
pprint.pprint(modified_order_response)


#Cancel an existing order
canceled_order_response = TDSession.cancel_order(account=TD_ACCOUNT, order_id=modified_order_id)
pprint.pprint(canceled_order_response)

# check to see if the order is filled
orders = TDSession.get_orders(account=TD_ACCOUNT)
pprint.pprint(orders)
