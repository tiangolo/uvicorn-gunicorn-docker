import os
import time

import docker

from ..utils import (
    CONTAINER_NAME,
    get_config,
    get_logs,
    get_process_names,
    remove_previous_container,
)

client = docker.from_env()


def verify_container(container):
    process_names = get_process_names(container)
    config_data = get_config(container)
    assert config_data["workers"] == 1
    assert len(process_names) == 2  # Manager + worker
    assert config_data["host"] == "127.0.0.1"
    assert config_data["port"] == "80"
    assert config_data["loglevel"] == "info"
    assert config_data["bind"] == "127.0.0.1:80"
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )


def test_env_vars_2():
    name = os.getenv("NAME")
    image = f"tiangolo/uvicorn-gunicorn:{name}"
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    remove_previous_container(client)
    container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        environment={"WEB_CONCURRENCY": 1, "HOST": "127.0.0.1"},
        ports={"80": "8000"},
        detach=True,
    )
    time.sleep(sleep_time)
    verify_container(container)
    container.stop()
    # Test that everything works after restarting too
    container.start()
    time.sleep(sleep_time)
    verify_container(container)
    container.stop()
    container.remove()
