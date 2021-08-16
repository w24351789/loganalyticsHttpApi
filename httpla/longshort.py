
import requests
from httpla.config import baseUrl

PATH = '/futures/data/globalLongShortAccountRatio'

def long_short_ratio(symbol='dogeusdt', period='5m', limit=1):
    url = baseUrl + PATH
    params = {
        'symbol': symbol,
        'period': period,
        'limit': limit
    }
    r = requests.get(url, params)
    info = r.json()
    return info
    


