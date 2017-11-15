import csv

## open the file containing the data
fin = open("../data/input_data/artificial_roads_by_region.csv","r",newline="")

## create a file reader using the file object, 'fin'
reader = csv.DictReader(fin)

## print the column headers
print("column headers:")
print(reader.fieldnames)

total_roads=0
## iterate over the rows in the CSV file
print("first 10 values of the 2011 column:")
for row in reader:
    ## print out the first 10 values of 2011
    if reader.line_num <= 11:
        print(row["2011"])
    if row["2011"] != "":
        total_roads+=float(row["2011"])

print("total leangth of roads as of 2011:")
print(total_roads)

fin.close()
