FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install

# モデルのダウンロード
ENV DOWNLOAD_REPO_ID="rinna/japanese-gpt2-xsmall"
ENV DOWNLOAD_PATH="~/model"
COPY src/download.py ./
RUN poetry run python download.py

COPY src/ ./src/

ENV TRANSFORMERS_OFFLINE=1
ENV HF_HUB_OFFLINE=1

# see https://cloud.google.com/run/docs/issues#home
CMD HOME=/root poetry run streamlit run src/gpt_container/streamlit.py --server.address 0.0.0.0 --server.port $PORT
