from requests import Response


def print_response(response: Response):
    print("Request:")
    for key, value in response.request.headers.items():
        print(f"{key}: {value}")
    print(response.request.body)

    print("Response:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
