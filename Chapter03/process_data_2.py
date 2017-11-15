import json
import pprint
import sys

######### OPEN AND READ THE DATA FILE ###########
inFile = open(sys.argv[1],'r')
scf_data = json.load(inFile)
# print(scf_data)
inFile.close()

############ DATA EXPLORATION #############
# dataType = str(type(scf_data))
# print("type of data: " + dataType)
# print("dictionary keys: " + str(scf_data.keys()))
# issues_data_type = str(type(scf_data["issues"]))
# print("data type of the 'issues' value: " + issues_data_type )
# print("first element of 'issues' list:")
# print(scf_data["issues"][0])

## print data variables
# pp = pprint.PrettyPrinter(indent=4)
# print("first data entry:")
# pp.pprint(scf_data["issues"][0])

############ DATA MODIFICATION #############
new_scf_data = []
variables = ["address","created_at","summary","description","lng","lat","rating"]
for old_entry in scf_data["issues"]:
    new_entry={}
    for variable in variables:
        new_entry[variable] = old_entry[variable]
    # print(new_entry)
    new_scf_data.append(new_entry)

### OUTPvariableUTTING THE NEW DATA TO A NEW FILE ###
outfile = open(sys.argv[2],"w")
json.dump(new_scf_data, outfile, indent=4)
outfile.close()
