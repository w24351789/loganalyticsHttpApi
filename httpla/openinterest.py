
import requests
from httpla.config import baseUrl

PATH = '/futures/data/openInterestHist'

def open_interest(symbol='dogeusdt', period='5m', limit=1):
    url = baseUrl + PATH
    params = {
        'symbol': symbol,
        'period': period,
        'limit': limit
    }
    r = requests.get(url, params)
    info = r.json()
    return info
    