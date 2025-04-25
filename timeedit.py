from src.reserve import reserve
from src.session import get_session

# A timeedit session lasts for 30 minutes
# How long does a MSISAuth last? Starting 2025-04-25 23:00
room_id = "00598071"
date = "20250426"
start_time = "12:15"
end_time = "13:00"


def main():
    print(f"Trying to resrve '{room_id}': {date} {start_time} {end_time}")
    session = get_session()
    reserve(session, room_id, date, start_time, end_time)


if __name__ == "__main__":
    main()
