import pandas as pd
import json
file = "Fileexample.csv"
df = pd.read_csv(file)
df = pd.read_xml(file)
df = pd.read_json(file)
df = pd.read_excel(file)
#colum
df.columns = ['Name', 'Phone', 'Number', 'Birthday']
#Read a Json
with open('fileexample.json', 'r') as openfile:
    json_object = json.load(openfile)
print(json_object) 
# Read XML
