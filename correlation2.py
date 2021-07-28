import csv
import plotly.express as px

with open("data4.csv", newline = "") as f:
    reader = csv.DictReader(f)
    fileData = list(reader)

fig = px.scatter(fileData, x = "Coffee in ml", y = "sleep in hours")
fig.show()