from datetime import datetime, timedelta
from requests import Session

from src.objects import get_rooms, get_user_id  # pyright:ignore[reportUnusedImport]
from src.reserve import reserve, reserve_at_22  # pyright:ignore[reportUnusedImport]
from src.session import get_session


def root(session):
    while True:
        print()
        print("1. Boka")
        print("2. Debug")
        choice = input()

        match (choice):
            case "1":
                boka(session)
            case _:
                print("bad choice")


def boka(session: Session):
    start_hour = get_time("Starttid (timme): ")
    end_hour = get_time("Sluttid (timme): ")
    datetime = get_date("Datum: ")
    room = input("Rum: ")

    date = datetime.strftime("%Y%m%d")
    start_time = f"{start_hour}:15"
    end_time = f"{end_hour}:00"

    reserve(session, [room], date, start_time, end_time)


def get_time(prompt: str):
    while True:
        try:
            time = int(input(prompt))
            if time >= 0 and time < 24:
                return time
        except:
            pass


def get_date(prompt: str):
    date_format = "%Y-%m-%d"

    while True:
        try:
            date = datetime.strptime(input(prompt), date_format)
            return date
        except:
            pass


def get_bookable_dates():
    now = datetime.today()

    if now.hour >= 22:
        now = now + timedelta(days=1)

    day0 = now.strftime("%Y-%m-%d")
    day1 = (now + timedelta(days=1)).strftime("%Y-%m-%d")
    day2 = (now + timedelta(days=2)).strftime("%Y-%m-%d")

    return [day0, day1, day2]
