import pandas

## read the csv file into a pandas dataframe
roads = pandas.read_csv("../data/input_data/artificial_roads_by_region.csv")

## print out the column headers
# print("column headers:")
# print(list(roads))

## extract roads from 2011
roads_2011 = roads['2011']
# print(roads_2011)

## convert the data type from string to float
roads_2011_2 = roads_2011.astype('float')

## find the sum of the values from 2011
total_2011 = roads_2011_2.sum()

print("total road leangth as of 2011:")
print(total_2011)

## create a list of columns to extract
columns = ["2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000"]
## extract the numerical fields
roads_num = roads[columns]

## the more concise way
roads_num = roads.drop("region name",axis=1)

# ## sum along the vertical axis for all columns
total_by_year=roads_num.sum(0)

# print("total road leangth by year:")
# print(total_by_year)
