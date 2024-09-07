import streamlit
from generator import Generator
import torch

generator_cpu = Generator()
generator_cuda = None

with streamlit.expander("cuda device"):
    if torch.cuda.is_available():
        streamlit.text(f'cuda.get_device_name: {torch.cuda.get_device_name()}')
        streamlit.text(f'cuda.get_device_capability: {torch.cuda.get_device_capability()}')
        streamlit.text(f'cuda.device_count: {torch.cuda.device_count()}')
        streamlit.text(f'cuda.current_device: {torch.cuda.current_device()}')
        cuda_device = f'cuda:{torch.cuda.current_device()}'
        generator_cuda = Generator(device=cuda_device)
    else:
        streamlit.text('no cuda device')

input_text = streamlit.text_input("入力してね", value="")

if len(input_text) > 0:
    streamlit.text(f'入力は「{input_text}」です')

    streamlit.text('CPU:')
    result = generator_cpu.generate(input_text)
    streamlit.markdown(result["output"])
    streamlit.text(f'実行時間: {result["time"]:.3f}秒')

    if generator_cuda is not None:
        streamlit.text('GPU:')
        result = generator_cuda.generate(input_text)
        streamlit.markdown(result["output"])
        streamlit.text(f'実行時間: {result["time"]:.3f}秒')
