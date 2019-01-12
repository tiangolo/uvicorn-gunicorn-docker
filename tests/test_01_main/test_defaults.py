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
def test_defaults(image, response_text):
    stop_previous_container(client)
    container = client.containers.run(
        image, name=CONTAINER_NAME, ports={"80": "8000"}, detach=True
    )
    config_data = get_config(container)
    assert config_data["workers_per_core"] == 2
    assert config_data["host"] == "0.0.0.0"
    assert config_data["port"] == "80"
    assert config_data["loglevel"] == "info"
    assert config_data["workers"] > 2
    assert config_data["bind"] == "0.0.0.0:80"
    time.sleep(1)
    response = requests.get("http://127.0.0.1:8000")
    assert response.text == response_text
    container.stop()
    container.remove()
