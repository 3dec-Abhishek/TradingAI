from learning.performance_tracker import PerformanceTracker
from learning.trade_statistics import TradeStatistics

tracker = PerformanceTracker()

tracker.add_trade(
    symbol="AAPL",
    strategy="RSI",
    action="BUY CALL",
    entry_price=2.50,
    exit_price=3.20,
    quantity=10,
    confidence=85,
    risk="LOW",
    ai_summary="Strong bullish setup"
)

tracker.add_trade(
    symbol="TSLA",
    strategy="Moving Average",
    action="BUY PUT",
    entry_price=5.00,
    exit_price=4.20,
    quantity=5,
    confidence=72,
    risk="MEDIUM",
    ai_summary="Trend reversal"
)

stats = TradeStatistics(tracker)

print(stats.generate())