ARG VARIANT=3.11-bookworm
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

ENV PYTHONUNBUFFERED 1

ARG USER=vscode
ARG DEBIAN_FRONTEND=noninteractive

# Обновление и установка необходимых пакетов
RUN apt update \
    && apt install -y --no-install-recommends sudo git \
    && apt autoremove -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -s /usr/bin/bash ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/${USER} \
    && chmod 0440 /etc/sudoers.d/${USER}

# Установка Poetry
RUN pip install poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install

# Команда для запуска веб-сервера Django
# CMD poetry install && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
