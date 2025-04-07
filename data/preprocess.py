import pandas as pd

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators like returns, rolling mean, and volatility.
    
    Args:
        df (pd.DataFrame): OHLCV dataframe.
    
    Returns:
        pd.DataFrame: DataFrame with indicators.
    """
    df = df.copy()
    df['returns'] = df['close'].pct_change()
    df['rolling_mean'] = df['close'].rolling(window=20).mean()
    df['rolling_std'] = df['close'].rolling(window=20).std()
    df['zscore'] = (df['close'] - df['rolling_mean']) / df['rolling_std']
    return df.dropna()