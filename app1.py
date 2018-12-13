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


app.layout = html.Div([
    dcc.Graph(
        id='review-vs-sales',
        figure={
            'data': [
                go.Scatter(
                    x=X,
                    y=df['Sales Rank'],
                    text=df['Title'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    #name=i
                ) #for i in df.Author.unique()
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
