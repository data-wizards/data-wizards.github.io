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

k

Entropy = go.Scatter(
    x=df['Entropy'],
    y=X,
    mode='markers'
)
Brightness = go.Scatter(
    x=df['Brightness'],
    y=X,
    mode='markers'
)
Keypoints = go.Scatter(
    x=df['Keypoints'],
    y=X,
    mode='markers',
    #axis={'title': 'Sales Rank'}
)


fig = tools.make_subplots(rows=1, cols=3, specs=[[{},{},{}]],
                          shared_xaxes=False, shared_yaxes=True,
                          vertical_spacing=0.001)
fig.append_trace(Entropy, 1, 1)
fig.append_trace(Brightness, 1, 2)
fig.append_trace(Keypoints, 1, 3)

fig['layout'].update(height=400, width=800, title='Correlation between Entropy, Brightness, Keypoints and Sales Rank')



app.layout = html.Div([
    dcc.Graph(figure=fig, id='my-figure')
])

if __name__ == '__main__':
    app.run_server(debug=True)
