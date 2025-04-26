import requests

# from .helpers import print_response
from .ids import get_room_ids, get_user_id


def reserve(
    session: requests.Session,
    room_search: str,
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
    print("CSTT", cstt)

    room_id = get_room_ids(session, room_search)[0]
    user_id = get_user_id(session)

    res: requests.Response = session.post(
        url=te_url,
        data={
            "kind": "reserve",
            "o": [f"{room_id}.195", f"{user_id}.184"],
            "dates": date,
            "starttime": start_time,
            "endtime": end_time,
            "url": f"https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html#{room_id}",
            "CSTT": cstt,
        },
    )
    print("Reserve", res.status_code, res.reason)
    # print_response(res)
    # print(res.text)
