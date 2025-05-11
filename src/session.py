from datetime import datetime
from requests.models import Response


from http.cookiejar import MozillaCookieJar
import os
import requests
from requests import Session
from bs4 import BeautifulSoup


def get_session():
    session = requests.session()

    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    }

    cookie_file = "cookies.txt"

    mozilla_cookie_jar: MozillaCookieJar = MozillaCookieJar(filename=cookie_file)

    if not os.path.isfile(cookie_file):
        mozilla_cookie_jar.save(ignore_discard=True, ignore_expires=True)

    mozilla_cookie_jar.load(ignore_discard=True, ignore_expires=True)

    session.cookies.update(  # pyright:ignore[reportUnknownMemberType]
        mozilla_cookie_jar
    )

    authenticate_session(session)

    try:
        session.cookies.clear(domain="")
    except KeyError:
        pass

    for cookie in session.cookies:
        mozilla_cookie_jar.set_cookie(cookie)

    mozilla_cookie_jar.save(ignore_discard=True, ignore_expires=True)

    return session


def get_MSISAuth(session: Session):
    res: Response = session.get(
        "https://cloud.timeedit.net/liu/web/timeedit/sso/liu_stud_saml2?back=https://cloud.timeedit.net/liu/web/wr_stud/"
    )

    soup = BeautifulSoup(res.text, "html.parser")
    tag = soup.select_one("#loginFormPaginated")
    path = tag.get("action") if tag else None
    adfs_url = "https://fs.liu.se" + str(path)

    username = os.getenv("LIU_USERNAME")
    password = os.getenv("LIU_PASSWORD")

    if username == None or password == None:
        raise SystemExit("LIU_USERNAME or LIU_PASSWORD not set")

    res = session.post(
        adfs_url,
        data={
            "UserName": username,
            "Password": password,
            "AuthMethod": "FormsAuthentication",
            "Kmsi": "true",
        },
    )


def authenticate_session(session: Session):
    if session.cookies.get("MSISAuth") == None:
        get_MSISAuth(session)
        if session.cookies.get("MSISAuth") == None:
            raise SystemExit(
                datetime.today().strftime("%Y-%m-%d %H:%M:%S"), "Failed to get MSISAuth"
            )

    res = session.get(
        url="https://cloud.timeedit.net/liu/web/timeedit/sso/liu_stud_saml2?back=https://cloud.timeedit.net/liu/web/wr_stud/"
    )

    soup = BeautifulSoup(res.text, "html.parser")
    tag = soup.select_one('input[name="SAMLResponse"]')
    saml_response = tag.get("value") if tag else None

    sso_res = session.post(
        url="https://cloud.timeedit.net/liu/web/timeedit/ssoResponse/liu_stud_saml2",
        data={"SAMLResponse": saml_response},
    )

    if sso_res.status_code != 200:
        session.cookies.clear("fs.liu.se", "/adfs", "MSISAuth")
        authenticate_session(session)
