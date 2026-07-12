from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class MarketData:

    symbol: str

    price: float

    rsi: float = 50

    sma20: float = 0

    sma50: float = 0

    volatility: float = 0

    trend: str = "UNKNOWN"



@dataclass
class StrategySignal:

    strategy: str = "UNKNOWN"

    signal: str = "HOLD"

    confidence: float = 50



@dataclass
class TradeDecision:

    symbol: str

    action: str = "HOLD"

    strategy: str = "UNKNOWN"

    confidence: float = 50

    quantity: int = 0

    reasons: list = field(default_factory=list)



@dataclass
class RiskResult:

    status: str = "UNKNOWN"

    score: float = 0

    reason: list = field(default_factory=list)
