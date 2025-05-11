from dotenv import load_dotenv

from src.helpers import print_response  # pyright:ignore[reportUnusedImport]
from src.cli import root  # pyright:ignore[reportUnusedImport]
from src.ids import get_room_ids, get_user_id  # pyright:ignore[reportUnusedImport]
from src.reserve import reserve, reserve_at_22  # pyright:ignore[reportUnusedImport]
from src.session import get_session


# A timeedit session lasts for 30 minutes
# How long does a MSISAuth last?
# 48h? 44h?

room_searches = ["sh603", "sh6", "sh"]
date = "20250513"
start_time = "08:15"
end_time = "10:00"


def main():
    session = get_session()
    # root(session)
    print(f"Trying to resrve '{room_searches}': {date} {start_time}-{end_time}")
    reserve_at_22(session, room_searches, date, start_time, end_time)
    # # rooms = get_room_ids(session, "Fe")
    # print(get_user_id(session))


if __name__ == "__main__":
    _ = load_dotenv()
    main()
