import csv
import plotly.express as px

with open("data2.csv", newline = "") as f:
    reader = csv.DictReader(f)
    fig = px.scatter(reader, x = "Size of TV", y = "	Average time spent watching TV in a week (hours)")
    fig.update_yaxes(rangemode = "tozero")
    fig.show()