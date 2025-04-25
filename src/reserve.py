import requests


def reserve(
    session: requests.Session,
    # TEliuweb: str,
    room_id: str,
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

    res: requests.Response = session.post(
        url=te_url,
        data={
            "kind": "reserve",
            "o": ["646946.195", "715608.184"],
            "dates": date,
            "starttime": start_time,
            "endtime": end_time,
            "url": f"https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html#{room_id}",
            "CSTT": cstt,
        },
    )
    print("Reserve", res.status_code, res.reason)
