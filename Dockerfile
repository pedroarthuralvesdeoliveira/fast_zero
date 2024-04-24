FROM python:3.12
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
RUN chmod +x ./entrypoint.sh
CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app