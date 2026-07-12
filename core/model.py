from dataclasses import dataclass, field
from typing import Dict, Any, List
from datetime import datetime


@dataclass
class MarketData:

    symbol: str

    price: float

    rsi: float = 50

    sma20: float = 0

    sma50: float = 0

    volatility: float = 0

    trend: str = "UNKNOWN"

    timestamp: str = ""



@dataclass
class TradingSignal:

    strategy: str

    action: str

    confidence: float

    reason: List[str] = field(
        default_factory=list
    )



@dataclass
class TradeDecision:

    symbol: str

    action: str

    quantity: int

    confidence: float

    strategy: str

    regime: str



@dataclass
class RiskResult:

    status: str

    score: float

    reason: List[str]



@dataclass
class TradeResult:

    status: str

    symbol: str

    quantity: int

    price: float

    message: str



@dataclass
class SystemEvent:

    event_type: str

    data: Dict[str,Any]

    timestamp: str = field(
        default_factory=lambda:
        str(datetime.now())
    )