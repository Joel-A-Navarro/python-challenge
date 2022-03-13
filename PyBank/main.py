# import dependencies
import os
import csv
csvpath = os.path.join("PyBank/Resources/budget_data.csv")

# create variables 
month = []
totalpro = []
monthchange = []

# import csv with headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # total months and total profit in a table   
    for row in csvreader:
        month.append(str(row[0]))
        totalpro.append(int(row[1]))
    total_m = len(month)
    total_p = sum(totalpro)
    
    # month change and append to list       
    for x in range(len(totalpro)-1):
        monthchange.append(totalpro[x+1]-totalpro[x]) 

    # average change
    mcpl = sum(monthchange)    
    denom = len(monthchange)  
    averagepl = mcpl/denom

    # greatest and least amounts from monthchange list
    greatest = max(monthchange)
    least = min(monthchange)

    # find index position of min and max values
    index = monthchange.index(greatest)
    index2 = monthchange.index(least)

    # index in variable the table is one longer(nextmonth - previous) equals change
    month_location1 = (month[index+1])
    month_location2 = (month[index2+1])

    # print table in terminal
    print("Financial Analysis")
    print("------------------------------------------")
    print(f'Total Months: {total_m}')
    print(f'Total: ${format(total_p,",.0f")}')
    print(f'Average Change: ${format(averagepl, ",.2f")}')
    print(f'Greatest Increase in Profits: {month_location1} (${format(greatest, ",.0f")})')
    print(f'Greatest Decrease in Profits: {(month_location2)} (${format(least,",.0f")})')           

    #Send output to text file
    f = open("PyBank_output.txt", "a")
    print("Financial Analysis", file=f)
    print("------------------------------------------", file=f)
    print(f'Total Months: {total_m}', file=f)
    print(f'Total: ${format(total_p,",.0f")}', file=f)
    print(f'Average Change: ${format(averagepl, ",.2f")}', file=f)
    print(f'Greatest Increase in Profits: {month_location1} (${format(greatest, ",.0f")})', file=f)
    print(f'Greatest Decrease in Profits: {(month_location2)} (${format(least,",.0f")})', file=f)  
    f.close()