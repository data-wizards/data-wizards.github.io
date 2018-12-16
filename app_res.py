import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

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


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df['Brightness'],
                    y=df['UniqueColors'],
                    text=df['Title'],
                    mode='markers',
                    opacity=0.7,
                    marker = dict(
                        size = 15,
                        color=df['Sales Rank'],
                        colorscale='Hot', #earth
                        showscale=True,
                    )
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Brightness'},
                yaxis={'title': 'UniqueColors'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
