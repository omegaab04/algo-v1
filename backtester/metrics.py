import numpy as np

def evaluate_performance(df):
    """
    Print key performance metrics from the backtest.
    """
    strategy_returns = df['strategy_returns'].dropna()
    cum_return = df['cum_returns'].iloc[-1] - 1
    annual_return = (1 + cum_return) ** (252 / len(df)) - 1
    sharpe = (strategy_returns.mean() / strategy_returns.std()) * np.sqrt(252)
    mdd = calculate_max_drawdown(df['cum_returns'])

    print("\n📈 Backtest Performance")
    print(f"Total Return:       {cum_return:.2%}")
    print(f"Annualised Return:  {annual_return:.2%}")
    print(f"Sharpe Ratio:       {sharpe:.2f}")
    print(f"Max Drawdown:       {mdd:.2%}")

def calculate_max_drawdown(cum_returns):
    """
    Calculate max drawdown from cumulative return curve.
    """
    roll_max = cum_returns.cummax()
    drawdown = cum_returns / roll_max - 1.0
    return drawdown.min()