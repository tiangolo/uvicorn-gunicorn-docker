import os
import time

import docker
import requests
from docker.client import DockerClient

from ..utils import (
    CONTAINER_NAME,
    get_config,
    get_logs,
    get_response_text1,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container: DockerClient, response_text: str) -> None:
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text
    config_data = get_config(container)
    assert config_data["workers_per_core"] == 2
    assert config_data["host"] == "0.0.0.0"
    assert config_data["port"] == "8000"
    assert config_data["loglevel"] == "warning"
    assert config_data["bind"] == "0.0.0.0:8000"
    assert config_data["graceful_timeout"] == 20
    assert config_data["timeout"] == 20
    assert config_data["keepalive"] == 20
    assert config_data["errorlog"] is None
    assert config_data["accesslog"] is None
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert '"GET / HTTP/1.1" 200' not in logs
    assert "[INFO] Application startup complete." not in logs


def test_env_vars_1() -> None:
    name = os.getenv("NAME")
    image = f"tiangolo/uvicorn-gunicorn:{name}"
    response_text = get_response_text1()
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(client)
    container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        environment={
            "WORKERS_PER_CORE": 2,
            "PORT": "8000",
            "LOG_LEVEL": "warning",
            "GRACEFUL_TIMEOUT": "20",
            "TIMEOUT": "20",
            "KEEP_ALIVE": "20",
            "ACCESS_LOG": "",
            "ERROR_LOG": "",
        },
        ports={"8000": "8000"},
        detach=True,
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
