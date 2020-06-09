import plotly.graph_objects as go

ages = ['Less than a high school diploma', 'High School Diploma or GED', 'Some college/Associate''s degree', 'Bachelor''s degree or higher']

fig = go.Figure()
fig.add_trace(go.Bar(x=ages,
                y=['40.6', '29.5', '32.4', '23.7'],
                marker_color='rgb(55, 83, 109)'
                ))

fig.update_layout(
    title='Symptoms of Depressive Disorder Among Varying Education Levels',
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
    # barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()