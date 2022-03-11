import responses
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")


@responses.activate
def test_example():
    """
    GIVEN the /time endpoint
    WHEN I call it
    THEN current time is returned
    """
    endpoint = f'http://localhost:{config["PORT"]}/api/v1/time'
    mocked_value = {'time': 12345.123}

    responses.add(responses.GET, endpoint, json=mocked_value, status=200)
    response = requests.get(endpoint)

    assert mocked_value == response.json()
