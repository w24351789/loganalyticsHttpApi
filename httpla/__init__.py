import datetime
import logging
from httpla.util import symbol_signal
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    symbol_signal('btcusdt')
    symbol_signal('ethusdt')
    symbol_signal('dogeusdt')

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
