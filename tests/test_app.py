import json
import pytest
from app.app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["WORKOUTS"].clear()
    with app.test_client() as c:
        yield c

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}

def test_add_workout_success(client):
    payload = {"workout": "Running", "duration": 30}
    resp = client.post(
        "/workouts",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert resp.status_code == 201
    data = resp.get_json()
    assert "message" in data
    assert data["entry"]["workout"] == "Running"
    assert data["entry"]["duration"] == 30

def test_list_workouts(client):
    client.post(
        "/workouts",
        data=json.dumps({"workout": "Cycling", "duration": 45}),
        content_type="application/json",
    )
    resp = client.get("/workouts")
    assert resp.status_code == 200
    items = resp.get_json()
    assert isinstance(items, list)
    assert len(items) == 1
    assert items[0]["workout"] == "Cycling"
    assert items[0]["duration"] == 45

def test_missing_fields_rejected(client):
    resp = client.post(
        "/workouts",
        data=json.dumps({"workout": "Yoga"}),
        content_type="application/json",
    )
    assert resp.status_code == 400
    assert "Please enter both workout and duration." in resp.get_json()["error"]

    resp = client.post(
        "/workouts",
        data=json.dumps({"workout": "", "duration": 10}),
        content_type="application/json",
    )
    assert resp.status_code == 400
    assert "Please enter both workout and duration." in resp.get_json()["error"]

def test_invalid_duration_rejected(client):
    resp = client.post(
        "/workouts",
        data=json.dumps({"workout": "Stretching", "duration": "abc"}),
        content_type="application/json",
    )
    assert resp.status_code == 400
    assert "Duration must be a number." in resp.get_json()["error"]
