from os import environ
from pathlib import Path

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class Generator():
    def __init__(self) -> None:
        pretrained = Path(environ["DOWNLOAD_PATH"]).expanduser()
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained)
        self.model = AutoModelForCausalLM.from_pretrained(pretrained)

    def generate(self, input_text: str, max_length: int=200):
        token_ids = self.tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt")

        with torch.no_grad():
            output_ids = self.model.generate(
                token_ids.to(self.model.device),
                max_length=max_length,
                max_new_tokens=128,
                repetition_penalty=1.1,
            )
        return self.tokenizer.decode(output_ids.tolist()[0])
