import streamlit
from generator import Generator

generator_cpu = Generator()
generator_cuda = Generator(device="cuda:0")

input_text = streamlit.text_input("入力してね", value="")

if len(input_text) > 0:
    streamlit.text(f'入力は「{input_text}」です')

    streamlit.text('CPU:')
    result = generator_cpu.generate(input_text)
    streamlit.markdown(result["output"])
    streamlit.text(f'実行時間: {result["time"]:.3f}秒')

    streamlit.text('GPU:')
    result = generator_cuda.generate(input_text)
    streamlit.markdown(result["output"])
    streamlit.text(f'実行時間: {result["time"]:.3f}秒')
