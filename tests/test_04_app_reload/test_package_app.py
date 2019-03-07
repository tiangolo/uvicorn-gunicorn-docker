import time
from pathlib import Path, PurePath

import docker
import pytest
import requests

from ..utils import (
    CONTAINER_NAME,
    IMAGE_NAME,
    get_config,
    get_logs,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container, response_text):
    config_data = get_config(container)
    assert config_data["workers_per_core"] == 1
    assert config_data["host"] == "0.0.0.0"
    assert config_data["port"] == "80"
    assert config_data["loglevel"] == "info"
    assert config_data["workers"] >= 2
    assert config_data["bind"] == "0.0.0.0:80"
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text


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
        ("latest.dockerfile", "Test app. From Uvicorn with Gunicorn. Using Python 3.7"),
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
def test_package_app(dockerfile, response_text):
    remove_previous_container(client)
    test_path: PurePath = Path(__file__)
    path = test_path.parent / "package_app"
    client.images.build(path=str(path), dockerfile=dockerfile, tag=IMAGE_NAME)
    container = client.containers.run(
        IMAGE_NAME, name=CONTAINER_NAME, ports={"80": "8000"}, detach=True
    )
    time.sleep(1)
    verify_container(container, response_text)
    container.stop()
    # Test that everything works after restarting too
    container.start()
    time.sleep(1)
    verify_container(container, response_text)
    container.stop()
    container.remove()
