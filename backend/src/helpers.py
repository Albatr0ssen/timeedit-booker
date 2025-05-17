from requests import Response


def print_response(response: Response):
    print(response.status_code, response.reason)
    print("\nRequest:")
    for key, value in response.request.headers.items():
        print(f"{key}: {value}")
    # print(response.request.body)

    print("\nResponse:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
