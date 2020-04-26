import os
import time

import docker
import requests
from docker.client import DockerClient

from ..utils import (
    CONTAINER_NAME,
    get_logs,
    get_response_text1,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container: DockerClient, response_text: str) -> None:
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert "Uvicorn running on http://0.0.0.0:80" in logs
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text


def test_env_vars_1() -> None:
    name = os.getenv("NAME")
    image = f"tiangolo/uvicorn-gunicorn:{name}"
    response_text = get_response_text1()
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(client)
    container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        environment={"PORT": "8000", "LOG_LEVEL": "debug"},
        ports={"8000": "8000"},
        detach=True,
        command="/start-reload.sh",
    )
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.exec_run(
        "sed -i 's|Uvicorn with Gunicorn|Uvicorn with autoreload|' /app/main.py"
    )
    new_response_text = response_text.replace(
        "Uvicorn with Gunicorn", "Uvicorn with autoreload"
    )
    time.sleep(sleep_time)
    verify_container(container, new_response_text)
    container.stop()
    container.remove()
