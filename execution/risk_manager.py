from execution.alpaca_interface import api
from utils.logger import log

# Risk thresholds
MAX_POSITIONS = 5           # Max number of open positions
MAX_POSITION_SIZE = 10000   # Max dollar size per position
MAX_TOTAL_EXPOSURE = 50000  # Max total capital at risk

def is_risk_exceeded() -> bool:
    """
    Returns True if portfolio is at or over risk limits.
    """
    try:
        positions = api.list_positions()
        if len(positions) > MAX_POSITIONS:
            log("⚠️ Too many open positions")
            return True

        total_exposure = 0
        for p in positions:
            value = float(p.market_value)
            if value > MAX_POSITION_SIZE:
                log(f"⚠️ Position {p.symbol} exceeds size limit (${value:.2f})")
                return True
            total_exposure += value

        if total_exposure > MAX_TOTAL_EXPOSURE:
            log(f"⚠️ Total exposure too high: ${total_exposure:.2f}")
            return True

        return False

    except Exception as e:
        log(f"❌ Risk check failed: {e}")
        return True  # safer to stop trading if uncertain