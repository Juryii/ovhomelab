FROM library/python:3.11-bookworm

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

# install poetry and dependencies
RUN pip install poetry

RUN poetry config virtualenvs.in-project true

WORKDIR /workspace

COPY . /workspace

RUN poetry install