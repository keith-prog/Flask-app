from flask import request


def test_correct_format(accept_json, client):
    """
    test to ensure we have a list of list and the embeded has 4 items
    """
    resp = client.get("/getdata")
    assert resp.status_code == 200
    assert resp.mimetype == "application/json"
    json = resp.json
    assert isinstance(json, list)
    assert isinstance(json[0], list)  # is this a list in a list
    assert len(json[0]) == 4  # does the emeded list contain 4 items
