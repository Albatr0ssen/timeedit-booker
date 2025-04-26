from requests import Session


def get_room_ids(session: Session, search_text: str):
    res = session.get(
        url="https://cloud.timeedit.net/liu/web/wr_stud/objects.json",
        params={"sid": 4, "types": 195, "search_text": search_text},
    )

    if res.status_code != 200:
        raise Exception("Failed to get rooms")

    room_ids: list[str] = res.json()["ids"]  # pyright: ignore[reportAny]
    print(room_ids)
    return room_ids


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
