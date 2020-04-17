import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import App, build_graph
from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/time-series':
        return App()
    else:
        return Homepage()

@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)
def update_graph(city):
    graph = build_graph(city)
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)


