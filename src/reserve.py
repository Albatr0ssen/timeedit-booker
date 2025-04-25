from datetime import datetime
from http.cookiejar import Cookie
import requests

from .helpers import print_response


def reserve(
    TEliuweb: str,
    room_id: str,
    MSIS_auth: str,
    start_time: str,
    end_time: str,
):
    session = requests.session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    }

    cookies = {
        "sso-parameters": "back=https%3A%2F%2Fcloud.timeedit.net%2Fliu%2Fweb%2Fwr_stud%2F",
        "ssoserver": "liu_stud_saml2",
        "TEliuweb": TEliuweb,
    }

    # fs_liu_cookie = Cookie(
    #     name="MSISAuth",
    #     value=MSIS_auth,
    #     secure=True,
    #     expires=None,
    #     discard=True,
    #     rest={"HttpOnly": "true"},
    #     # Domain
    #     domain_specified=True,
    #     domain_initial_dot=False,
    #     domain="fs.liu.se",
    #     # Path
    #     path_specified=True,
    #     path="/adfs",
    #     # Version
    #     version=0,
    #     rfc2109=False,
    #     # Port
    #     port=None,
    #     port_specified=False,
    #     # Comment
    #     comment=None,
    #     comment_url=None,
    # )

    # session.cookies.set_cookie(fs_liu_cookie)  # pyright:ignore[reportUnknownMemberType]

    te_url = "https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html"

    cstt_res = requests.post(
        url=te_url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"
        },
        cookies=cookies,
        data={"CSTTG": "gen"},
    )

    if cstt_res.status_code != 200:
        raise SystemExit("CSTT", cstt_res.status_code, cstt_res.reason)

    cstt = cstt_res.text
    print("CSTT", cstt)

    res: requests.Response = session.post(
        url=te_url,
        cookies=cookies,
        data={
            "kind": "reserve",
            "o": ["646946.195", "715608.184"],
            "dates": "20250426",
            "starttime": start_time,
            "endtime": end_time,
            "url": f"https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html#{room_id}",
            "CSTT": cstt,
        },
    )
    print("Reserve", res.status_code, res.reason)
    print_response(res)
