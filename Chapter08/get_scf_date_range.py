import requests
import csv

## build the base url
url = "https://seeclickfix.com/api/v2/issues?"

## restrict the result to issues after January 2017
url+="after=2017-01-01T00:00:00"

## restrict the result to issues before February 2017
url+="&before=2017-01-07T00:00:00"

## leave the page paramater empty so that it
## can be dynamically changed
url+="&page="

## create a list of field names that should be extracted
fields=["created_at","closed_at","summary","address"]

## open the output file and create a writer
## write the column headers to the output file
fout = open("output_data/scf_date_range_issues.csv","w")
writer=csv.writer(fout)
writer.writerow(fields)

## initialize the page and data variables
page=1
data=requests.get(url+str(page)).json()["issues"]

## go page by page until there is no data
while len(data)>0:
    ## if there is data, iterate over the
    ## data entries, writing the result to the output
    for entry in data:
        row=[]
        for field in fields:
            row.append(entry[field])
        writer.writerow(row)

    ## in each iteration of the loop,
    ## increase the page number and get
    ## the data for the subsequent page
    page+=1
    data=requests.get(url+str(page)).json()["issues"]


fout.close()
