
import requests
from httpla.config import baseUrl

PATH = '/fapi/v1/premiumIndex'

def mark_price(symbol='dogeusdt'):
    url = baseUrl + PATH
    params = {
        'symbol': symbol,
    }
    r = requests.get(url, params)
    info = r.json()
    return info
    