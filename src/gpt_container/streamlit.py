import streamlit

input_text = streamlit.text_input("入力してね", value="")

streamlit.text(f'入力は「{input_text}」です')
