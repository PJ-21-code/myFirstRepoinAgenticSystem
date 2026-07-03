import logging
from tenacity import retry, stop_after_attempt, wait_exponential, before_sleep_log

logging.basicConfig(filename='logs/api_retries.log',level= logging.INFO)
logger= logging.getLogger(__name__)

attempt_counter= {'n':0}

@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    )

def lookup_order_status(order_id: str) -> str:

    attempt_counter['n'] +=1
    
    if attempt_counter['n']<=2:
        raise Exception('HTTP 429 Too many attempts')
    
    return f'Order {order_id} — out for delivery. Expected by 6 PM today'

if __name__ == '__main__':
    print(lookup_order_status('ORD-7842'))

    

