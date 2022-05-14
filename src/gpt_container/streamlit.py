import streamlit
from generator import Generator

generator = Generator()

input_text = streamlit.text_input("入力してね", value="")

if len(input_text) > 0:
    streamlit.text(f'入力は「{input_text}」です')
    streamlit.text(f'出力は')
    generated_text = generator.generate(input_text, 100)
    streamlit.markdown(generated_text)
