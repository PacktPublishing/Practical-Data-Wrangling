import requests
import json

## build a base url which is the endpoint to the api
## for this script, this is all you need
base_url = "https://seeclickfix.com/api/v2/issues?"

## submit a get request to the URL and
## collect the response in the response object
response = requests.get(base_url)

## use the json module to write the response data
## from the api into a json file
fout = open("output_data/scf_recent_issues.json","w")
json.dump(response.json(),fout,indent=4)
fout.close()
