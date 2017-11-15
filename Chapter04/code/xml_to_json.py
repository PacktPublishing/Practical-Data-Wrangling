import json
from xml.etree import ElementTree as et

fin = open("../data/input_data/wikipedia.xml","r")
tree = et.parse(fin)
root = tree.getroot()

## search through the element tree
## for a long list of elements
data = root.getchildren()[1].getchildren()[1].getchildren()
# print(data)
# print("item_tag:")
# print(data[0].tag)
# print("item_attributes:")
# print(data[0].attrib)

## iterate over the xml data converting
## each entry to json format
json_data=[]
for entry in data:
    json_entry = {}
    json_data.append(entry.attrib)

## output the new data to a json file
fout = open("../data/output_data/wikipedia.json","w")
json.dump(json_data,fout,indent=4)

fin.close()
fout.close()
