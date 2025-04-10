# execution/position_tracker.py

from execution.alpaca_interface import api

def get_current_position(symbol: str) -> int:
    """
    Returns current position quantity (+ for long, - for short, 0 for flat).
    """
    try:
        position = api.get_position(symbol)
        qty = int(position.qty)
        return qty if position.side == 'long' else -qty
    except:
        return 0  # No position