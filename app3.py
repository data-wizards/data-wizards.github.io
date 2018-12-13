import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

from plotly import tools
import plotly.plotly as py

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/dogatekin/Project/master/subsetDF.csv')

x = df['Review Score']
X = x[x>0.5]

trace0 = go.Histogram(
    x=df['Sales Rank']
)
trace1 = go.Histogram(
    x=X,
)


fig = tools.make_subplots(rows=1, cols=2, specs=[[{},{}]],
                          shared_xaxes=False, shared_yaxes=False,
                          vertical_spacing=0.001)
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)

fig['layout'].update(height=400, width=800, title='Histogram of the two possible response variables')



app.layout = html.Div([
    dcc.Graph(figure=fig, id='my-figure')
])

if __name__ == '__main__':
    app.run_server(debug=True)
