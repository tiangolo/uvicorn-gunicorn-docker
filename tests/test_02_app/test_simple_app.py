import time
from pathlib import Path, PurePath

import docker
import pytest
import requests

from ..utils import get_config, stop_previous_container

client = docker.from_env()


@pytest.mark.parametrize(
    "dockerfile,response_text",
    [
        (
            "python3.6.dockerfile",
            "Test app. From Uvicorn with Gunicorn. Using Python 3.6",
        ),
        (
            "python3.7.dockerfile",
            "Test app. From Uvicorn with Gunicorn. Using Python 3.7",
        ),
        (
            "latest.dockerfile",
            "Test app. From Uvicorn with Gunicorn. Using Python 3.7",
        ),
        (
            "python3.6-alpine3.8.dockerfile",
            "Test app. From Uvicorn with Gunicorn. Using Python 3.6",
        ),
        (
            "python3.7-alpine3.8.dockerfile",
            "Test app. From Uvicorn with Gunicorn. Using Python 3.7",
        ),
    ],
)
def test_defaults(dockerfile, response_text):
    stop_previous_container(client)
    tag = "uvicorn-gunicorn-testimage"
    test_path: PurePath = Path(__file__)
    path = test_path.parent / "simple_app"
    client.images.build(path=str(path), dockerfile=dockerfile, tag=tag)
    container = client.containers.run(
        tag, name="uvicorn-gunicorn-test", ports={"80": "8000"}, detach=True
    )
    config_data = get_config(container)
    assert config_data["workers_per_core"] == 2
    assert config_data["host"] == "0.0.0.0"
    assert config_data["port"] == "80"
    assert config_data["loglevel"] == "info"
    assert config_data["workers"] > 2
    assert config_data["bind"] == "0.0.0.0:80"
    time.sleep(1)
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text
    container.stop()
    container.remove()
