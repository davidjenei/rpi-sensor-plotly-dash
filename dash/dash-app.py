import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import sqlite3
from datetime import datetime as dt
from datetime import timedelta as delta

from flask import Flask
server = Flask(__name__)

server.secret_key = os.environ.get('secret_key', 'secret')
db = os.environ.get('SQLITE_DB', 'temp.db')

con = sqlite3.connect(db, check_same_thread=False)

app = dash.Dash('app', server=server)

dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

app.layout = html.Div([
    html.H1('Sensors'),
    html.Div([
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Légnyomás', 'value': 'Legnyomas'},
                {'label': 'Páratartalom', 'value': 'Paratartalom'},
                {'label': 'Erkély', 'value': 'Erkely'},
                {'label': 'Anett szoba', 'value': 'Anett szoba'},
                {'label': 'Nappali', 'value': 'Nappali'},
                {'label': 'PIR', 'value': 'PIR'},
                {'label': 'BME280', 'value': 'BME280'}
            ],
            value='Nappali'
        ),
        dcc.DatePickerRange(
            id='my-date',
            start_date_placeholder_text="Start Period",
            display_format='YYYY-MM-DD',
            start_date=dt.today() + delta(-30),
            end_date=dt.today(),
            end_date_placeholder_text="End Period",
            calendar_orientation='vertical',
        )
    ]),
    dcc.Loading(
        id="my-loading",
        children=[dcc.Graph(id='my-graph')],
        type="default"
    )
], className="container")


@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value'),
               Input('my-date', 'start_date'),
               Input('my-date', 'end_date')])
def update_graph(selected_dropdown_value, start, end):
    df = pd.read_sql_query(
        "SELECT * FROM adatok WHERE ido > datetime('{}') AND ido < datetime('{}')".format(start, end), con)
    dff = df[df['homero'] == selected_dropdown_value]
    return {
        'data': [{
            'x': dff.ido,
            'y': dff.fok,
            'line': {
                'width': 3,
                'shape': 'line'
            }
        }],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            }
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=40080, host='0.0.0.0')

