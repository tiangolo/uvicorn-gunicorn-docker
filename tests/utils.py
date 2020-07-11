import json
import os
from typing import Any, Dict, Iterator, List

from docker.client import DockerClient
from docker.errors import NotFound
from docker.models.containers import Container

CONTAINER_NAME = "uvicorn-gunicorn-test"
IMAGE_NAME = "uvicorn-gunicorn-testimage"


def get_process_names(container: Container) -> List[Iterator[Any]]:
    return [filter(lambda i: "gunicorn" in i, p) for p in container.top()["Processes"]]


def get_gunicorn_conf_path(container: Container) -> str:
    gunicorn_processes = get_process_names(container)
    first_process = list(gunicorn_processes[0])[0]
    first_part, partition, last_part = first_process.partition("-c")
    return last_part.strip().split()[0]


def get_config(container: Container) -> Dict[str, Any]:
    gunicorn_conf = get_gunicorn_conf_path(container)
    result = container.exec_run(f"python {gunicorn_conf}")
    return json.loads(result.output.decode())


def remove_previous_container(client: DockerClient) -> None:
    try:
        previous = client.containers.get(CONTAINER_NAME)
        previous.stop()
        previous.remove()
    except NotFound:
        return None


def get_logs(container: DockerClient) -> str:
    logs = container.logs()
    return logs.decode("utf-8")


def get_response_text1() -> str:
    python_version = os.getenv("PYTHON_VERSION")
    return f"Hello world! From Uvicorn with Gunicorn. Using Python {python_version}"


def get_response_text2() -> str:
    python_version = os.getenv("PYTHON_VERSION")
    return f"Test app. From Uvicorn with Gunicorn. Using Python {python_version}"


def generate_dockerfile_content(name: str) -> str:
    content = f"FROM tiangolo/uvicorn-gunicorn:{name}\n"
    content += "COPY ./app /app"
    return content
