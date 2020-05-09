import plotly.graph_objects as go
import pandas as pd

state_data = pd.read_csv('StateData.csv')
prison_data = pd.read_csv('test.csv')

choro = go.Choroplethmapbox(
    locations=state_data['Code'],
    z = state_data['Cases'].astype(int),
    # locationmode = 'USA-states',
    colorscale = 'Reds',
    colorbar_title = 'Thousands People',
)

scatter = go.Scattermapbox(
    lat=prison_data['Latitude'],
    lon=prison_data['Longitude'],
    text=prison_data['Inmates Positive'],
    mode='markers+text',
    marker=dict(size=12, color='rgb(0,0,255)')
)

# layout = go.Layout(mapbox=dict(center=go.layout.mapbox.Center(lat=38, lon=-97), accesstoken='pk.eyJ1IjoiYXNoMDk0OSIsImEiOiJjazlraGVnaWgwNDVqM2VubjdmcDB2cGY2In0.zWvDiP833xIAM0-d2L0X-w', zoom=3))
layout = go.Layout(mapbox=dict(accesstoken='pk.eyJ1IjoiYXNoMDk0OSIsImEiOiJjazlraGVnaWgwNDVqM2VubjdmcDB2cGY2In0.zWvDiP833xIAM0-d2L0X-w'))
fig = go.Figure(data=[choro,],layout=layout)

fig.show()


# fig = go.Figure(data=go.Choropleth(
#     locations=state_data['Code'],
#     z = state_data['Cases'].astype(int),
#     locationmode = 'USA-states',
#     colorscale = 'Reds',
#     colorbar_title = 'Thousands People',
# ))

# fig.update_layout(
#     geo_scope='usa'
# )