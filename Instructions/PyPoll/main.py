# import libraries
import pandas as pd

# import election_data_csv in resource folder
data = pd.read_csv("./Resources/election_data.csv")
print (data.head())

# identify variables
total_votes = 0

# loop over all rows, count votes
for row in data:
    print(row)
    