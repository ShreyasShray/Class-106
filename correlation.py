import pandas as pd
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drinks_sales = []
    with open(data_path, newline = "") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drinks_sales.append(float(row["Ice-cream Sales( ₹ )"]))

    return ({"x": ice_cream_sales, "y": cold_drinks_sales})

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between temperatur vs ice cream is " + str(correlation))

def setup():
    data_path = "data1.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()