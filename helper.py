
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

iex_api_key = os.getenv('IEX_API_KEY')

def get_latest_updates(*symbols):
    for i in symbols:
        ticker = i
        
        #creating the API reuqest
        api_url = f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={iex_api_key}'
        
        df = requests.get(api_url).json()
        
        print(df)

get_latest_updates('FB')