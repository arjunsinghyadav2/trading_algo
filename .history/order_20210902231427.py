from config import CONSUMER_KEY, REDIRECT_URI, JSON_PATH
from arjun import TD_ACCOUNT
from td.client import TDClient
import pprint
from datetime import datetime, timedelta

#create a new instance of the client
TDSession = TDClient(client_id=CONSUMER_KEY,
                     redirect_uri=REDIRECT_URI, credentials_path=JSON_PATH)

#login into a new session
TDSession.login()

limit_order = {
    "order_type" : "LIMIT",
    "session" : "NORMAL",
    "duration" : "DAY",
    "price" : 8.5,
    "order_statergy_type" : "SINGLE",
    "order_leg_collection" : [
        {
            "instruction" : "BUY",
            "quantity" : 1,
            "instrument" : {
                "symbol" : "PENN",
                "asset_type" : "EQUITY"
            }
        }
    ]
}

# Place the order and grab the order id
order_response = TDSession.place_order(account=TD_ACCOUNT, order = limit_order)
order_id = order_response['order_id']
pprint.pprint(order_response)

# check to see if the order is filled
orders = TDSession.get_orders(account=TD_ACCOUNT)
pprint.pprint(orders)