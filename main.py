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

# Config

STRATEGY = "hybrid"           # Choose: 'momentum', 'meanrev', 'hybrid'
SYMBOL = "AAPL"
TIMEFRAME = "1D"
BARS_LIMIT = 200
NEWS_OVERRIDE = True
MANUAL_MODE = True            # ← NEW toggle for news-only + price mode
SLEEP_INTERVAL = 60 * 5       # 5 min loop

# Strategy loading

def load_strategy(name: str):
    if name == "momentum":
        return MomentumStrategy(fast=10, slow=50)
    elif name == "meanrev":
        return MeanReversionStrategy(window=20, threshold=1.0)
    elif name == "hybrid":
        return HybridStrategy()
    else:
        raise ValueError(f"Unknown strategy: {name}")

# Main
def main():
    strategy = load_strategy(STRATEGY)
    log(f"🚀 Running strategy: {STRATEGY} on {SYMBOL}")
    if MANUAL_MODE:
        log("🧠 Manual Mode Active: Trading is disabled.")

    while True:
        try:
            # Fetching market data
            df = get_historical_data(SYMBOL, timeframe=TIMEFRAME, limit=BARS_LIMIT)
            latest_price = df['close'].iloc[-1]

            if MANUAL_MODE:
                # Manual monitor only
                log(f"💰 Latest price for {SYMBOL}: ${latest_price:.2f}")
                monitor_trump_news(trigger_threshold=-0.5)
                log(f"⏱ Waiting {SLEEP_INTERVAL // 60} min before next check...\n")
                time.sleep(SLEEP_INTERVAL)
                continue

            # Signal
            df = strategy.generate_signals(df)
            latest_signal = df['signal'].iloc[-1]

            # Trump news override
            if NEWS_OVERRIDE and monitor_trump_news():
                log("🚨 News override triggered — no trades executed.")
                time.sleep(SLEEP_INTERVAL)
                continue

            # Risk limits
            if is_risk_exceeded():
                log("⛔ Risk limit exceeded — exiting loop.")
                break

            # Executing trade
            current_pos = get_current_position(SYMBOL)
            execute_trade(SYMBOL, latest_signal, current_pos)

        except Exception as e:
            log(f"⚠️ Error in main loop: {e}")

        # Sleep until next cycle
        time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    main()