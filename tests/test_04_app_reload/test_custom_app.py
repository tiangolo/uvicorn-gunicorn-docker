import os
import time
from pathlib import Path
from typing import Dict

import docker
import pytest
import requests
from docker.models.containers import Container

from ..utils import (
    CONTAINER_NAME,
    IMAGE_NAME,
    generate_dockerfile_content,
    get_logs,
    get_response_text2,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container: Container, response_text: str) -> None:
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
    "environment",
    [
        {"MODULE_NAME": "custom_app.custom_main", "VARIABLE_NAME": "custom_var"},
        {"APP_MODULE": "custom_app.custom_main:custom_var"},
    ],
)
def test_custom_app(environment: Dict[str, str]) -> None:
    name = os.getenv("NAME", "")
    dockerfile_content = generate_dockerfile_content(name)
    dockerfile = "Dockerfile"
    response_text = get_response_text2()
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(client)
    test_path = Path(__file__)
    path = test_path.parent / "custom_app"
    dockerfile_path = path / dockerfile
    dockerfile_path.write_text(dockerfile_content)
    client.images.build(path=str(path), dockerfile=dockerfile, tag=IMAGE_NAME)
    container = client.containers.run(
        IMAGE_NAME,
        name=CONTAINER_NAME,
        environment=environment,
        ports={"80": "8000"},
        detach=True,
        command="/start-reload.sh",
    )
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.exec_run(
        "sed -i 's|Uvicorn with Gunicorn|Uvicorn with autoreload|' /app/custom_app/custom_main.py"
    )
    new_response_text = response_text.replace(
        "Uvicorn with Gunicorn", "Uvicorn with autoreload"
    )
    time.sleep(sleep_time)
    verify_container(container, new_response_text)
    container.stop()
    container.remove()
