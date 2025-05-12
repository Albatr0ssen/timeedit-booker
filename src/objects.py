import asyncio
from random import random
from requests import Session
from typing import cast

from .session import get_session


class Room:
    id: str = ""
    name: str = ""

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


def get_rooms(session: Session, search_text: str):
    res = session.get(
        url="https://cloud.timeedit.net/liu/web/wr_stud/objects.json",
        params={"sid": 4, "types": 195, "search_text": search_text},
    )

    if res.status_code != 200:
        raise Exception("Failed to get rooms")

    rooms: list[Room] = []
    room_records: list[str] = res.json()["records"]  # pyright: ignore[reportAny]
    for record in room_records:
        id = record["id"]  # pyright: ignore[reportArgumentType]
        name = record["fields"][0]["values"][0]  # pyright: ignore[reportArgumentType]
        room: Room = Room(id, name)
        rooms.append(room)

    return rooms


def get_user_id(session: Session):
    res = session.get(
        url="https://cloud.timeedit.net/liu/web/wr_stud/objects.json",
        params={"sid": 4, "types": 184},
    )

    if res.status_code != 200:
        raise Exception("Failed to get rooms")

    user_id: str = res.json()["ids"][0]  # pyright: ignore[reportAny]
    print(user_id)
    return user_id


async def wait_for_reservable_room(
    search_text: str, date: str, start_time: str, end_time: str
):
    session = await get_session()

    while True:
        res = session.get(
            url="https://cloud.timeedit.net/liu/web/wr_stud/objects.json",
            params={
                "max": 50,
                "part": "t",
                "sid": 4,
                "l": "sv_SE",
                "types": "195",
                "subtypes": "230",
                "fe": ["23.Valla", "160.Studbok-grupprum-24h"],
                "dates": f"{date}-{date}",
                "starttime": f"{start_time}:0",
                "endtime": f"{end_time}:0",
                "search_text": f"{search_text}",
            },
        )

        if res.status_code == 412:
            print("Session expired, getting new")
            session = await get_session()
            continue
        elif res.text == '"Inga sökresultat"':
            print(".", end="", flush=True)
            await asyncio.sleep(2 + random() * 2)
            continue
        elif res.status_code == 200:
            print(res.text)
            room_id = cast(str, res.json()["objects"][0]["id"])
            room_name = cast(str, res.json()["objects"][0]["fields"]["Signatur"])
            return Room(room_id, room_name)
        else:
            raise SystemExit(res.text)
    # if res.text == :
