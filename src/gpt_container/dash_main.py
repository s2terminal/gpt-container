from dash import Dash, dcc, html, Input, Output, State
from os import environ
from generator import Generator

app = Dash(__name__)

app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic', children='入力してね')
])

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    generator = Generator()
    if value is not None and len(value) > 0:
        generated_text = generator.generate(value, 100)
        return generated_text
    return '入力してね'

if __name__ == '__main__':
    # TODO: 環境変数でdebugを受け取るようにしたほうがいい
    app.run_server(host='0.0.0.0', port=environ["PORT"], debug=False)
