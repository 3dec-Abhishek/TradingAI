from positions.position import Position
from positions.position_manager import PositionManager
from positions.portfolio_monitor import PortfolioMonitor

manager = PositionManager()

position = Position(
    symbol="AAPL",
    option_type="CALL",
    strike=320,
    expiration="2026-08-21",
    contracts=2,
    entry_price=3.20,
    stop_loss=2.80,
    take_profit=4.50,
)

manager.open_position(position)

monitor = PortfolioMonitor(manager)

report = monitor.monitor(
    {
        "AAPL": 3.95
    }
)

print(report)