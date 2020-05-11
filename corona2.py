import plotly.graph_objects as go
import pandas as pd

state_data = pd.read_csv('StateData.csv')
prison_data = pd.read_csv('test3.csv') #too many overlapping points
prison_data = prison_data.sort_values(by = 'Inmates Positive', ascending=True)
max_state_cases = int(state_data['Cases'].max())
test = 0.1*max_state_cases
choro = go.Choropleth(
    locations=state_data['Code'],
    z = state_data['Cases'].astype(int),
    locationmode = 'USA-states',
    # colorscale = 'ylgnbu', #Portland, #RdBu, #Reds, haline, 
    colorscale=[
        # [0, "rgb(0, 0, 0)"],
        # [0.9, "rgb(200, 100, 100)"],

        # [0, 'red'],
        # [0.05, 'red'],
        # [0.05, 'blue'],
        # [0.1, 'blue'],
        # [0.1, 'green'],
        # [0.2, 'green'],
        # [0.2, 'orange'],
        # [1, 'orange']

        [0, '#BF5900'],
        [0.05, '#AB5C16'],
        [0.05, '#72665B'],
        [0.1, '#4C6C89'],
        [0.1, '#3970A0'],
        [0.2, '#2673B7'],
        [0.2, '#1376CE'],
        [1, '#007AE5']
    ],
    colorbar_title = 'Thousands People',
    zauto=False,
)

scatter = go.Scattergeo(
    lat=prison_data['Latitude'],
    lon=prison_data['Longitude'],
    text=prison_data['Inmates Positive'],
    mode='markers',
    marker=dict(size=12, color=prison_data['Inmates Positive'], colorscale='Reds') #Need to add colorscale trace for scatters
)

fig = go.Figure(data=[choro, scatter],) #scatter
fig.update_layout(geo_scope='usa') 
fig.show()