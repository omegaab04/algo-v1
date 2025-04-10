import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')