import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Trading AI"

BROKER = os.getenv(
    "BROKER",
    "MOCK"
)

RISK_LIMIT = {
    "max_position_percent": 20,
    "max_daily_loss_percent": 2
}
