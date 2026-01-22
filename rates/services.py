import requests
from decimal import Decimal

CBR_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

def get_usd_rate() -> Decimal:
    response = requests.get(CBR_URL, timeout=5)
    response.raise_for_status()
    data = response.json()
    return Decimal(data['Valute']['USD']['Value'])