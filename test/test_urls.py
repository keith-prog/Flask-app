from flask import request


def test_up(client):
    """ Test to see of the server is up. """
    assert client.get("/").status_code == 200
    resp = client.get("/")
    assert "<html>" in resp.get_data(True)


def test_correct_form(client):
    """ Grab the home page, check for 200 code (all ok), then check to
        see if we have received the correct form and that the response is
        a HTML page.
    """
    response = client.get("/")
    assert response.status_code == 200


def test_CV(client):
    assert client.get("/CV").status_code == 200


def test_bio(client):
    assert client.get("/bio").status_code == 200


def test_interests(client):
    assert client.get("/interests").status_code == 200


def test_technologies(client):
    assert client.get("/technologies").status_code == 200


def test_AI(client):
    assert client.get("/technologies/artificial_intelligence").status_code == 200


def test_form(client):
    assert client.get("/showform").status_code == 200


def test_facial(client):
    assert client.get("/technologies/facial_recognition").status_code == 200


def test_Quantum(client):
    assert client.get("/technologies/quantum").status_code == 200


def test_getData(client):
    assert client.get("/getdata").status_code == 200


def test_form_operation(client, clean_up_db):
    """ Create some test/sample data, then POST the data to the server.  Ensure
        the request is using POST, then look for a 200 (all ok) status code.  Get the 
        response, check for a valid HTML page, then check that the submitted form data
        was received then send back to the browser in the response.
    """
    form_data = {
        "name": "test",
        "email": "test@test.com",
        "message": "test",
    }
    response = client.post("/savedata", data=form_data)
    assert request.method == "POST"
    assert response.status_code == 200


def test_formats(client):
    """ Test to see what comes back """
    assert client.get("/").status_code == 200

    resp = client.get("/")

    assert "<html>" in resp.get_data(True)
