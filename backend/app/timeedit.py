from dotenv import load_dotenv
import asyncio

from .helpers import print_response  # pyright:ignore[reportUnusedImport]
from .objects import get_rooms, get_user_id  # pyright:ignore[reportUnusedImport]
from .reserve import (
    reserve,  # pyright:ignore[reportUnusedImport]
    reserve_at_22,  # pyright:ignore[reportUnusedImport]
    reserve_when_available,
)

# A timeedit session lasts for 30 minutes
# How long does a MSISAuth last?
# 48h? 44h?

room_searches = ["fe241", "fe", "sh"]
date = "20250515"
start_time = "13:15"
end_time = "15:00"


async def main():
    print(f"Trying to resrve '{room_searches}': {date} {start_time}-{end_time}")
    # await reserve_at_22(room_searches, date, start_time, end_time)

    await reserve_when_available("fe241", "20250515", "08:15", "10:00")


# rooms = get_room_ids(session, "Fe")
# print(get_user_id(session))


if __name__ == "__main__":
    _ = load_dotenv()
    asyncio.run(main())
