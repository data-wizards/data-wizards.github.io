import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

from numpy import arange,array,ones
from scipy import stats

from plotly import tools
import plotly.plotly as py

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/dogatekin/Project/master/subsetDF.csv')

# generate data without 0 as review score
x = df['Review Score']
X = x[x>0.5]

y1 = df['Entropy']
Y1 = y1[x>0.5]

y2 = df['Brightness']
Y2 = y2[x>0.5]

y3 = df['Keypoints']
Y3 = y3[x>0.5]

# Generated linear fit for entropy
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(Y1,X)
line1 = slope1*Y1+intercept1

# Generated linear fit for brightness
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(Y2,X)
line2 = slope2*Y2+intercept2

# Generated linear fit for keypoints
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(Y3,X)
line3 = slope3*Y3+intercept3

Entropy = go.Scatter(
    x=Y1,
    y=X,
    mode='markers'
)
trace1 = go.Scatter(
    x=Y1,
    y=line1,
    mode='lines'
)
Brightness = go.Scatter(
    x=Y2,
    y=X,
    mode='markers'
)
trace2 = go.Scatter(
    x=Y2,
    y=line2,
    mode='lines'
)
Keypoints = go.Scatter(
    x=Y3,
    y=X,
    mode='markers',
    #axis={'title': 'Sales Rank'}
)
trace3 = go.Scatter(
    x=Y3,
    y=line3,
    mode='lines'
)


fig = tools.make_subplots(rows=1, cols=3, specs=[[{},{},{}]],
                          shared_xaxes=False, shared_yaxes=True,
                          vertical_spacing=0.001)
fig.append_trace(Entropy, 1, 1)
fig.append_trace(trace1, 1, 1)
fig.append_trace(Brightness, 1, 2)
fig.append_trace(trace2, 1, 2)
fig.append_trace(Keypoints, 1, 3)
fig.append_trace(trace3, 1, 3)

fig['layout'].update(height=400, width=800, title='Correlation between Entropy, Brightness, Keypoints and Sales Rank')



app.layout = html.Div([
    dcc.Graph(figure=fig, id='my-figure')
])

if __name__ == '__main__':
    app.run_server(debug=True)
