import pandas as pd
import plotly.graph_objects as go

week1 = pd.read_csv('data\Symptoms of Anxiety Disorder - Week 1.csv')
week2 = pd.read_csv('data\Symptoms of Anxiety Disorder - Week 2.csv')
week3 = pd.read_csv('data\Symptoms of Anxiety Disorder - Week 3.csv')
week4 = pd.read_csv('data\Symptoms of Anxiety Disorder - Week 4.csv')

fig = go.Figure(
    data = go.Choropleth(
        locations=week1['State Abbreviation'],
        z=week1['Value'].astype(float),
        colorscale='Blues',
        locationmode='USA-states',
        # zmin=10,
        zmin=15,
        zmax=45,
        zauto=False
    ),
    layout = go.Layout(
        title='Symptoms of Anxiety Disorder for Apr 23 - May 5',
        title_x=0.5,
        geo_scope='usa',
        updatemenus=[dict(
            type='buttons',
            buttons=[dict(
                label='Play',
                method='animate',
                args=[None, {'frame': {'duration': 4000},}])])]
    ),
    frames=[
        go.Frame(
            data=[go.Choropleth(
                locations=week2['State Abbreviation'],
                z=week2['Value'].astype(float),
                colorscale='Blues',
                locationmode='USA-states',
                zmin=15,    
                zmax=45,
                zauto=False)],
            layout=go.Layout(title_text='Symptoms of Anxiety Disorder for May 7 - May 12')
        ),
        go.Frame(
            data=[go.Choropleth(
                locations=week3['State Abbreviation'],
                z=week3['Value'].astype(float),
                colorscale='Blues',
                locationmode='USA-states',
               zmin=15,
                zmax=45,
                zauto=False)],
            layout=go.Layout(title_text='Symptoms of Anxiety Disorder for May 14 - May 19')
        ),
        go.Frame(
            data=[go.Choropleth(
                locations=week4['State Abbreviation'],
                z=week4['Value'].astype(float),
                colorscale='Blues',
                locationmode='USA-states',
               zmin=15,
                zmax=45,
                zauto=False)],
            layout=go.Layout(title_text='Symptoms of Anxiety Disorder for May 21 - May 26')
        )
    ]
)

fig.update_layout(transition_duration=3000)
fig.show()
