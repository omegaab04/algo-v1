import matplotlib.pyplot as plt

def plot_signals(df):
    """
    Plot price and cumulative strategy returns.
    """
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    df['close'].plot(ax=axes[0], title='Price')
    axes[0].set_ylabel("Price")

    df['cum_returns'].plot(ax=axes[1], title='Cumulative Strategy Returns', color='green')
    axes[1].set_ylabel("Cumulative Return")
    axes[1].axhline(1, color='black', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()