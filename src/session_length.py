from requests.sessions import Session
from datetime import datetime
from time import sleep
import requests

from .session import get_session


def test_msis_auth():
    start_time = datetime.now()
    print("Start:", start_time)
    counter = 0
    while True:
        print(f"{counter} Time elapsed: {datetime.now() - start_time}")
        session = get_session()
        _ = session.get("https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html")
        counter += 1
        sleep(30 * 60)  # 30 min
