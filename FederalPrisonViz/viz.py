import plotly.graph_objects as go
import pandas as pd

state_data = pd.read_csv('UpdatedStateData.csv')
prison_data = pd.read_csv('UpdatedPrisonDataWithGeo.csv')
prison_data = prison_data.sort_values(by = 'Inmates Positive', ascending=True)
prison_data = prison_data.loc[(prison_data['Inmates Positive'] >= 5) | (prison_data['State'] == 'NY')]

choro = go.Choropleth(
    locations=state_data['Code'],
    z = state_data['Cases'].astype(int),
    locationmode = 'USA-states', 
    colorscale=[
        # [0, '#BFAA00'],
        # [0.05, '#BFAA00'],
        
        # [0.05, '#C29904'],
        # [0.1, '#C29904'],
        
        # [0.1, '#C68808'],
        # [0.2, '#C68808'],
        
        # [0.2, '#CA770C'], 
        # [0.3, '#CA770C'],

        # [0.3, '#CE6610'],
        # [0.4, '#CE6610'],

        # [0.5, '#D25514'],
        # [0.6, '#D25514'],

        # [0.7, '#D54418'],
        # [0.8, '#D54418'],

        # [0.8, '#D9331C'],
        # [0.9, '#D9331C'],

        # [0.9, '#E50028'],
        # [1, '#E50028']

        [0, '#DD8D27'],
        [0.025, '#DD8D27'],

        [0.025, '#DD8527'],
        [0.05, '#DD8527'],
        
        [0.05, '#DE6D27'],
        [0.1, '#DE6D27'],
        
        [0.1, '#DF5E27'],
        [0.2, '#DF5E27'],
        
        [0.2, '#E04E27'], 
        [0.3, '#E04E27'],

        [0.3, '#E13E27'],
        [0.4, '#E13E27'],

        [0.5, '#E22F27'],
        [0.6, '#E22F27'],

        [0.7, '#E31F27'],
        [0.8, '#E31F27'],

        [0.8, '#E40F27'],
        [0.9, '#E40F27'],

        [0.9, '#E50028'],
        [1, '#E50028']
    ],
    colorbar_title = 'Thousands People',
    zauto=False,
    name='',
)

scatter = go.Scattergeo(
    lat=prison_data['Latitude'],
    lon=prison_data['Longitude'],
    text=prison_data['Facility'] + '<br>' + 'Inmates Positive: ' + prison_data['Inmates Positive'].astype(str),
    mode='markers',
    marker=dict(size=12, color=prison_data['Inmates Positive'], colorscale='Blues'),
    name=''
)

fig = go.Figure(data=[choro, scatter],) 
fig.update_layout(title='Coronavirus Cases in States vs Federal Prisons', title_x=0.5, geo_scope='usa') 
fig.show()