from requests import Session


class Room:
    id: str = ""
    name: str = ""

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


def get_room_ids(session: Session, search_text: str):
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
