import os
import pandas as pd
from alpaca_trade_api.rest import REST
from dotenv import load_dotenv

load_dotenv()

# Load API keys 
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

# Initialise API keys
api = REST(API_KEY, API_SECRET, BASE_URL)

def get_historical_data(symbol: str, timeframe: str = "1D", limit: int = 1000) -> pd.DataFrame:
    """
    Fetch historical OHLCV data for a given symbol and timeframe.
    
    Args:
        symbol (str): Ticker symbol (e.g., "AAPL").
        timeframe (str): Bar timeframe (e.g., "1Min", "5Min", "1H", "1D").
        limit (int): Number of data points to fetch (max 10000).
    
    Returns:
        pd.DataFrame: OHLCV DataFrame indexed by datetime.
    """
    bars = api.get_bars(symbol, timeframe, limit=limit).df
    if bars.empty:
        raise ValueError(f"No data returned for {symbol}")

    df = bars[bars['symbol'] == symbol].copy()
    df.drop(columns=['symbol'], inplace=True)
    df.index = pd.to_datetime(df.index)
    return df