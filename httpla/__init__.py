import datetime
import logging
import json
import os
from httpla.longshort import long_short_ratio
from httpla.openinterest import open_interest
from httpla.price import mark_price
from httpla.http2la import post_data
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    # Update the customer ID to your Log Analytics workspace ID
    customer_id = os.environ['customer_id']

    # For the shared key, use either the primary or the secondary Connected Sources client authentication key   
    shared_key = os.environ['shared_key']

    # The log type is the name of the event that is being submitted
    longshort_table = 'LongShortRate'

    long_short_ratio_data = long_short_ratio('dogeusdt', '5m', 1)

    long_short_body = json.dumps(long_short_ratio_data)


    # open interest
    open_interest_table = 'OpenInterest'

    open_interest_data = open_interest('dogeusdt', '5m', 1)

    openinterest_body = json.dumps(open_interest_data)

    # mark price
    mark_price_table = 'MarkPriceData'

    mark_price_data = mark_price('dogeusdt')

    mark_price_body = json.dumps(mark_price_data)

    # Post to Log Analytics

    post_data(customer_id, shared_key, long_short_body, longshort_table)
    post_data(customer_id, shared_key, openinterest_body, open_interest_table)
    post_data(customer_id, shared_key, mark_price_body, mark_price_table)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
