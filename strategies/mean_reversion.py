import pandas as pd
from strategies.base_strategy import BaseStrategy

class MeanReversionStrategy(BaseStrategy):
    def __init__(self, window: int = 20, threshold: float = 1.0):
        self.window = window
        self.threshold = threshold

    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['mean'] = df['close'].rolling(self.window).mean()
        df['std'] = df['close'].rolling(self.window).std()
        df['zscore'] = (df['close'] - df['mean']) / df['std']
        df['signal'] = 0
        df.loc[df['zscore'] > self.threshold, 'signal'] = -1
        df.loc[df['zscore'] < -self.threshold, 'signal'] = 1
        return df.dropna()