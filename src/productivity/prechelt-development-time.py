"""Regenerate boxplot of development times."""

import pandas as pd
import plotly.express as px
import sys

assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} infile outfile"
df = pd.read_csv(sys.argv[1])
fig = px.box(df, y="whours", points="all")
fig.update_layout(margin={"t": 0, "b": 0, "l": 0, "r": 0})
fig.write_image(sys.argv[2], width=600, height=400)
