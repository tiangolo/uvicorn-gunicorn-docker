## DEPRECATED 🚨

This Docker image is now deprecated. There's no need to use it, you can just use Uvicorn with `--workers`. ✨

Read more about it below.

---

[![Test](https://github.com/tiangolo/uvicorn-gunicorn-docker/actions/workflows/test.yml/badge.svg)](https://github.com/tiangolo/uvicorn-gunicorn-docker/actions/workflows/test.yml) [![Deploy](https://github.com/tiangolo/uvicorn-gunicorn-docker/workflows/Deploy/badge.svg)](https://github.com/tiangolo/uvicorn-gunicorn-docker/actions?query=workflow%3ADeploy)

## Supported tags and respective `Dockerfile` links

* [`python3.11`, `latest` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.11.dockerfile)
* [`python3.10`, _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.10.dockerfile)
* [`python3.9`, _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.9.dockerfile)
* [`python3.11-slim` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.11-slim.dockerfile)
* [`python3.10-slim` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.10-slim.dockerfile)
* [`python3.9-slim` _(Dockerfile)_](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.9-slim.dockerfile)

## Deprecated tags

🚨 These tags are no longer supported or maintained, they are removed from the GitHub repository, but the last versions pushed might still be available in Docker Hub if anyone has been pulling them:

* `python3.9-alpine3.14`
* `python3.8`
* `python3.8-slim`
* `python3.8-alpine3.10`
* `python3.7`
* `python3.7-alpine3.8`
* `python3.6`
* `python3.6-alpine3.8`

The last date tags for these versions are:

* `python3.9-alpine3.14-2024-03-11`
* `python3.8-2024-11-02`
* `python3.8-slim-2024-11-02`
* `python3.8-alpine3.10-2024-03-11`
* `python3.7-2024-11-02`
* `python3.7-alpine3.8-2024-03-11`
* `python3.6-2022-11-25`
* `python3.6-alpine3.8-2022-11-25`

---

**Note**: There are [tags for each build date](https://hub.docker.com/r/tiangolo/uvicorn-gunicorn/tags). If you need to "pin" the Docker image version you use, you can select one of those tags. E.g. `tiangolo/uvicorn-gunicorn:python3.11-2024-11-02`.

# uvicorn-gunicorn

[**Docker**](https://www.docker.com/) image with [**Uvicorn**](https://www.uvicorn.org/) managed by [**Gunicorn**](https://gunicorn.org/) for high-performance web applications in **[Python](https://www.python.org/)** with performance auto-tuning.

**GitHub repo**: [https://github.com/tiangolo/uvicorn-gunicorn-docker](https://github.com/tiangolo/uvicorn-gunicorn-docker)

**Docker Hub image**: [https://hub.docker.com/r/tiangolo/uvicorn-gunicorn/](https://hub.docker.com/r/tiangolo/uvicorn-gunicorn/)

## Description

Python web applications running with **Uvicorn** (using the "ASGI" specification for Python asynchronous web applications) have shown to have [some of the best performances, as measured by third-party benchmarks](https://www.techempower.com/benchmarks/#section=test&runid=a979de55-980d-4721-a46f-77298b3f3923&hw=ph&test=fortune&l=zijzen-7).

The achievable performance is on par with (and in many cases superior to) **Go** and **Node.js** frameworks.

This image has an **auto-tuning** mechanism included to start a number of worker processes based on the available CPU cores. That way you can just add your code and get **high performance** automatically, which is useful in **simple deployments**.

## 🚨 WARNING: You Probably Don't Need this Docker Image

You are probably using **Kubernetes** or similar tools. In that case, you probably **don't need this image** (or any other **similar base image**). You are probably better off **building a Docker image from scratch** as explained in the docs for [FastAPI in Containers - Docker: Build a Docker Image for FastAPI](https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes), that same process and ideas could be applied to other ASGI frameworks.

### Cluster Replication

If you have a cluster of machines with **Kubernetes**, Docker Swarm Mode, Nomad, or other similar complex system to manage distributed containers on multiple machines, then you will probably want to **handle replication** at the **cluster level** instead of using a **process manager** (like Gunicorn with Uvicorn workers) in each container, which is what this Docker image does.

In those cases (e.g. using Kubernetes) you would probably want to build a **Docker image from scratch**, installing your dependencies, and running **a single Uvicorn process** instead of this image.

For example, your `Dockerfile` could look like:

```Dockerfile
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

You can read more about this in the [FastAPI documentation about: FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/#replication-number-of-processes) as the same ideas would apply to other ASGI frameworks.

### Multiple Workers

If you definitely want to have multiple workers on a single container, Uvicorn now supports handling subprocesses, including restarting dead ones. So there's no need for Gunicorn to manage multiple workers in a single container.

You could modify the example `Dockerfile` from above, adding the `--workers` option to Uvicorn, like:

```Dockerfile
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]
```

That's all you need. You don't need this Docker image at all. 😅

You can read more about it in the [FastAPI Docs about Deployment with Docker](https://fastapi.tiangolo.com/deployment/docker/).

## Technical Details

Uvicorn didn't have support for managing worker processing including restarting dead workers. But now it does.

Before that, Gunicorn could be used as a process manager, running Uvicorn workers. This added complexity that is no longer necessary.

## Legacy Docs

The rest of this document is kept for historical reasons, but you probably don't need it. 😅

### `tiangolo/uvicorn-gunicorn`

This image will set a sensible configuration based on the server it is running on (the amount of CPU cores available) without making sacrifices.

It has sensible defaults, but you can configure it with environment variables or override the configuration files.

There is also a slim version. If you want one of those, use one of the tags from above.

### Frameworks

This image was created to be the base image for:

* [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker)
* [**tiangolo/uvicorn-gunicorn-fastapi**](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)

But could be used as the base image to run any Python web application that uses the ASGI specification.

If you are creating a new [**Starlette**](https://www.starlette.io/) web application you should use [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker) instead.

If you are creating a new [**FastAPI**](https://fastapi.tiangolo.com/) web application you should use [**tiangolo/uvicorn-gunicorn-fastapi**](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) instead.

**Note**: FastAPI is based on Starlette and adds several features on top of it. Useful for APIs and other cases: data validation, data conversion, documentation with OpenAPI, dependency injection, security/authentication and others.

**Note**: Unless you are doing something more technically advanced, you probably should be using [**Starlette**](https://www.starlette.io/) with [**tiangolo/uvicorn-gunicorn-starlette**](https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker) or [**FastAPI**](https://fastapi.tiangolo.com/) with [**tiangolo/uvicorn-gunicorn-fastapi**](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker).

## How to use

You don't need to clone the GitHub repo.

You can use this image as a base image for other images.

Assuming you have a file `requirements.txt`, you could have a `Dockerfile` like this:

```Dockerfile
FROM tiangolo/uvicorn-gunicorn:python3.11

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
```

It will expect a file at `/app/app/main.py`.

Or otherwise a file at `/app/main.py`.

And will expect it to contain a variable `app` with your "ASGI" application.

Then you can build your image from the directory that has your `Dockerfile`, e.g:

```bash
docker build -t myimage ./
```

* Run a container based on your image:

```bash
docker run -d --name mycontainer -p 80:80 myimage
```

You should be able to check it in your Docker container's URL, for example: http://192.168.99.100/ or http://127.0.0.1/ (or equivalent, using your Docker host).

## Dependencies and packages

You will probably also want to add any dependencies for your app and pin them to a specific version, probably including Uvicorn and Gunicorn.

This way you can make sure your app always works as expected.

You could install packages with `pip` commands in your `Dockerfile`, using a `requirements.txt`, or even using [Poetry](https://python-poetry.org/).

And then you can upgrade those dependencies in a controlled way, running your tests, making sure that everything works, but without breaking your production application if some new version is not compatible.

### Using Poetry

Here's a small example of one of the ways you could install your dependencies making sure you have a pinned version for each package.

Let's say you have a project managed with [Poetry](https://python-poetry.org/), so, you have your package dependencies in a file `pyproject.toml`. And possibly a file `poetry.lock`.

Then you could have a `Dockerfile` using Docker multi-stage building with:

```Dockerfile
FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM tiangolo/uvicorn-gunicorn:python3.11

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
```

That will:

* Install poetry and configure it for running inside of the Docker container.
* Copy your application requirements.
    * Because it uses `./poetry.lock*` (ending with a `*`), it won't crash if that file is not available yet.
* Install the dependencies.
* Then copy your app code.

It's important to copy the app code *after* installing the dependencies, that way you can take advantage of Docker's cache. That way it won't have to install everything from scratch every time you update your application files, only when you add new dependencies.

This also applies for any other way you use to install your dependencies. If you use a `requirements.txt`, copy it alone and install all the dependencies on the top of the `Dockerfile`, and add your app code after it.

## Advanced usage

### Environment variables

These are the environment variables that you can set in the container to configure it and their default values:

#### `MODULE_NAME`

The Python "module" (file) to be imported by Gunicorn, this module would contain the actual application in a variable.

By default:

* `app.main` if there's a file `/app/app/main.py` or
* `main` if there's a file `/app/main.py`

For example, if your main file was at `/app/custom_app/custom_main.py`, you could set it like:

```bash
docker run -d -p 80:80 -e MODULE_NAME="custom_app.custom_main" myimage
```

#### `VARIABLE_NAME`

The variable inside of the Python module that contains the ASGI application.

By default:

* `app`

For example, if your main Python file has something like:

```Python
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def read_root():
    return {"message": "Hello world!"}
```

In this case `api` would be the variable with the "ASGI application". You could set it like:

```bash
docker run -d -p 80:80 -e VARIABLE_NAME="api" myimage
```

#### `APP_MODULE`

The string with the Python module and the variable name passed to Gunicorn.

By default, set based on the variables `MODULE_NAME` and `VARIABLE_NAME`:

* `app.main:app` or
* `main:app`

You can set it like:

```bash
docker run -d -p 80:80 -e APP_MODULE="custom_app.custom_main:api" myimage
```

#### `GUNICORN_CONF`

The path to a Gunicorn Python configuration file.

By default:

* `/app/gunicorn_conf.py` if it exists
* `/app/app/gunicorn_conf.py` if it exists
* `/gunicorn_conf.py` (the included default)

You can set it like:

```bash
docker run -d -p 80:80 -e GUNICORN_CONF="/app/custom_gunicorn_conf.py" myimage
```

You can use the [config file](https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/gunicorn_conf.py) from this image as a starting point for yours.

#### `WORKERS_PER_CORE`

This image will check how many CPU cores are available in the current server running your container.

It will set the number of workers to the number of CPU cores multiplied by this value.

By default:

* `1`

You can set it like:

```bash
docker run -d -p 80:80 -e WORKERS_PER_CORE="3" myimage
```

If you used the value `3` in a server with 2 CPU cores, it would run 6 worker processes.

You can use floating point values too.

So, for example, if you have a big server (let's say, with 8 CPU cores) running several applications, and you have an ASGI application that you know won't need high performance. And you don't want to waste server resources. You could make it use `0.5` workers per CPU core. For example:

```bash
docker run -d -p 80:80 -e WORKERS_PER_CORE="0.5" myimage
```

In a server with 8 CPU cores, this would make it start only 4 worker processes.

**Note**: By default, if `WORKERS_PER_CORE` is `1` and the server has only 1 CPU core, instead of starting 1 single worker, it will start 2. This is to avoid bad performance and blocking applications (server application) on small machines (server machine/cloud/etc). This can be overridden using `WEB_CONCURRENCY`.

#### `MAX_WORKERS`

Set the maximum number of workers to use.

You can use it to let the image compute the number of workers automatically but making sure it's limited to a maximum.

This can be useful, for example, if each worker uses a database connection and your database has a maximum limit of open connections.

By default it's not set, meaning that it's unlimited.

You can set it like:

```bash
docker run -d -p 80:80 -e MAX_WORKERS="24" myimage
```

This would make the image start at most 24 workers, independent of how many CPU cores are available in the server.

#### `WEB_CONCURRENCY`

Override the automatic definition of number of workers.

By default:

* Set to the number of CPU cores in the current server multiplied by the environment variable `WORKERS_PER_CORE`. So, in a server with 2 cores, by default it will be set to `2`.

You can set it like:

```bash
docker run -d -p 80:80 -e WEB_CONCURRENCY="2" myimage
```

This would make the image start 2 worker processes, independent of how many CPU cores are available in the server.

#### `HOST`

The "host" used by Gunicorn, the IP where Gunicorn will listen for requests.

It is the host inside of the container.

So, for example, if you set this variable to `127.0.0.1`, it will only be available inside the container, not in the host running it.

It's is provided for completeness, but you probably shouldn't change it.

By default:

* `0.0.0.0`

#### `PORT`

The port the container should listen on.

If you are running your container in a restrictive environment that forces you to use some specific port (like `8080`) you can set it with this variable.

By default:

* `80`

You can set it like:

```bash
docker run -d -p 80:8080 -e PORT="8080" myimage
```

#### `BIND`

The actual host and port passed to Gunicorn.

By default, set based on the variables `HOST` and `PORT`.

So, if you didn't change anything, it will be set by default to:

* `0.0.0.0:80`

You can set it like:

```bash
docker run -d -p 80:8080 -e BIND="0.0.0.0:8080" myimage
```

#### `LOG_LEVEL`

The log level for Gunicorn.

One of:

* `debug`
* `info`
* `warning`
* `error`
* `critical`

By default, set to `info`.

If you need to squeeze more performance sacrificing logging, set it to `warning`, for example:

You can set it like:

```bash
docker run -d -p 80:8080 -e LOG_LEVEL="warning" myimage
```

#### `WORKER_CLASS`

The class to be used by Gunicorn for the workers.

By default, set to `uvicorn.workers.UvicornWorker`.

The fact that it uses Uvicorn is what allows using ASGI applications like FastAPI and Starlette, and that is also what provides the maximum performance.

You probably shouldn't change it.

But if for some reason you need to use the alternative Uvicorn worker: `uvicorn.workers.UvicornH11Worker` you can set it with this environment variable.

You can set it like:

```bash
docker run -d -p 80:8080 -e WORKER_CLASS="uvicorn.workers.UvicornH11Worker" myimage
```

#### `TIMEOUT`

Workers silent for more than this many seconds are killed and restarted.

Read more about it in the [Gunicorn docs: timeout](https://docs.gunicorn.org/en/stable/settings.html#timeout).

By default, set to `120`.

Notice that Uvicorn and ASGI frameworks like FastAPI and Starlette are async, not sync. So it's probably safe to have higher timeouts than for sync workers.

You can set it like:

```bash
docker run -d -p 80:8080 -e TIMEOUT="20" myimage
```

#### `KEEP_ALIVE`

The number of seconds to wait for requests on a Keep-Alive connection.

Read more about it in the [Gunicorn docs: keepalive](https://docs.gunicorn.org/en/stable/settings.html#keepalive).

By default, set to `2`.

You can set it like:

```bash
docker run -d -p 80:8080 -e KEEP_ALIVE="20" myimage
```

#### `GRACEFUL_TIMEOUT`

Timeout for graceful workers restart.

Read more about it in the [Gunicorn docs: graceful-timeout](https://docs.gunicorn.org/en/stable/settings.html#graceful-timeout).

By default, set to `120`.

You can set it like:

```bash
docker run -d -p 80:8080 -e GRACEFUL_TIMEOUT="20" myimage
```

#### `ACCESS_LOG`

The access log file to write to.

By default `"-"`, which means stdout (print in the Docker logs).

If you want to disable `ACCESS_LOG`, set it to an empty value.

For example, you could disable it with:

```bash
docker run -d -p 80:8080 -e ACCESS_LOG= myimage
```

#### `ERROR_LOG`

The error log file to write to.

By default `"-"`, which means stderr (print in the Docker logs).

If you want to disable `ERROR_LOG`, set it to an empty value.

For example, you could disable it with:

```bash
docker run -d -p 80:8080 -e ERROR_LOG= myimage
```

#### `GUNICORN_CMD_ARGS`

Any additional command line settings for Gunicorn can be passed in the `GUNICORN_CMD_ARGS` environment variable.

Read more about it in the [Gunicorn docs: Settings](https://docs.gunicorn.org/en/stable/settings.html#settings).

These settings will have precedence over the other environment variables and any Gunicorn config file.

For example, if you have a custom TLS/SSL certificate that you want to use, you could copy them to the Docker image or mount them in the container, and set [`--keyfile` and `--certfile`](http://docs.gunicorn.org/en/latest/settings.html#ssl) to the location of the files, for example:

```bash
docker run -d -p 80:8080 -e GUNICORN_CMD_ARGS="--keyfile=/secrets/key.pem --certfile=/secrets/cert.pem" -e PORT=443 myimage
```

**Note**: instead of handling TLS/SSL yourself and configuring it in the container, it's recommended to use a "TLS Termination Proxy" like [Traefik](https://docs.traefik.io/). You can read more about it in the [FastAPI documentation about HTTPS](https://fastapi.tiangolo.com/deployment/#https).

#### `PRE_START_PATH`

The path where to find the pre-start script.

By default, set to `/app/prestart.sh`.

You can set it like:

```bash
docker run -d -p 80:8080 -e PRE_START_PATH="/custom/script.sh" myimage
```

### Custom Gunicorn configuration file

The image includes a default Gunicorn Python config file at `/gunicorn_conf.py`.

It uses the environment variables declared above to set all the configurations.

You can override it by including a file in:

* `/app/gunicorn_conf.py`
* `/app/app/gunicorn_conf.py`
* `/gunicorn_conf.py`

### Custom `/app/prestart.sh`

If you need to run anything before starting the app, you can add a file `prestart.sh` to the directory `/app`. The image will automatically detect and run it before starting everything.

For example, if you want to add Alembic SQL migrations (with SQLALchemy), you could create a `./app/prestart.sh` file in your code directory (that will be copied by your `Dockerfile`) with:

```bash
#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
```

and it would wait 10 seconds to give the database some time to start and then run that `alembic` command.

If you need to run a Python script before starting the app, you could make the `/app/prestart.sh` file run your Python script, with something like:

```bash
#! /usr/bin/env bash

# Run custom Python script before starting
python /app/my_custom_prestart_script.py
```

You can customize the location of the prestart script with the environment variable `PRE_START_PATH` described above.

### Development live reload

The default program that is run is at `/start.sh`. It does everything described above.

There's also a version for development with live auto-reload at:

```bash
/start-reload.sh
```

#### Details

For development, it's useful to be able to mount the contents of the application code inside of the container as a Docker "host volume", to be able to change the code and test it live, without having to build the image every time.

In that case, it's also useful to run the server with live auto-reload, so that it re-starts automatically at every code change.

The additional script `/start-reload.sh` runs Uvicorn alone (without Gunicorn) and in a single process.

It is ideal for development.

#### Usage

For example, instead of running:

```bash
docker run -d -p 80:80 myimage
```

You could run:

```bash
docker run -d -p 80:80 -v $(pwd):/app myimage /start-reload.sh
```

* `-v $(pwd):/app`: means that the directory `$(pwd)` should be mounted as a volume inside of the container at `/app`.
    * `$(pwd)`: runs `pwd` ("print working directory") and puts it as part of the string.
* `/start-reload.sh`: adding something (like `/start-reload.sh`) at the end of the command, replaces the default "command" with this one. In this case, it replaces the default (`/start.sh`) with the development alternative `/start-reload.sh`.

#### Development live reload - Technical Details

As `/start-reload.sh` doesn't run with Gunicorn, any of the configurations you put in a `gunicorn_conf.py` file won't apply.

But these environment variables will work the same as described above:

* `MODULE_NAME`
* `VARIABLE_NAME`
* `APP_MODULE`
* `HOST`
* `PORT`
* `LOG_LEVEL`

## 🚨 Alpine Python Warning

In short: You probably shouldn't use Alpine for Python projects, instead use the `slim` Docker image versions.

---

Do you want more details? Continue reading 👇

Alpine is more useful for other languages where you build a static binary in one Docker image stage (using multi-stage Docker building) and then copy it to a simple Alpine image, and then just execute that binary. For example, using Go.

But for Python, as Alpine doesn't use the standard tooling used for building Python extensions, when installing packages, in many cases Python (`pip`) won't find a precompiled installable package (a "wheel") for Alpine. And after debugging lots of strange errors you will realize that you have to install a lot of extra tooling and build a lot of dependencies just to use some of these common Python packages. 😩

This means that, although the original Alpine image might have been small, you end up with a an image with a size comparable to the size you would have gotten if you had just used a standard Python image (based on Debian), or in some cases even larger. 🤯

And in all those cases, it will take much longer to build, consuming much more resources, building dependencies for longer, and also increasing its carbon footprint, as you are using more CPU time and energy for each build. 🌳

If you want slim Python images, you should instead try and use the `slim` versions that are still based on Debian, but are smaller. 🤓

## Tests

All the image tags, configurations, environment variables and application options are tested.

## Release Notes

### Latest Changes

#### Features

* 👷 Avoid creating unnecessary `*.pyc` files with `PYTHONDONTWRITEBYTECODE=1` and ensure logs are printed immediately with `PYTHONUNBUFFERED=1`. PR [#192](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/192) by [@estebanx64](https://github.com/estebanx64).

#### Refactors

* ♻️ Do not `EXPOSE` ports `80` and `443` by default as they can be customized. PR [#238](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/238) by [@tiangolo](https://github.com/tiangolo).

#### Upgrades

* ⬆ Bump uvicorn[standard] from 0.35.0 to 0.38.0. PR [#265](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/265) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.34.3 to 0.35.0. PR [#256](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/256) by [@dependabot[bot]](https://github.com/apps/dependabot).
* Bump uvicorn[standard] from 0.34.0 to 0.34.3. PR [#255](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/255) by [@dependabot[bot]](https://github.com/apps/dependabot).
* Bump uvicorn[standard] from 0.32.1 to 0.34.0. PR [#250](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/250) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.32.0 to 0.32.1. PR [#249](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/249) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.21.0 to 0.32.0. PR [#244](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/244) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Drop support for Python 3.7 and 3.8. PR [#246](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/246) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump gunicorn from 21.2.0 to 22.0.0. PR [#210](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/210) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump gunicorn from 21.2.0 to 22.0.0 in /docker-images. PR [#209](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/209) by [@dependabot[bot]](https://github.com/apps/dependabot).

#### Docs

* 📝 Deprecate this Docker image, use Uvicorn with `--workers` ✨. PR [#225](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/225) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* ⬆ Bump actions/labeler from 5 to 6. PR [#261](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/261) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 5 to 6. PR [#260](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/260) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update Dependabot config prefix. PR [#257](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/257) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update CI config for labeler. PR [#252](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/252) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add Labeler to CI. PR [#251](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/251) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump tiangolo/latest-changes from 0.3.1 to 0.3.2. PR [#248](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/248) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Remove old unused files. PR [#247](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/247) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump actions/checkout from 4.1.7 to 4.2.2. PR [#245](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/245) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump tiangolo/issue-manager from 0.5.0 to 0.5.1. PR [#239](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/239) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `issue-manager.yml`. PR [#237](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/237) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update `latest-changes` GitHub Action. PR [#236](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/236) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump docker/build-push-action from 5 to 6. PR [#217](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/217) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump gunicorn from 22.0.0 to 23.0.0. PR [#222](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/222) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/checkout from 4.1.0 to 4.1.7. PR [#216](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/216) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump docker/login-action from 1 to 3. PR [#211](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/211) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update issue-manager.yml GitHub Action permissions. PR [#219](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/219) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Bump peter-evans/dockerhub-description from 3 to 4. PR [#203](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/203) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump docker/build-push-action from 2 to 5. PR [#202](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/202) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump tiangolo/issue-manager from 0.4.0 to 0.5.0. PR [#201](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/201) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump docker/setup-buildx-action from 1 to 3. PR [#200](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/200) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/setup-python from 4 to 5. PR [#199](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/199) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Add GitHub templates for discussions and issues, and security policy. PR [#205](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/205) by [@alejsdev](https://github.com/alejsdev).
* 🔧 Update `latest-changes.yml`. PR [#198](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/198) by [@alejsdev](https://github.com/alejsdev).

### 0.8.0

#### Features

* ✨ Add support for multi-arch builds, including support for `arm64` (e.g. Mac M1). PR [#195](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/195) by [@tiangolo](https://github.com/tiangolo).

#### Docs

* 📝 Update test badge in `README.md`. PR [#197](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/197) by [@alejsdev](https://github.com/alejsdev).

#### Refactors

* 🔥 Remove Alpine support. PR [#193](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/193) by [@tiangolo](https://github.com/tiangolo).

#### Upgrades

* ⬆️ Bump gunicorn from 20.1.0 to 21.2.0. PR [#185](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/185) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump uvicorn[standard] from 0.20.0 to 0.21.0. PR [#174](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/174) by [@dependabot[bot]](https://github.com/apps/dependabot).

#### Internal

* ⬆️ Bump actions/checkout from 3.3.0 to 4.1.0. PR [#189](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/189) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update mypy requirement from ^0.991 to ^1.1. PR [#173](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/173) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update black requirement from ^22.10 to ^23.1. PR [#171](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/171) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/checkout from 3.1.0 to 3.3.0. PR [#170](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/170) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update latest changes token. PR [#178](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/178) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action to update Docker Hub description, fix. PR [#168](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/168) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action for Docker Hub description. PR [#167](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/167) by [@tiangolo](https://github.com/tiangolo).

### 0.7.0

The highlights of this release are:

* Support for Python 3.10 and 3.11.
* Deprecation of Python 3.6.
    * The last Python 3.6 image tag was pushed and is available in Docker Hub, but it won't be updated or maintained anymore.
    * The last image with a date tag is `python3.6-2022-11-25`.
* Upgraded versions of all the dependencies.

#### Features

* ✨ Add support for Python 3.11. PR [#159](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/159) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Upgrade Uvicorn version. PR [#161](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/161) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add support for Python 3.10. PR [#99](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/99) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Upgrade Uvicorn to the last version supporting Python 3.6. PR [#155](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/155) by [@tiangolo](https://github.com/tiangolo).
* ✨ Add Python 3.9 and Alpine Python 3.9. PR [#52](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/52) by [@graue70](https://github.com/graue70).
* ⬆️ Install uvicorn[standard] to include uvloop and Gunicorn support. PR [#54](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/54) by [@tiangolo](https://github.com/tiangolo).

#### Breaking Changes

* 🔥 Deprecate and remove Python 3.6. PR [#160](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/160) by [@tiangolo](https://github.com/tiangolo).

#### Docs

* ✏️ Fix typo, delete repeated line in README. PR [#147](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/147) by [@jiyeonseo](https://github.com/jiyeonseo).
* 📝 Add note to discourage Alpine with Python. PR [#96](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/96) by [@tiangolo](https://github.com/tiangolo).
* 📝 Add warning for Kubernetes, when to use this image. PR [#95](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/95) by [@tiangolo](https://github.com/tiangolo).
* ✏️ Fix typo duplicate "Note" in Readme. PR [#92](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/92) by [@tiangolo](https://github.com/tiangolo).
* ✏️ Fix typo (type annotation) in tests. PR [#55](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/55) by [@tiangolo](https://github.com/tiangolo).

#### Internal

* ⬆️ Update mypy requirement from ^0.971 to ^0.991. PR [#166](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/166) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update autoflake requirement from ^1.3.1 to ^2.0.0. PR [#165](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/165) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update black requirement from ^20.8b1 to ^22.10. PR [#164](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/164) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update docker requirement from ^5.0.3 to ^6.0.1. PR [#163](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/163) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Update Dependabot config. PR [#162](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/162) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add scheduled CI every Monday. PR [#158](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/158) by [@tiangolo](https://github.com/tiangolo).
* 👷 Do not run double CI for PRs, run on push only on master. PR [#157](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/157) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action alls-green. PR [#156](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/156) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Update black requirement from ^19.10b0 to ^20.8b1. PR [#87](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/87) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update mypy requirement from ^0.770 to ^0.971. PR [#143](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/143) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update docker requirement from ^4.2.0 to ^5.0.3. PR [#97](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/97) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/setup-python from 1 to 4.1.0. PR [#142](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/142) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update isort requirement from ^4.3.21 to ^5.8.0. PR [#88](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/88) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump tiangolo/issue-manager from 0.2.0 to 0.4.0. PR [#85](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/85) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Update pytest requirement from ^5.4.1 to ^7.0.1. PR [#123](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/123) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆️ Bump actions/checkout from 2 to 3.1.0. PR [#145](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/145) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 📌 Add external dependencies and Dependabot to get automatic upgrade PRs. PR [#84](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/84) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update Latest Changes. PR [#83](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/83) by [@tiangolo](https://github.com/tiangolo).
* 🔥 Remove unused Travis and old GitHub Actions configs. PR [#56](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/56) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action latest-changes, update issue-manager, add funding. PR [#53](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/53) by [@tiangolo](https://github.com/tiangolo).

### 0.6.0

* Add docs about installing and pinning dependencies. PR [#41](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/41).
* Add `slim` version. PR [#40](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/40).
* Remove leftover unneeded config for tests. PR [#39](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/39).
* Add extra configs, tests, and docs for:
    * `WORKER_CLASS`
    * `TIMEOUT`
    * `KEEP_ALIVE`
    * `GRACEFUL_TIMEOUT`
    * `ACCESS_LOG`
    * `ERROR_LOG`
    * `GUNICORN_CMD_ARGS`
    * `MAX_WORKERS`
    * PR [#38](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/38)
* Set up CI using GitHub actions, they provide more free instances, so builds finish faster (4 min vs 9 min). PR [#37](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/37).
* Add support for Python 3.8. PR [#36](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/36).
* Refactor tests to remove custom testing Dockerfiles, generate them during tests. PR [#35](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/35).
* Refactor and simplify build process to reduce code duplication. PR [#34](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/34).
* Disable `pip` cache during installation with `--no-cache-dir`. PR [#13](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/13) by [@pmav99](https://github.com/pmav99).
* Migrate local development from Pipenv to Poetry. PR [#31](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/31).
* Add tests and docs for custom `PRE_START_PATH` env var. PR [#30](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/30).
* Add support for custom `PRE_START_PATH` env var. PR [#12](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/12) by [@mgfinch](https://github.com/mgfinch).

### 0.5.0

* Refactor tests to use env vars and add image tags for each build date, like `tiangolo/uvicorn-gunicorn:python3.7-2019-10-15`. PR [#15](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/15).
* Update Gunicorn worker heartbeat directory to `/dev/shm` to improve performance. PR [#9](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/9) by [@wshayes](https://github.com/wshayes).
* Upgrade Travis. PR [#7](https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/7).

### 0.4.0

* Add support for live auto-reload with an additional custom script `/start-reload.sh`, check the [updated documentation](https://github.com/tiangolo/uvicorn-gunicorn-docker#development-live-reload). PR <a href="https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/6" target="_blank">#6</a>.

### 0.3.0

* Set `WORKERS_PER_CORE` by default to `1`, as it shows to have the best performance on benchmarks.
* Make the default web concurrency, when `WEB_CONCURRENCY` is not set, to a minimum of 2 workers. This is to avoid bad performance and blocking applications (server application) on small machines (server machine/cloud/etc). This can be overridden using `WEB_CONCURRENCY`. This applies for example in the case where `WORKERS_PER_CORE` is set to `1` (the default) and the server has only 1 CPU core. PR <a href="https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/5" target="_blank">#5</a>.

### 0.2.0

* Make `/start.sh` run independently, reading and generating used default environment variables. And remove `/entrypoint.sh` as it doesn't modify anything in the system, only reads environment variables. PR <a href="https://github.com/tiangolo/uvicorn-gunicorn-docker/pull/4" target="_blank">#4</a>.

### 0.1.2

* Whenever this image is built (and each of its tags/versions), trigger a build for the children images (<a href="https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker" target="_blank">FastAPI</a> and <a href="https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker" target="_blank">Starlette</a>).

### 0.1.0

* Add support for `/app/prestart.sh`.

## License

This project is licensed under the terms of the MIT license.
