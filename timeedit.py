import re
from requests.models import Response


from urllib.parse import quote
import requests


def print_response(response: requests.Response):
    print("Request:")
    for key, value in response.request.headers.items():
        print(f"{key}: {value}")
    print(response.request.body)

    print("Response:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")


toggle = True
if toggle:
    te_url = "https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html"

    TEliuweb = "dd7b1bd4c8044ea55065412b958be3807862900925721832381"

    cookies = {
        "sso-parameters": "back=https%3A%2F%2Fcloud.timeedit.net%2Fliu%2Fweb%2Fwr_stud%2F",
        "ssoserver": "liu_stud_saml2",
        "TEliuweb": TEliuweb,
    }

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

    res: Response = requests.post(
        url=te_url,
        cookies=cookies,
        headers={
            "Host": "cloud.timeedit.net",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://cloud.timeedit.net",
            "Connection": "keep-alive",
            "Referer": "https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        },
        data={
            "kind": "reserve",
            "nocache": 4,
            "l": "sv_SE",
            "o": ["646946.195", "715608.184"],
            "aos": "",
            "dates": "20250426",
            "starttime": "11:15",
            "endtime": "12:00",
            "url": "https://cloud.timeedit.net/liu/web/wr_stud/ri1Q8.html#00646946",
            "fe7": "",
            "CSTT": cstt,
        },
    )
    print("Reserve", res.status_code, res.reason)
    print_response(res)
