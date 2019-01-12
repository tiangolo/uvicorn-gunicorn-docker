import time

import docker
import pytest
import requests

from ..utils import CONTAINER_NAME, get_config, stop_previous_container

client = docker.from_env()


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
def test_env_bind(image, response_text):
    stop_previous_container(client)
    container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        environment={"BIND": "0.0.0.0:8080", "HOST": "127.0.0.1", "PORT": "9000"},
        ports={"8080": "8000"},
        detach=True,
    )
    config_data = get_config(container)
    assert config_data["host"] == "127.0.0.1"
    assert config_data["port"] == "9000"
    assert config_data["bind"] == "0.0.0.0:8080"
    time.sleep(1)
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text
    container.stop()
    container.remove()
