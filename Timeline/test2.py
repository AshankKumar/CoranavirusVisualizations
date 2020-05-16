import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# data = pd.read_csv('today.csv')
# data = data.loc[(data['state'] != 'Guam') & (data['state'] != 'District of Columbia') & (data['state'] != 'Northern Mariana Islands') & (data['state'] != 'Puerto Rico') & (data['state'] != 'Virgin Islands')]

data = pd.read_csv('testdata.csv')

# choro = go.Choroplethmapbox(
#     locations=data['fips'],
#     z=data['cases'].astype(int),
#     # locationmode ='USA-states',
#     colorscale='Reds'
# )

scatter = go.Scattermapbox(
    lat = data['Latitude'],
    lon = data['Longitude'],
    # color = data['Inmates Positive'],
    # colorscale='Reds'
)

layout = go.Layout(mapbox=dict(accesstoken='pk.eyJ1IjoiYXNoMDk0OSIsImEiOiJjazlraGVnaWgwNDVqM2VubjdmcDB2cGY2In0.zWvDiP833xIAM0-d2L0X-w'))
fig = go.Figure(data=[scatter], layout=layout)
fig.show()


