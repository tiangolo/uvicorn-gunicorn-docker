[![Build Status](https://travis-ci.org/tiangolo/uvicorn-gunicorn-docker.svg?branch=master)](https://travis-ci.org/tiangolo/uvicorn-gunicorn-docker)

## Supported tags and respective `Dockerfile` links

* [`python3.7`, `latest` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/python3.7/Dockerfile)
* [`python3.6` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/python3.6/Dockerfile)
* [`python3.6-alpine3.8` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/python3.6-alpine3.8/Dockerfile)
* [`python3.7-alpine3.8` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/python3.7-alpine3.8/Dockerfile)

# uvicorn-gunicorn

**Docker** image with **Uvicorn** managed by **Gunicorn** for high-performance web applications in **Python 3.7** and **Python 3.6** in a single container with auto-tuning. Optionally with Alpine Linux.


## Description

This [**Docker**](https://www.docker.com/) image allows you to create [**Python**](https://www.python.org/) web applications that run with [**Uvicorn**](https://www.uvicorn.org/) and [**Gunicorn**](https://gunicorn.org/) in a single container.

Python web applications running with **Uvicorn** (using the "ASGI" specification) have shown to have [some of the best performances in third-party benchmarks](https://www.techempower.com/benchmarks/#section=test&runid=a979de55-980d-4721-a46f-77298b3f3923&hw=ph&test=fortune&l=zijzen-7). On par with **Go** and **Node.js** (in many cases, showing superior performance).

**Uvicorn** is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process. You can use **Gunicorn** to manage it and run multiple of these concurrent processes. That way, you get the best of concurrency and parallelism.

This image has an "auto-tuning" system included, so that you can just add your code and get a very **high performance** automatically.

The image will set a sensible configuration based on the server it is running on (and the amount of CPU cores available) without making sacrifices.

It has sensible defaults, but you can configure it with environment variables or override the configuration files.

There is also an Alpine version. If you want it, use one of the Alpine tags from above.

This image was created to be the base image for [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker) and [**tiangolo/uvicorn-gunicorn-fastapi**](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) but could be used as the base image to run any Python web application that uses the ASGI specification.

If you are creating a new [**Starlette**](https://www.starlette.io/) web application you should use [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker) instead.

If you are creating a new [**FastAPI**](https://fastapi.tiangolo.com/) web application you should use [**tiangolo/uvicorn-gunicorn-fastapi**](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) instead.

**Note**: Unless you are doing something more technically advanced, you probably should be using [**Starlette**](https://www.starlette.io/) with [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker) or [**FastAPI**](https://fastapi.tiangolo.com/) with [**tiangolo/uvicorn-gunicorn-fastapi**](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker).


**GitHub repo**: <https://github.com/tiangolo/uvicorn-gunicorn-docker>

**Docker Hub image**: <https://hub.docker.com/r/tiangolo/uvicorn-gunicorn/>

## How to use

* You shouldn't have to clone the GitHub repo. You should use it as a base image for other images, using this in your `Dockerfile`:

```Dockerfile
FROM tiangolo/uvicorn-gunicorn:python3.7

COPY ./app /app
```

* It will expect a file at `/app/app/main.py`, or a file at `/app/main.py`. And will expect that file to contain a variable `app` with your "ASGI" application.

## Advanced usage

### Environment variables

These are the environment variables that you can set in the container to configure it and their default values:

* `MODULE_NAME`: the Python "module" (file) to be imported by Gunicorn, this module would contain the actual application in a variable. By default:
    * `app.main` if there's a file `/app/app/main.py` or
    * `main` if there's a file `/app/main.py`
* `VARIABLE_NAME`: the variable inside of the Python module that contains the ASGI application. By default:
    * `app`
* `APP_MODULE`: the string with the Python module and the variable name passed to Gunicorn. By default, set based on the variables `MODULE_NAME` and `VARIABLE_NAME`:
        * `app.main:app` or
        * `main:app`
* `GUNICORN_CONF`: the path to a Gunicorn Python configuration file. By default:
    * `/app/gunicorn_conf.py` if it exists
    * `/app/app/gunicorn_conf.py` if it exists
    * `/gunicorn_conf.py` (the included default)
* `WORKERS_PER_CORE`: this image will check how many CPU cores are available in the current server running your application. It will set the number of workers to the CPU cores times this value. By default:
    * `2`
* `WEB_CONCURRENCY`: override the automatic definition of number of workers. By default:
    * set to the number of CPU cores in the current server times the variable `WORKERS_PER_CORE`, so, in a server with 2 cores, by default it will be set to `4`.
* `HOST`: the host used by Gunicorn. It is the host inside of the container. So, for example, if you set this variable to `127.0.0.1`, it will only be available inside the container, not in the host running it. It's is provided for completeness, but you probably shouldn't change it. By default:
    * `0.0.0.0`
* `PORT`: The port the container should listen on. If you are running your container in a restrictive environment that forces you to use some specific ports (like `8080`) you can set it with this variable. By default:
    * `80`
* `BIND`: The host and port passed to Gunicorn. By default, set based on the variables `HOST` and `PORT`. So, if you didn't change anything, it will be set to:
    * `0.0.0.0:80`
* `LOG_LEVEL`: the log level for Gunicorn. One of:
    * `debug`
    * `info`
    * `warning`
    * `error`
    * `critical`
    * Set to `info` by default. If you need to squeeze more performance sacrificing logging, set it to `warning`.

## License

This project is licensed under the terms of the MIT license.
