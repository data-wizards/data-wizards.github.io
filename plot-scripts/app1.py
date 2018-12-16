import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py

from numpy import arange,array,ones
from scipy import stats

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/dogatekin/Project/master/subsetDF.csv')

x = df['Review Score']
X = x[x>0.5]

y = df['Sales Rank']
Y = y[x>0.5]

t = df['Title']
T = t[x>0.5]

# Generated linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
line = slope*X+intercept


app.layout = html.Div([
    dcc.Graph(
        id='review-vs-sales',
        figure={
            'data': [
                go.Scatter(
                    x=X,
                    y=Y,
                    text=T,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    #name=i
                ),
                go.Scatter(
                    x=X,
                    y=line,
                    text='$R^2 = 0.7551,\\y = 4184277.8 + -745938.9x$',
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    #name=i
                ),
                go.Annotation(
                    x=4.5,
                    y=14000000,
                    text='$R^2 = 0.4251,\\y = 4184277.8 + -745938.9x$',
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    #name=i
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Review Score'},
                yaxis={'title': 'Sales Rank'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
