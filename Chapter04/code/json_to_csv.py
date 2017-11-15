import csv
import json

## read in the input json data
fin = open("../data/input_data/scf_extract.json","r",newline="")
json_data = json.load(fin)
fin.close()

## get an array of data fields to
## use as column headers
keys = json_data[0].keys()

## open an output file with write permission
## and create a writer object
fout = open("../data/output_data/scf_extract.csv","w")
writer = csv.writer(fout)
writer.writerow(keys)

## iterate over the json data extracting
## the data fields into an ordered list
## write each data entry to the output file
for entry in json_data:
    row=[]
    for key in keys:
        row.append(entry[key])
    writer.writerow(row)


fout.close()
