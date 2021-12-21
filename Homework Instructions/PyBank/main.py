# dependencies
import os

# csv data
path = r'resources\budget_data.csv'
with open(path) as data:
    
    rawData = data.read()

# variables
month = []
total_pro = []
month_change = []

# import data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # total months and profit   
    for row in csvreader:
        month.append(str(row[0]))
        total_pro.append(int(row[1]))
    total_m = len(month)
    total_p = sum(totalpro)
    
    # month changes     
    for x in range(len(total_pro)-1):
        month_change.append(totalpro[x+1]-totalpro[x]) 

    # average monthly change
    mcpl = sum(month_change)    
    denom = len(month_change)  
    average_pl = mcpl/denom

    # maximun and minimum amout
    greatest = max(month_change)
    least = min(month_change)

    # index positioning of min and max
    index = month_change.index(greatest)
    index_2 = month_change.index(least)
    month_location1 = (month[index+1])
    month_location2 = (month[index2+1])

    # print table
    print("Financial Analysis")
    print("------------------------------------------")
    print(f'Total Months: {total_m}')
    print(f'Total: ${format(total_p,",.0f")}')
    print(f'Average Change: ${format(average_pl, ",.2f")}')
    print(f'Greatest Increase in Profits: {month_location1} (${format(greatest, ",.0f")})')
    print(f'Greatest Decrease in Profits: {(month_location2)} (${format(least,",.0f")})')           

    # create text file
    os.chdir("C:\\UTSADBC\\python-challenge\\PyBank\\Analysis")
    f = open("PyBank_output.txt", "a")
    print("Financial Analysis", file=f)
    print("------------------------------------------", file=f)
    print(f'Total Months: {total_m}', file=f)
    print(f'Total: ${format(total_p,",.0f")}', file=f)
    print(f'Average Change: ${format(averagepl, ",.2f")}', file=f)
    print(f'Greatest Increase in Profits: {month_location1} (${format(greatest, ",.0f")})', file=f)
    print(f'Greatest Decrease in Profits: {(month_location2)} (${format(least,",.0f")})', file=f)  
    f.close()
