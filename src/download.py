from os import environ
from pathlib import Path
from huggingface_hub import snapshot_download

downloaded_path = snapshot_download(
    repo_id=environ["DOWNLOAD_REPO_ID"],
    local_dir=Path(environ["DOWNLOAD_PATH"]).expanduser()
)
