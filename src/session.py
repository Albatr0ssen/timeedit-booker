from http.cookiejar import MozillaCookieJar
import os
import requests
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

    if session.cookies.get("MSISAuth") == None:
        msis_auth: str = input("MSISAuth: ")
        _ = session.cookies.set(  # pyright:ignore[reportUnknownMemberType]
            name="MSISAuth", value=msis_auth
        )

    res = session.get(
        url="https://cloud.timeedit.net/liu/web/timeedit/sso/liu_stud_saml2?back=https%3A%2F%2Fcloud.timeedit.net%2Fliu%2Fweb%2Fwr_stud%2F"
    )

    print(res.url)

    soup = BeautifulSoup(res.text, "html.parser")
    tag = soup.select_one('input[name="SAMLResponse"]')
    saml_response = tag.get("value") if tag else None

    _ = session.post(
        url="https://cloud.timeedit.net/liu/web/timeedit/ssoResponse/liu_stud_saml2",
        data={"SAMLResponse": saml_response},
    )

    try:
        session.cookies.clear(domain="")
    except KeyError:
        pass

    for cookie in session.cookies:
        mozilla_cookie_jar.set_cookie(cookie)

    mozilla_cookie_jar.save(ignore_discard=True, ignore_expires=True)

    return session
