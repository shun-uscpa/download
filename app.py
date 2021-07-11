import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(prevent_initial_callbacks=True)
server = app.server

app.layout = html.Div(
    [html.Button("Download Text", id="btn_txt"), dcc.Download(id="download-text")]
)


@app.callback(
    Output("download-text", "data"),
    Input("btn_txt", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dict(content="Hello world!", filename="hello.txt")


if __name__ == "__main__":
    app.run_server(debug=True)