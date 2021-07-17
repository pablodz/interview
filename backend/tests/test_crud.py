import requests
import json


def test_post_CATAPI():

    url = 'http://0.0.0.0:5000/v1/api'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {
        "catid": "1",
        "catname": "negro"
    }

    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url, headers=headers,
                         json=payload)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()

    # print response full body as text
    print(resp.text)


def test_get_CATAPI():

    url = 'http://0.0.0.0:5000/v1/api'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # convert dict to json string by json.dumps() for body data.
    resp = requests.get(url)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()

    # print response full body as text
    print(resp.text)


def test_put_CATAPI():

    url = 'http://0.0.0.0:5000/v1/api/1'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {
        "catid": "1",
        "catname": "negrito"
    }

    # convert dict to json string by json.dumps() for body data.
    resp = requests.put(url, headers=headers,
                        json=payload)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()

    # print response full body as text
    print(resp.text)


def test_delete_CATAPI():

    url = 'http://0.0.0.0:5000/v1/api/1'

    # convert dict to json string by json.dumps() for body data.
    resp = requests.delete(url)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()

    # print response full body as text
    print(resp.text)
