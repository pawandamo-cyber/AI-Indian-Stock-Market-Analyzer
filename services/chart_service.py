import plotly.graph_objects as go

def get_stock_chart(symbol, period="6mo"):

    print("*********** NEW CHART SERVICE LOADED ***********")

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=["A", "B", "C"],
            y=[100, 200, 150],
            name="TEST BAR"
        )
    )

    fig.update_layout(
        title="THIS IS A TEST CHART",
        height=500
    )

    return fig