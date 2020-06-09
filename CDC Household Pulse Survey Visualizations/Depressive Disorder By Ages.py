import plotly.graph_objects as go

ages = ['18-29 years', '30-39 years', '40-49 years', '50-59 years', '60-69 years', '70-79 years', '80 years and above']

fig = go.Figure()
fig.add_trace(go.Bar(x=ages,
                y=['36.7', '27.4', '24.2', '24.6', '19.8', '13.3', '17.1'],
                marker_color='rgb(55, 83, 109)'
                ))

fig.update_layout(
    title='Symptoms of Depressive Disorde Among Varying Age Groups',
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