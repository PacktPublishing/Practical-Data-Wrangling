####
####
## reading in data
## set the working directory
## the working directory here should be changed 
## for your setup
setwd("~/Documents/book/ch6/ch6/")

## Read in the data, and assign to the roads_by_country
## variable. Roads by country is an R Dataframe
roads <- read.csv("data/artificial_roads_by_region.csv")

## select the 2011 column from the roads dataframe
roads.2011 <- roads$X2011

####
####
####
## finding the 2011 total

## create a index corresponding to not na values
not.na <- !is.na(roads.2011)

## index roads.2011 using not na
roads.2011.cleaned <- roads.2011[not.na]

## print the sum of the available roads in 2011.
total.2011<-sum(roads.2011.cleaned)

## the more concise way
total.2011<-sum(roads.2011, na.rm=TRUE)


####
####
####
### Outlier Detection and Removal ###

## get the numerical data
roads.num <- roads[,-1]

## get mean by row
roads.means <- rowMeans(roads.num,na.rm=TRUE)

## plot the means using a histogram
hist(roads.means)

## remove entries with means greater than 2000
roads.keep <- roads.means < 2000

## remove outliers from the original dataframe 
roads2<-roads[roads.keep,]

## remove outliers from the numerical roads dataframe
roads.num2 <- roads.num[roads.keep,]

## remove outliers from the vector of means
## (we will use this later)
roads.means2 <- roads.means[roads.keep]

## plot the means with outliers removed
hist(roads.means2)

####
####
####
### NA handling ###

### Removal of NA values
## remove all rows where all columns are NA

## get the sum of the values of each row
roads.num2.rowsums <- rowSums(roads.num2,na.rm=TRUE)

## make an index of the rows in which all values are NA
roads.keep2 <- roads.num2.rowsums>0

## filter out rows with all NA values
roads3 <- roads2[roads.keep2,]
roads.num3 <- roads.num2[roads.keep2,]
roads.means3 <- roads.means2[roads.keep2]


### Replacement of NA values with a constant
### (this is just for demonstration puposes,
### we won't use this here)

roads.replace.na <- roads3
roads.replace.na[is.na(roads3)] <- 0

### Imputation:
### replacing NA values with guesses.

### get the estimated total for 2011
roads.2011.3 <- roads3$X2011
roads.2011.3[is.na(roads.2011.3)] <- roads.means3[is.na(roads.2011.3)]
print(sum(roads.2011.3))

## create a function that takes a column and 
## replaces the na values with the row means
impute <- function(x,imputations) {
  x[is.na(x)] <- imputations[is.na(x)]
  return(as.numeric(x))
}

## apply the function to each column with apply()
roads.impute.na <- data.frame(
  apply(roads.num3,2,impute,imputations=roads.means3)
)

## print the estimated total for every year...
print(colSums(roads.impute.na))

####
####
## vector intro
print(c(1,2,3,4,5,6))
print(1:6)

my.vector=1:10
print(my.vector)
print(my.vector[3])
print(my.vector[1:5])

## is.na example
print(is.na(c(1,NA,2,NA,NA,3,4,NA,5)))

#### 
####
## indexing a dataframe examples
the.same.thing <- roads[,]
first.three.rows <- roads[1:3,]
first.tree.columns <- roads[,1:3]
dropped.first.column <- roads[,-1]
X2011.with.region <- roads[,c("region.name","X2011")]
