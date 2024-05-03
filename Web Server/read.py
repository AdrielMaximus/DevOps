import pandas as pd # type: ignore
import json
import xml.etree.ElementTree as tree
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
tree = etree.parse("fileexample.xml") # type: ignore
root = tree.getroot()
columns = ['Name', 'Phone', 'Number', 'Birthday']
df = pd.DataFrame(columns = columns)
for node in root:
    name = node.find("name").text
    phonenumber = node.find("phonenumber").text
    birthday = node.find("birthday").text
    
df = df.append(pd.Series([name.phonenumber, birthday], index = columns)... . ., ignore_index = True)
