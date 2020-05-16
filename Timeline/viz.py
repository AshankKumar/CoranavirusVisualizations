import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('today.csv')
df = df.loc[(df['state'] != 'Guam') & (df['state'] != 'District of Columbia') & (df['state'] != 'Northern Mariana Islands') & (df['state'] != 'Puerto Rico') & (df['state'] != 'Virgin Islands')]

yesterday = pd.read_csv('yesterday.csv')
yesterday = yesterday.loc[(yesterday['state'] != 'Guam') & (yesterday['state'] != 'District of Columbia') & (yesterday['state'] != 'Northern Mariana Islands') & (yesterday['state'] != 'Puerto Rico') & (yesterday['state'] != 'Virgin Islands')]

longago = pd.read_csv('longago.csv')
longago = longago.loc[(longago['state'] != 'Guam') & (longago['state'] != 'District of Columbia') & (longago['state'] != 'Northern Mariana Islands') & (longago['state'] != 'Puerto Rico') & (longago['state'] != 'Virgin Islands')]

fig = go.Figure(
    data = go.Choropleth(  
        locations=longago['code'], 
        z = longago['cases'],
        locationmode = 'USA-states', 
        colorscale = 'Reds',
    ),
    layout = go.Layout(
        geo_scope='usa',
        updatemenus=[dict(
            type='buttons',
            buttons=[dict(
                label='Play',
                method='animate',
                args=[None])])]
    ),
    frames=[
        go.Frame(data=go.Choropleth(
            locations=yesterday['code'], 
            z = yesterday['cases'],
            locationmode = 'USA-states', 
            colorscale = 'Reds',
        ))
    ]
)

fig.show()

# fig = go.Figure(data=go.Choropleth(
    # locations=df['code'], 
    # z = df['cases'],
    # locationmode = 'USA-states', 
    # colorscale = 'Reds',
# ))

# fig.update_layout(
#     geo_scope='usa',
# )