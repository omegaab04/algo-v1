# main.py

import time
import pandas as pd
from data.fetch_alpaca_data import get_historical_data
from strategies.momentum import MomentumStrategy
from strategies.mean_reversion import MeanReversionStrategy
from strategies.hybrid_strategy import HybridStrategy
from execution.order_executor import execute_trade
from execution.position_tracker import get_current_position
from execution.risk_manager import is_risk_exceeded
from news.news_monitor import monitor_trump_news
from utils.logger import log
from config.alpaca_keys import API_KEY, API_SECRET, BASE_URL

STRATEGY = "hybrid"            # Choose: 'momentum', 'meanrev', 'hybrid'
SYMBOL = "AAPL"                # Choose your ticker
TIMEFRAME = "1D"
BARS_LIMIT = 200
SLEEP_INTERVAL = 60 * 5        # 5 min loop
NEWS_OVERRIDE = True           # Block trades if risky Trump news detected
MANUAL_MODE = False            # Set to True for news + price only

def load_strategy(name: str):
    if name == "momentum":
        return MomentumStrategy(fast=10, slow=50)
    elif name == "meanrev":
        return MeanReversionStrategy(window=20, threshold=1.0)
    elif name == "hybrid":
        return HybridStrategy()
    else:
        raise ValueError(f"Unknown strategy: {name}")

def main():
    strategy = load_strategy(STRATEGY)
    log(f"Running strategy: {STRATEGY} on {SYMBOL}")
    if MANUAL_MODE:
        log("Manual Mode: No trades will be executed.")

    while True:
        try:
            # 1. Fetch market data
            df = get_historical_data(SYMBOL, timeframe=TIMEFRAME, limit=BARS_LIMIT)
            latest_price = df['close'].iloc[-1]

            if MANUAL_MODE:
                # Just display price and Trump news sentiment
                log(f"Latest price for {SYMBOL}: ${latest_price:.2f}")
                monitor_trump_news(trigger_threshold=-0.5)
                log(f"Waiting {SLEEP_INTERVAL // 60} minutes...\n")
                time.sleep(SLEEP_INTERVAL)
                continue

            # 2. Generate signal
            df = strategy.generate_signals(df)
            latest_signal = df['signal'].iloc[-1]

            # 3. Check Trump news
            if NEWS_OVERRIDE and monitor_trump_news():
                log("Trade blocked due to Trump news event.")
                time.sleep(SLEEP_INTERVAL)
                continue

            # 4. Check risk limits
            if is_risk_exceeded():
                log("Risk limit exceeded — no trades placed.")
                time.sleep(SLEEP_INTERVAL)
                continue

            # 5. Execute trade
            current_pos = get_current_position(SYMBOL)
            execute_trade(SYMBOL, latest_signal, current_pos)

        except Exception as e:
            log(f"Error in main loop: {e}")

        # 6. Sleep before next cycle
        time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    main()