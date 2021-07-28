import csv
import plotly.express as px

with open("data3.csv", newline = "") as f:
    reader = csv.DictReader(f)
    fig = px.scatter(reader, x = "Marks In Percentage", y = "Days Present")
    fig.update_yaxes(rangemode = "tozero")
    fig.show()