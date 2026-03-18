import pandas as pd
import plotly.express as px

data= {
    "epoch": [1,2,3,4,5,6,7,8,9,10],
    "losses": [0.9,0.85,0.83,0.70,0.63,0.61,0.60,0.58,0.55,0.54]
}

df= pd.DataFrame(data)

fig= px.line(
    df,
    x="epoch",
    y="losses",
    title="Epochs vs training losses graph"
)

fig.add_annotation(
    x=5,y=0.63,
    text= "Loss stabilizes",
    bordercolor= "red",
    showarrow= True,
    arrowhead=3
)

fig.show()