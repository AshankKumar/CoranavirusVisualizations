import plotly.graph_objects as go
import pandas as pd

# def sort_geocord(data):
#     #Create list of pair of rows to swap
#     #then swaps them
#     duplicate_cities = data.duplicated(['Cities'], keep=False)



# def swap_pd_rows(rows_to_swap):
#     #takes a list of pairs of rows to swap and 
#     #swaps them



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

        [0, 'red'],
        [0.05, 'red'],
        [0.05, 'blue'],
        [0.1, 'blue'],
        [0.1, 'green'],
        [0.2, 'green'],
        [0.2, 'orange'],
        [1, 'orange']
    ],
    colorbar_title = 'Thousands People',
    zauto=False,
    # zmax=int(state_data['Cases'].max()),
    # zmin=int(state_data['Cases'].median())
    # zmax=int(state_data['Cases'].max()),
    # zmin=int(state_data['Cases'].min()),
    # zmid=int(state_data['Cases'].median())
)

scatter = go.Scattergeo(
    lat=prison_data['Latitude'],
    lon=prison_data['Longitude'],
    text=prison_data['Inmates Positive'],
    mode='markers',
    marker=dict(size=12, color=prison_data['Inmates Positive'], colorscale='Reds') #Need to add colorscale trace for scatters
)

fig = go.Figure(data=[choro, ],) #scatter
fig.update_layout(geo_scope='usa') 
fig.show()