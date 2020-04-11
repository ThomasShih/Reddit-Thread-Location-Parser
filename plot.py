import plotly.graph_objects as go

def plot(df):
    print(df)
    fig = go.Figure(data=go.Scattergeo(
        lon = df['lon'],
        lat = df['lat'],
        text = df['display_name'],
        mode = 'markers',
        marker_color = 'black',
        ))
    fig.show()