
import pandas as pd
import requests

def get_latest_updates(*symbols):
    for i in symbols:
        ticker = i
        iex_api_key = 'pk_853c001b291b46c7879b9b80e848ebef'
        
        #creating the API reuqest
        api_url = f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={iex_api_key}'
        
        df = requests.get(api_url).json()
        
        # print(df)

get_latest_updates('FB')