import pandas as pd
file = "Fileexample.csv"
df = pd.read_csv(file)
df = pd.read_xml(file)
df = pd.read_json(file)
df = pd.read_excel(file)