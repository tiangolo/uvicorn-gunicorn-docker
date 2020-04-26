import os
import time
from pathlib import Path

import docker
import requests
from docker.client import DockerClient

from ..utils import (
    CONTAINER_NAME,
    IMAGE_NAME,
    generate_dockerfile_content,
    get_config,
    get_gunicorn_conf_path,
    get_logs,
    get_response_text2,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container: DockerClient, response_text: str) -> None:
    gunicorn_conf_path = get_gunicorn_conf_path(container)
    config_data = get_config(container)
    assert gunicorn_conf_path == "/app/gunicorn_conf.py"
    assert config_data["loglevel"] == "warning"
    assert config_data["workers"] == 3
    assert config_data["bind"] == "0.0.0.0:8000"
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text


def test_package_app_config() -> None:
    name = os.getenv("NAME", "")
    dockerfile_content = generate_dockerfile_content(name)
    dockerfile = "Dockerfile"
    response_text = get_response_text2()
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(client)
    test_path = Path(__file__)
    path = test_path.parent / "package_app_config"
    dockerfile_path = path / dockerfile
    dockerfile_path.write_text(dockerfile_content)
    client.images.build(path=str(path), dockerfile=dockerfile, tag=IMAGE_NAME)
    container = client.containers.run(
        IMAGE_NAME, name=CONTAINER_NAME, ports={"8000": "8000"}, detach=True
    )
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    # Test that everything works after restarting too
    container.start()
    time.sleep(sleep_time)
    verify_container(container, response_text)
    container.stop()
    container.remove()
