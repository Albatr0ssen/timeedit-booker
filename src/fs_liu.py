import requests

from src.helpers import print_response


def fs_liu():
    session = requests.session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    }

    MSIS_auth = "AAEAAJxYUX/g2oIp/yyilTQSE2Wa7lWp/FnFvTu6BJPNV9Jm6oOjQgK+sC+OEy/cscoVhHdoY2N4D0FrNqYjyY02vE1bxCAxqMsGBBq9zaftMUfyv2103/SS1QMc51I0pU9BMW1QBhmL4T8XVabe97JVx6Drx+RirzqQpR3HBzJprBftXlurUGix8ehd3RQDa60eiUNk+m5AXfgRcz1dv5fCcETuID8Fq8IKGxI2zbwBTaLC1f/EsrBoz2sGCU2sBBDc7esSZAA0h9Tu92zY4QwWJzcOM2C3+GJ/SbGDDqhSjx3A94T3OYEjq9LER6TXhiZNVVM4+clUVaCwjCe7OOLZUwXFiPyHdFAcR3laWVeo7GMjcZ7e3mgzvaudKKGaGlmsAwABAABgroT7v3fixFOUT8/LRbdJVnBJrcTLpxqMDfr5/aYvYB2D+mhr7W2VjWbNzyGUsjCRY8YHnFAv8iN2VPWJ1b5eSYfJTlkCFB4VSFA+a0vApMmWZBChskgjsweItANrBQrVP1NTt5XFvCRI650Alb3genVE/lcIYj0Mcx4GvlzuX6jPQumNanI5jHZ7hFEaLkHnUK5fWYANEtcZPhBneN7iiNDJm5MRQMiY30zHESSJ0yd+MX0bF16foBjGRmZhCMAsCa+GBDSw1oHd9Hxo5GUzfI1Gvem7olbXkdUYApaJKfgdY7x8xnpJoRwBDCgyys6pgKZR7dEYTzqA168WMp2ScAMAAL5lX5A7R30rwXioM+PeUWsS9RyU1p/+dWJI15HTkesAqrMz+YhRW4RjN2jSKOypGr+v7DgzXY24kPJVDtFrPOUJFhgM3YLgLhqyiExXrx73gHUS0nZY7Yi1516GDzkouAYp3Se7APSTbo14e4Y2jVdz2FgJAPi45jeZLrn4jeGmMAA3ehsUz61rovHVdprVUIbZZCCitrxxGciUQUqRsN1PYUn5xaleIgYqoNG95olo3DwERwpyw1KOA7x9jtFqWjcDRQmq7pVEL3zPB2vuvQdJ2LwRGRQ5Sqp2XTmFMKaGMh9neV/VdMitWxtB7QoAgIbA+5EaEEYWiwMjjumJkwVKDVqPLvjUUCnsm5bWvLP3TWHbJ3D3wgS2zZMAlwMFsJCgxCYj3R+j8W4+dXIZbhI3GY36/r9fYmW4yyulArMc9b23TOBE8g7UL0BgOE49Af7ToJcQwnGUOyQmxg+FBlsbbjlApjWJNU9WF7MQrADSCdvtLchpFmJPyY7N5lSTvqs2l+T2GrmHiNTbSVgqezaS9+H2gxTd9uIFmnvpz4IaWMA4ChBTYN6vCxaC2kUs0HDbvyQFfShYtmHZhDjjEeG+Gg24AfKuJ0G4L7Wv3EPvZZziuy2HQYfhQvRKkmf9RX+C0zlBqcAlZKoHnyo/Q7R/FoN2JLlZUEO6xUuVKWnrQZo3JPuQcYgDhIr5vwf9cf3uiib6UaL1WgDd3fOSVSRc+G+G87jXz7iX2LV0LKFLJEFypIHI0z5UYej3IbnRHZM/ZYiHQZo5xb9iWXeMTrqchFidWuMST5dhEnBa6MVahCMj8voPqwvksLfbiHa7EElqLs+Y4PUYR6JXWlKvCuQex/dFqlGH7X5GO1dsqYpF7ZUAHcnzBHGDZEc797mgHMeevc2wgBfASOaWDUTEiRsGbAoQ49ZligcNyz5QS4itZLivzJ1x0UT1uRc6RotvyB0VGEPkCnlfhblcAl14mgXjj7giz7bE0X6+zpN/9ALXrU/3s3J6wHbk4Rih1IIY2rF9c0AR88j0ANnSrTYTsqnkT/aNff+8MUy5V2KwFvCGrzA7ozjfW04rGPTQlIdb6w4lGsBjqDo6odMaSmV+rrLz5s+zQSppzKgU+QIeLh43xdoAmn+RKUaraFj7ZxcKtbnsch1zFvmtuOGII/g2Kc0="

    _ = session.cookies.set(  # pyright:ignore[reportUnknownMemberType]
        "MSISAuth", MSIS_auth
    )

    res = session.get(
        "https://cloud.timeedit.net/liu/web/timeedit/sso/liu_stud_saml2?back=https%3A%2F%2Fcloud.timeedit.net%2Fliu%2Fweb%2Fwr_stud%2F"
    )
    print("Cookie test", res.status_code, res.reason)
    print_response(res)
    print(res.cookies)
