import torch
from transformers import T5Tokenizer, AutoModelForCausalLM

class Generator():
    def __init__(self) -> None:
        pretrained = "rinna/japanese-gpt2-xsmall"
        self.tokenizer = T5Tokenizer.from_pretrained(pretrained)
        self.model = AutoModelForCausalLM.from_pretrained(pretrained)

    def generate(self, input_text: str, max_length: int=200):
        token_ids = self.tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt")

        with torch.no_grad():
            output_ids = self.model.generate(
                token_ids.to(self.model.device),
                max_length=max_length,
                do_sample=True,
                top_k=500,
                top_p=0.95,
                pad_token_id=self.tokenizer.pad_token_id,
                bos_token_id=self.tokenizer.bos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                bad_word_ids=[[self.tokenizer.unk_token_id]]
            )
        return self.tokenizer.decode(output_ids.tolist()[0])
