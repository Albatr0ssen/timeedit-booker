from src.cli import root
from src.ids import get_room_ids, get_user_id  # pyright:ignore[reportUnusedImport]
from src.reserve import reserve, reserve_at_22  # pyright:ignore[reportUnusedImport]
from src.session import get_session

# A timeedit session lasts for 30 minutes
# How long does a MSISAuth last?
# 48h? 44h?
# Starting 2025-04-27 ca 19:00

room_search = "fe244"
date = "20250501"
start_time = "10:15"
end_time = "12:00"


def main():
    session = get_session()
    # root(session)
    # print(f"Trying to resrve '{room_search}': {date} {start_time}-{end_time}")
    reserve_at_22(session, room_search, date, start_time, end_time)
    # # rooms = get_room_ids(session, "Fe")
    # print(get_user_id(session))


if __name__ == "__main__":
    main()
