import pandas as pd
from strategies.base_strategy import BaseStrategy
from strategies.momentum import MomentumStrategy
from strategies.mean_reversion import MeanReversionStrategy

class HybridStrategy(BaseStrategy):
    def __init__(self):
        self.momentum = MomentumStrategy()
        self.mean_reversion = MeanReversionStrategy()

    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        momentum_df = self.momentum.generate_signals(df)
        meanrev_df = self.mean_reversion.generate_signals(df)

        df['momentum'] = momentum_df['signal']
        df['meanrev'] = meanrev_df['signal']
        df['signal'] = (df['momentum'] + df['meanrev']).clip(-1, 1)
        return df.dropna()