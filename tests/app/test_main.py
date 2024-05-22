from fastapi.testclient import TestClient

from app.main import app


def test_main():
    with TestClient(app) as client:
        url = "https://i.chzbgr.com/full/9340632064/hC25A9707/coding-meme-face-no-one-people-who-use-the-light-ide-theme"
        response = client.post("/url", json={"target_url": url})

        assert response.status_code == 200
        assert "short_url" in response.json()
        short_url = response.json()["short_url"]
        assert len(short_url) == 11

        response = client.get("/{}".format(short_url), follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["Location"] == url

        response = client.post("/url", json={"target_url": url})
        assert response.status_code == 200
        assert "short_url" in response.json()
        short_url_2 = response.json()["short_url"]
        assert short_url == short_url_2

        response = client.get("/non-existing-path", follow_redirects=False)
        assert response.status_code == 404
