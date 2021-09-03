from config import CONSUMER_KEY,REDIRECT_URI,JSON_PATH
from arjun import TD_ACCOUNT
from td.client import TDClient

#create a new instance of the client
td_client = TDClient(consumer_id = CONSUMER_KEY, redirect_uri = REDIRECT_URI, json_path = JSON_PATH)
