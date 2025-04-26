# from src.ids import get_room_ids, get_user_id
from src.reserve import reserve
from src.session import get_session

# A timeedit session lasts for 30 minutes
# How long does a MSISAuth last? Starting 2025-04-25 23:00
room_search = "Fe"
date = "20250427"
start_time = "11:15"
end_time = "12:00"


def main():
    print(f"Trying to resrve '{room_search}': {date} {start_time} {end_time}")
    session = get_session()
    reserve(session, room_search, date, start_time, end_time)
    # get_room_ids(session, "Fe")
    # get_user_id(session)


if __name__ == "__main__":
    main()
