import pandas as pd
from typing import Type
from strategies.base_strategy import BaseStrategy
from backtester.metrics import evaluate_performance
from backtester.vis import plot_signals
from utils.logger import log

def run_backtest(df: pd.DataFrame, strategy_class: Type[BaseStrategy], strategy_params: dict = {}) -> pd.DataFrame:
    """
    Run a strategy on historical OHLCV data and evaluate performance.
    
    Args:
        df: DataFrame with historical OHLCV data.
        strategy_class: The strategy class (must implement BaseStrategy).
        strategy_params: Parameters to pass into the strategy.

    Returns:
        DataFrame with strategy results.
    """
    log(f"📊 Starting backtest with {strategy_class.__name__}")

    strategy = strategy_class(**strategy_params)
    df = strategy.generate_signals(df)

    # Calculate positions and PnL
    df['position'] = df['signal'].shift(1).fillna(0)
    df['returns'] = df['close'].pct_change().fillna(0)
    df['strategy_returns'] = df['position'] * df['returns']
    df['cum_returns'] = (1 + df['strategy_returns']).cumprod()

    evaluate_performance(df)
    plot_signals(df)

    return df