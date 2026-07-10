from learning.performance_tracker import PerformanceTracker
from learning.strategy_tracker import StrategyTracker
from learning.learning_engine import LearningEngine

tracker = PerformanceTracker()

tracker.add_trade(
    symbol="AAPL",
    strategy="RSI",
    action="BUY",
    entry_price=2,
    exit_price=3,
    quantity=10,
    confidence=90,
    risk="LOW",
    ai_summary="Bullish"
)

tracker.add_trade(
    symbol="TSLA",
    strategy="Moving Average",
    action="SELL",
    entry_price=4,
    exit_price=2,
    quantity=5,
    confidence=60,
    risk="HIGH",
    ai_summary="Bearish"
)

strategy_tracker = StrategyTracker(
    tracker
)

learning = LearningEngine(
    tracker,
    strategy_tracker
)

print()

print(strategy_tracker.analyze())

print()

for line in learning.generate_feedback():

    print("-", line)