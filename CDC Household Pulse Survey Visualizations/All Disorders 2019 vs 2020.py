import plotly.graph_objects as go

disorders = ['Symptoms of Anxiety Disorder', 'Symptoms of Depressive Disorder', 'Symptoms of Anxiety Disorder and/or Depressive Disorder']

fig = go.Figure()
fig.add_trace(go.Bar(x=disorders,
                y=['8.2', '6.6', '11.0'],
                name='2019 Percentages',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=disorders,
                y=['29.4', '24.9', '34.3'],
                name='2020 Percentages',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_layout(
    title='Symptoms of Mental Health Disorders Between 2019 and 2020',
    title_x=0.5,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Percentage',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()