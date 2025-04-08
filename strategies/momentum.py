import pandas as pd
from strategies.base_strategy import BaseStrategy

class MomentumStrategy(BaseStrategy):
    def __init__(self, fast: int = 10, slow: int = 50):
        self.fast = fast
        self.slow = slow

    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['sma_fast'] = df['close'].rolling(self.fast).mean()
        df['sma_slow'] = df['close'].rolling(self.slow).mean()
        df['signal'] = 0
        df.loc[df['sma_fast'] > df['sma_slow'], 'signal'] = 1
        df.loc[df['sma_fast'] < df['sma_slow'], 'signal'] = -1
        return df.dropna()