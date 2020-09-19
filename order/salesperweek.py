import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go 
from plotly.subplots import make_subplots

from data.datafile import sales_week
week = sales_week()

fig = make_subplots(rows=4, cols=1,shared_xaxes=True)
fig.add_trace(go.Scatter(x=week.index, y=week['Sales14'],mode='lines+markers',
                         name='2014',marker_color='blue'), row=1, col=1)
fig.add_trace(go.Scatter(x=week.index, y=week['Sales15'],mode='lines+markers',
                         name='2015',marker_color='green'), row=2, col=1)
fig.add_trace(go.Scatter(x=week.index, y=week['Sales16'],mode='lines+markers',
                         name='2016',marker_color='red'), row=3, col=1)
fig.add_trace(go.Scatter(x=week.index, y=week['Sales17'],mode='lines+markers',
                         name='2017',marker_color='navy'), row=4, col=1)
fig.update_layout(template='simple_white',height = 1000,
                   title='Sales per Week')

layout = html.Div([
        html.H1(children='Sales per Week'), 
        html.H6(children='Visualising sales per week of different year'), 
        dcc.Graph(id='dist-chart', figure=fig)],
        style={'color': 'navy', 'textAlign': 'center'})