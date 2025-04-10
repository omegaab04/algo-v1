import matplotlib.pyplot as plt

def plot_equity_vs_price(df):
    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.plot(df.index, df['close'], label='Price', color='black')
    ax2 = ax1.twinx()
    ax2.plot(df.index, df['cum_returns'], label='Equity', color='green')

    ax1.set_ylabel("Price")
    ax2.set_ylabel("Cumulative Return")

    plt.title("Price vs Strategy Equity")
    plt.show()