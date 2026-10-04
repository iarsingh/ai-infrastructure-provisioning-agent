from fastapi.testclient import TestClient
from provagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'provision a small env', **{'payload': {'size': 'small'}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert "gke" in payload["modules"]
    refused = client.post("/agent/run", json={"goal": 'apply the plan'}).json()
    assert refused["refused"] is True
