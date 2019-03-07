import time

import docker
import pytest
import requests

from ..utils import CONTAINER_NAME, remove_previous_container, get_logs

client = docker.from_env()


def verify_container(container, response_text):
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert "Uvicorn running on http://0.0.0.0:80" in logs
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text


@pytest.mark.parametrize(
    "image,response_text",
    [
        (
            "tiangolo/uvicorn-gunicorn:python3.6",
            "Hello world! From Uvicorn with Gunicorn. Using Python 3.6",
        ),
        (
            "tiangolo/uvicorn-gunicorn:python3.7",
            "Hello world! From Uvicorn with Gunicorn. Using Python 3.7",
        ),
        (
            "tiangolo/uvicorn-gunicorn:latest",
            "Hello world! From Uvicorn with Gunicorn. Using Python 3.7",
        ),
        (
            "tiangolo/uvicorn-gunicorn:python3.6-alpine3.8",
            "Hello world! From Uvicorn with Gunicorn in Alpine. Using Python 3.6",
        ),
        (
            "tiangolo/uvicorn-gunicorn:python3.7-alpine3.8",
            "Hello world! From Uvicorn with Gunicorn in Alpine. Using Python 3.7",
        ),
    ],
)
def test_env_vars_1(image, response_text):
    remove_previous_container(client)
    container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        environment={"PORT": "8000", "LOG_LEVEL": "warning"},
        ports={"8000": "8000"},
        detach=True,
        command="/start-reload.sh",
    )
    time.sleep(1)
    verify_container(container, response_text)
    container.exec_run(
        "sed -i 's|Uvicorn with Gunicorn|Uvicorn with autoreload|' /app/main.py"
    )
    new_response_text = response_text.replace(
        "Uvicorn with Gunicorn", "Uvicorn with autoreload"
    )
    time.sleep(1)
    verify_container(container, new_response_text)
    container.stop()
    container.remove()
