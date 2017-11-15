import re
import csv

## match street number at the beginning of string
street_address_pattern_string = "^[0-9]+"
## match space characters
street_address_pattern_string += "\s+"
## match the street name
street_address_pattern_string += "([0-9]|[a-z])+"
# # ## match space characters
street_address_pattern_string += "\s+"
# #
# # ## match common street suffixes:
street_address_pattern_string += "(av|"
street_address_pattern_string += "ave|"
street_address_pattern_string += "avenue|"
street_address_pattern_string += "st|"
street_address_pattern_string += "street|"
street_address_pattern_string += "dr|"
street_address_pattern_string += "rd|"
street_address_pattern_string += "drive|"
street_address_pattern_string += "road|"
street_address_pattern_string += "blvd|"
street_address_pattern_string += "boulevard|"
street_address_pattern_string += "pl|"
street_address_pattern_string += "place)"
## match whitespace or end of string
street_address_pattern_string += "(\s|$|\.)"

### JUST THE STREET NUMBER
## match street number at the beginning of string
street_number_pattern_string = "^[0-9]+"
## match space characters
street_number_pattern_string += "\s+"

## compile the pattern
street_address_regex = re.compile(street_address_pattern_string)
street_number_regex = re.compile(street_number_pattern_string)

match_count=0.

## read and iterate over the data
fin=open("data/scf_address_data.csv","r",newline="")
fout=open("data/scf_street_name_data.csv","w",newline="")
reader = csv.DictReader(fin)

headers=reader.fieldnames
headers.append("street_name")
writer = csv.DictWriter(fout,fieldnames=headers)

for row in reader:
    address=row["address"]

    ## apply the regular expression
    street_address_match = street_address_regex.search(address.lower())
    if street_address_match:
        match_count+=1

        street_address=street_address_match.group()
        street_name = street_number_regex.split(street_address)[1]
        ## append the street address to the
        ## row and write result to the output
        row["street_name"]=street_name
        writer.writerow(row)

        ## as a sanity check to make sure
        ## the regular expression is correct
        ## print out the matched items.
        # if row_count<200:
            # print(street_address)
            # print(street_name)



# print("percent match: "+str(match_count/reader.line_num))
fin.close()
fout.close()
