import os
import pandas as pd

def save_to_csv(df: pd.DataFrame, symbol: str, folder: str = "data/cache"):
    """Save a DataFrame to CSV."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{symbol}.csv")
    df.to_csv(path)
    print(f"✅ Saved data to {path}")

def load_from_csv(symbol: str, folder: str = "data/cache") -> pd.DataFrame:
    """Load a CSV as a DataFrame."""
    path = os.path.join(folder, f"{symbol}.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(f"No data found for {symbol} in {folder}")
    return pd.read_csv(path, index_col=0, parse_dates=True)