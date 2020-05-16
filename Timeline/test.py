import pandas as pd
import plotly.graph_objects as go

mapbox_access_token = 'pk.eyJ1IjoiYXNoMDk0OSIsImEiOiJjazlraGVnaWgwNDVqM2VubjdmcDB2cGY2In0.zWvDiP833xIAM0-d2L0X-w'

filename = "https://raw.githubusercontent.com/spencerlawrence36/basic/master/places.csv"
df = pd.read_csv(filename, encoding='utf-8')
df = df.head(100)

data = [go.Scattermapbox(
               lat=[33.49],
               lon=[-112.05],
               mode='markers',
               marker=dict(size=10, color='red')
            )
        ]

layout = go.Layout(width=800,
    autosize=True,
    hovermode='closest',
    mapbox=dict(accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=33.49,
                            lon=-112.05),
                pitch=0,
                zoom=9,
                style='light'
                )
            )

lats = list(df['lat'])
lons = list(df['lng'])

frames = [dict(data= [dict(type='scattermapbox',
                           lat=lats[:k+1],
                           lon=lons[:k+1])],
               traces= [0],
               name='frame{}'.format(k)       
              )for k  in  range(1, len(df))]   

sliders = [dict(steps= [dict(method= 'animate',
                           args= [[ 'frame{}'.format(k) ],
                                  dict(mode= 'immediate',
                                  frame= dict( duration=100, redraw= True ),
                                           transition=dict( duration= 0)
                                          )
                                    ],
                            label='{:d}'.format(k)
                             ) for k in range(len(df))], 
                transition= dict(duration= 0 ),
                x=0,#slider starting position  
                y=0, 
                currentvalue=dict(font=dict(size=12), 
                                  prefix='Point: ', 
                                  visible=True, 
                                  xanchor= 'center'),  
                len=1.0)
           ]

layout.update(updatemenus=[dict(type='buttons', showactive=False,
                                y=0,
                                x=1.05,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=100, 
                                                                    redraw=True),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate'
                                                        )
                                                   ]
                                             )
                                        ]
                               )
                          ],
              sliders=sliders);

fig=go.Figure(data=data, layout=layout, frames=frames)
fig.show()