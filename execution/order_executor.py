from execution.alpaca_interface import api
from utils.logger import log

def execute_trade(symbol: str, signal: int, current_position: int, qty: int = 10):
    """
    Executes a trade based on signal and current position.
    Signal: 1 = long, -1 = short, 0 = exit.
    """
    if signal == current_position:
        log(f"🟡 Holding {symbol}: no action needed.")
        return

    try:
        if signal == 1:
            log(f"🟢 Going long: Buying {qty} shares of {symbol}")
            if current_position < 0:
                api.submit_order(symbol=symbol, qty=abs(current_position), side='buy', type='market', time_in_force='gtc')
            api.submit_order(symbol=symbol, qty=qty, side='buy', type='market', time_in_force='gtc')

        elif signal == -1:
            log(f"🔴 Going short: Selling {qty} shares of {symbol}")
            if current_position > 0:
                api.submit_order(symbol=symbol, qty=abs(current_position), side='sell', type='market', time_in_force='gtc')
            api.submit_order(symbol=symbol, qty=qty, side='sell', type='market', time_in_force='gtc')

        elif signal == 0 and current_position != 0:
            log(f"⚪ Exiting position: Closing {current_position} shares of {symbol}")
            side = 'sell' if current_position > 0 else 'buy'
            api.submit_order(symbol=symbol, qty=abs(current_position), side=side, type='market', time_in_force='gtc')

    except Exception as e:
        log(f"❌ Trade execution failed: {e}")