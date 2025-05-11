from dotenv import load_dotenv
import asyncio

from src.helpers import print_response  # pyright:ignore[reportUnusedImport]
from src.ids import get_room_ids, get_user_id  # pyright:ignore[reportUnusedImport]
from src.reserve import (
    reserve,  # pyright:ignore[reportUnusedImport]
    reserve_at_22,  # pyright:ignore[reportUnusedImport]
)

# A timeedit session lasts for 30 minutes
# How long does a MSISAuth last?
# 48h? 44h?

room_searches = ["sh603", "sh6", "sh"]
date = "20250511"
start_time = "20:15"
end_time = "21:00"


async def main():
    print(f"Trying to resrve '{room_searches}': {date} {start_time}-{end_time}")
    await reserve(room_searches, date, start_time, end_time)
    # # rooms = get_room_ids(session, "Fe")
    # print(get_user_id(session))


if __name__ == "__main__":
    _ = load_dotenv()
    asyncio.run(main())
