import time

import docker
import pytest

from ..utils import (
    CONTAINER_NAME,
    get_config,
    get_logs,
    get_process_names,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container):
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert "Uvicorn running on http://127.0.0.1:80" in logs


@pytest.mark.parametrize(
    "image",
    [
        ("tiangolo/uvicorn-gunicorn:python3.6"),
        ("tiangolo/uvicorn-gunicorn:python3.7"),
        ("tiangolo/uvicorn-gunicorn:latest"),
        ("tiangolo/uvicorn-gunicorn:python3.6-alpine3.8"),
        ("tiangolo/uvicorn-gunicorn:python3.7-alpine3.8"),
    ],
)
def test_env_vars_2(image):
    remove_previous_container(client)
    container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        environment={"HOST": "127.0.0.1"},
        ports={"80": "8000"},
        detach=True,
        command="/start-reload.sh",
    )
    time.sleep(1)
    verify_container(container)
    container.stop()
    container.remove()
