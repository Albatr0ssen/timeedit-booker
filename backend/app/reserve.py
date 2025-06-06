import asyncio
import random
from time import sleep
import requests
from datetime import datetime

from .session import get_session
from .helpers import print_response  # pyright:ignore[reportUnusedImport]
from .objects import (
    Room,
    get_rooms,
    get_user_id,
    wait_for_reservable_room,
)


async def reserve_at_22(
    room_searches: list[str],
    date: str,
    start_time: str,
    end_time: str,
):
    now = datetime.today()
    at_22 = now.replace(hour=22, minute=00, second=1)
    time_till_22 = at_22.timestamp() - now.timestamp()
    if time_till_22 < 0:
        raise Exception("Already after 22")
    print(f"Sleeping for {time_till_22} sec")
    sleep(time_till_22)
    await reserve(room_searches, date, start_time, end_time)


async def reserve(
    room_searches: list[str],
    date: str,
    start_time: str,
    end_time: str,
) -> None:
    session = await asyncio.create_task(get_session())
    for room_search in room_searches:
        rooms = get_rooms(session, room_search)
        if await asyncio.create_task(
            reserve_a_room(session, rooms, date, start_time, end_time)
        ):
            return


async def reserve_a_room(
    session: requests.Session,
    rooms: list[Room],
    date: str,
    start_time: str,
    end_time: str,
):
    te_url = "https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html"

    cstt_res = session.post(
        url=te_url,
        data={"CSTTG": "gen"},
    )

    if cstt_res.status_code != 200:
        raise SystemExit("CSTT", cstt_res.status_code, cstt_res.reason)

    cstt = cstt_res.text
    # print("CSTT", cstt)

    user_id = get_user_id(session)

    for room in rooms:
        res: requests.Response = session.post(
            url=te_url,
            data={
                "kind": "reserve",
                "o": [f"{room.id}.195", f"{user_id}.184"],
                "dates": date,
                "starttime": start_time,
                "endtime": end_time,
                "url": f"https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html#{room.id}",
                "CSTT": cstt,
            },
        )

        if res.status_code == 200:
            print(
                f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Successfully booked {room.name} {start_time}-{end_time}"
            )
            return True

        print(f"Failed to book {room.name}", res.status_code, res.reason)
        match (res.status_code):
            case 409:
                error_text = res.text
                no_bookable_hours = "Bokningen kunde ej genomföras.  Användarens maximala bokningslängd har överskridits"
                not_available = "Bokningen kunde ej genomföras.  Tiden är upptagen eftersom objektet"
                out_of_range_date = "Bokningen kunde ej genomföras.  Bokningen är utanför datumgränserna"
                out_of_range_time = "Time not in date range"
                if error_text.startswith(no_bookable_hours):
                    print("No bookable hours")
                elif error_text.startswith(not_available):
                    print("Room not available")
                elif error_text.startswith(out_of_range_date):
                    print("Time not in date range")
                elif error_text.startswith(out_of_range_time):
                    print("Time not in time range")
                else:
                    print("Unkown 409 error", res.text)
            case _:
                raise Exception("Unkown response trying to reserve, session expired?")

    return False


async def reserve_when_available(
    search_text: str, date: str, start_time: str, end_time: str
):
    room = await wait_for_reservable_room(search_text, date, start_time, end_time)
    session = await get_session()
    _ = await reserve_a_room(session, [room], date, start_time, end_time)
