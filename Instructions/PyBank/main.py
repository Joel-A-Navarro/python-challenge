# import dependencies
import pandas as pd

data = pd.read_csv("PyBank/Resources/budget_data.csv")
print (data.head())

#number of months in data set
#alternately months = len(data)
months = data["Date"].count()
print(months)

#net total amount of profit/losses
total = data["Profit/Losses"].sum()
print(total)

#calculate changes in profit/losses, find average
monthly_changes = [0]
for x in range(months - 1):
    #(x + 1, 1)
    current_row = data["Profit/Losses"][x]
    next_row = data["Profit/Losses"][x + 1]
    change = next_row - current_row
    monthly_changes.append(change)
print(monthly_changes)
data["monthly_differences"] = monthly_changes
print(data.head())
average_change = data["monthly_differences"][1:].mean()
print(average_change)