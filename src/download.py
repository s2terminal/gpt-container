from os import environ
from pathlib import Path
import shutil
from huggingface_hub import snapshot_download

downloaded_path = snapshot_download(repo_id=environ["DOWNLOAD_REPO_ID"])
model_path = Path(environ["DOWNLOAD_PATH"]).expanduser()

shutil.move(downloaded_path, model_path)
print('moved', downloaded_path, model_path)
