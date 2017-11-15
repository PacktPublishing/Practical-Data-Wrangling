## this may crash your computer,
## so use this code for demonstration purposes,
## or run at your own risk (without any unsaved work open)

import csv

myData=[]

fin = open('data/fake_weather_data.csv','r',newline='')
reader = csv.reader(fin)
for row in reader:
    myData.append(row)
