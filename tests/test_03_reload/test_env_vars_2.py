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
    logs = get_logs(container)
    assert "Checking for script in /app/prestart.sh" in logs
    assert "Running script /app/prestart.sh" in logs
    assert (
        "Running inside /app/prestart.sh, you could add migrations to this file" in logs
    )
    assert "Uvicorn running on http://127.0.0.1:80" in logs


def test_env_vars_2():
    name = os.getenv("NAME")
    image = f"tiangolo/uvicorn-gunicorn:{name}"
    sleep_time = int(os.getenv("SLEEP_TIME", 1))
    time.sleep(sleep_time)
    remove_previous_container(client)
    container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        environment={"HOST": "127.0.0.1"},
        ports={"80": "8000"},
        detach=True,
        command="/start-reload.sh",
    )
    time.sleep(sleep_time)
    verify_container(container)
    container.stop()
    container.remove()
