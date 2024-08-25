import time
from os import environ
from pathlib import Path

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class Generator():
    def __init__(self, device="cpu") -> None:
        pretrained = Path(environ["DOWNLOAD_PATH"]).expanduser()
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained)
        self.model = AutoModelForCausalLM.from_pretrained(pretrained)
        self.model = self.model.to(device)

    def generate(self, input_text: str):
        token_ids = self.tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt")

        start = time.time()
        with torch.no_grad():
            output_ids = self.model.generate(
                token_ids.to(self.model.device),
                max_new_tokens=128,
                repetition_penalty=1.1,
            )
        end = time.time()
        return {
            "output": self.tokenizer.decode(output_ids.tolist()[0], skip_special_tokens=True),
            "time": end - start
        }
