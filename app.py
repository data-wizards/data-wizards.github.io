import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/dogatekin/Project/master/subsetDF.csv')


app.layout = html.Div([
    dcc.Graph(
        id='sales-histogram',
        figure={
            'data': [
                go.Histogram(x=df['Sales Rank'],
                     histnorm='probability')] #also without histnorm

                    #py.iplot(data, filename='normalized histogram')
            ,
            'layout': go.Layout(
                xaxis={'title': 'Bins'},
                yaxis={'title': 'Sales Rank'},
                margin={'l': 50, 'b': 30, 't': 40, 'r': 40},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
