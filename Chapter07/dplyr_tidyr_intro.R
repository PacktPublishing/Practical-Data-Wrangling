setwd("~/Documents/book/ch7/ch7")
vehicles<-read.csv("data/vehicles.csv")
gas_prices <- read.csv("data/gas_prices.csv")
roads.lengths <- read.csv("data/artificial_roads_by_region.csv")

library('dplyr')
library('tidyr')


########
#### dplyr intro ###

### Graph fuel economy alongside
### gas prices in USD

## select demo:
vehicles.product <- select(vehicles,make,model,year)
print(vehicles.product)

## the same thing as a tibble
vehicles.product.as.tibble <- as_tibble(
  select(vehicles,make,model,year)
)
print(vehicles.product.as.tibble)

## using arrange
vehicles.product.arranged <- as.tibble(
  arrange(vehicles.product,make,model,year)
)
print(vehicles.product.arranged)

## chain the select and arrange operations to be more cohesive
vehicles.product.arranged <- as_tibble(
  vehicles %>% ## start with the original data
  select(make,model,year,cylinders) %>% ## select the columns
  arrange(make,model,year) ## arrange the rows
)
print(vehicles.product.arranged)

## filter data to just the toyota camry
vehicles.camry <- as.tibble(
  car_data %>% 
  filter(
    make == "Toyota",
    model=="Camry"
  ) %>%
  select(make,model,year)
)
print(vehicles.camry)

### find the average fuel consumption by year:
camry.fuel_economy.by_year <- as_tibble(
  vehicles %>% 
  group_by(year) %>%
  filter(
    make=="Toyota",
    model=="Camry"
  ) %>%
  summarize(
    avg.annual.consumption = mean(barrels08)
  )
)
print(camry.fuel_economy.by_year)

plot(camry.fuel_economy.by_year,type='l')

gas_prices.by_year <- as.tibble(
  gas_prices %>%
    group_by(year) %>%
    select(year,value) %>%
    filter(year>=1984) %>%
    summarize(
      max_price = max(value)
    )
)
print(gas_prices.by_year)

plot(gas_prices.by_year,type='l')

#######
#######
#######
### revisiting the roads dataset one more time ###

## create a copy of roads.lengths and 
## add row means and row sums columns
roads.lengths2<-roads.lengths
roads.lengths2$mean_val <- rowMeans(
  roads.lengths[,-1],
  na.rm = TRUE
)
roads.lengths2$row_total<-rowSums(
  roads.lengths[,-1],
  na.rm=TRUE
)

roads.2011.estimate <- 
  roads.lengths2 %>%
    filter(
      mean_val<2000,
      row_total>0
    )%>%
    mutate(
      X2011.new=ifelse(
      is.na(X2011),
      mean_val,
      X2011
    )
    ) %>%
    select(
      X2011.new
    )
  
print(sum(roads.2011.estimate))
#####
#####
#####
#####

