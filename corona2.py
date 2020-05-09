import plotly.graph_objects as go
import pandas as pd

state_data = pd.read_csv('StateData.csv')
# prison_data = pd.read_csv('test.csv')
prison_data = pd.read_csv('test3.csv') #too many overlapping points

choro = go.Choropleth(
    locations=state_data['Code'],
    z = state_data['Cases'].astype(int),
    locationmode = 'USA-states',
    colorscale = 'Blues',
    colorbar_title = 'Thousands People',
)

scatter = go.Scattergeo(
    lat=prison_data['Latitude'],
    lon=prison_data['Longitude'],
    text=prison_data['Inmates Positive'],
    mode='markers',
    marker=dict(size=12, color=prison_data['Inmates Positive'], colorscale='Reds') #Need to add colorscale trace for scatters
)

fig = go.Figure(data=[choro, scatter],)
fig.update_layout(geo_scope='usa') 
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