FROM --platform=linux/amd64 fnndsc/ubuntu-python3:ubuntu20.04-python3.8.5

LABEL maintainer="Kevin Mahoney <kevin@mandolin.com>"

RUN apt-get update && \
    apt-get -yqq dist-upgrade && \
    pip install --no-cache-dir "uvicorn[standard]" gunicorn

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Unset python3 entrypoint from base image.
ENTRYPOINT [""]

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]
