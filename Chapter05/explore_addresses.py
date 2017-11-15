import pandas

## read data to a dataframe
addresses=pandas.read_csv("data/scf_address_data.csv")

## extract address column and print random sample to
## output
print(addresses["address"].sample(100, random_state(0)))
