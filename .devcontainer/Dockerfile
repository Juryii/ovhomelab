FROM library/python:3.11-bookworm

ARG USER=vscode
ARG DEBIAN_FRONTEND=noninteractive
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG POSTGRES_DB

# Обновление и установка необходимых пакетов
RUN apt update \
    && apt install -y --no-install-recommends sudo git postgresql postgresql-contrib \
    && apt autoremove -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -s /usr/bin/bash ${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD: ALL" >/etc/sudoers.d/${USER} \
    && chmod 0440 /etc/sudoers.d/${USER}

# Установка Poetry
RUN pip install poetry \
    && poetry config virtualenvs.in-project true

# Настройка PostgreSQL
USER postgres
RUN service postgresql start && \
    su postgres -c "psql -c \"CREATE USER ${POSTGRES_USER} WITH PASSWORD '${POSTGRES_PASSWORD}';\"" && \
    su postgres -c "psql -c \"CREATE DATABASE ${POSTGRES_DB} OWNER ${POSTGRES_USER} ;\"" && \
    service postgresql stop
    #psql --command "CREATE USER ${POSTGRES_USER} WITH SUPERUSER PASSWORD '${POSTGRES_PASSWORD}';" && \
    #createdb -O ${POSTGRES_USER} ${POSTGRES_DB}

# Переключение обратно на пользователя vscode
USER ${USER}
WORKDIR /workspace

# Команда для запуска PostgreSQL и веб-сервера Django
CMD sudo service postgresql start && poetry install && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
