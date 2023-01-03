from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd

mode = 'Regresja'
df = pd.read_csv('./winequelity.csv');


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead([
            html.Tr([html.Th(col) for col in dataframe.columns])
        ]),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ]);


app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Hello dash'),
    generate_table(df, 10),
    html.Div([dcc.Dropdown(id='dropdown', options=[
        {
            "label": "Regresja",
            "value": "Regresja",
        },
        {
            "label": "Klasyfikacja",
            "value": "Klasyfikacja",
        }
    ])]),
    html.Div([
        dcc.Dropdown(id='column-names-dropdown', options=[{
            "label": col,
            "value": col
        } for col in df.columns])
    ]),
    html.Div(id='graph-container')
])


def on_value_selected(value, main_column_name):
    def get_dummies_col(dataframe, sep=","):
        dataframe["dummies"] = [sep.join([item for item in row if isinstance(item, str)]) for row in
                                dataframe.itertuples(index=False)]
        return dataframe.replace({"dummies": {"": "None/NA", "None": "None/NA"}})

    result_dataframe = df[[main_column_name, value]]
    result_dataframe = get_dummies_col(result_dataframe)
    dummies = result_dataframe["dummies"].str.get_dummies(sep=",")
    grouped_result = dummies.join(df[value]).groupby([df[value].name]).sum()

    grouped_result.index.rename(value, inplace=True)
    fig = px.imshow(grouped_result, title=f"Heatmap of {main_column_name} per {value}")

    return [
        dcc.Graph(id='graph', figure=fig)
    ]


@app.callback(
    Output('graph-container', 'children'),
    Input('dropdown', 'value'),
    Input('column-names-dropdown', 'value')
)
def on_regression_dropdown_selection(graph_type, column_name):
    return on_value_selected(column_name, 'target' if graph_type == 'Regresja' else 'pH')


if __name__ == '__main__':
    app.run_server(dev_tools_hot_reload=True, debug=True)
