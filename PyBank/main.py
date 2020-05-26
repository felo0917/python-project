# Import Data from CSV file
import os 
import csv

#Path of data from CSV file
csvpath = os.path.join('Resources', 'Budget_data.csv')


# Read the CSV file
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Total number of months
    month_count = []

    revenue = []
    revenue_change = []
    average_change = []

    #read the header row first
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")   

    # Loop to calculate total number of months
    for row in csvreader:
        month_count.append(row[0])
        revenue.append(row[1])
    print(len(month_count))

    # Loop through the data for revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

    # Average Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])

    # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    print(revenue_change)
    average_change = Total / len(revenue_change)
    print(average_change)
    print(Total)

 # Greatest Increase
    profit_increase = max(revenue_change)
    print(profit_increase)
    j = revenue_change.index(profit_increase)
    month_increase = month_count[j+1]
    
# Greatest Decrease
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    k = revenue_change.index(profit_decrease)
    month_decrease = month_count[k+1]


# Print Financial Analysis
print(f'Financial Analysis'+'\n')
print(f'----------------------'+'\n')
print("Total months: " + str(len(month_count)))
print("Net Total: $ " + str(total_revenue))
print("Average Change: $" + str(average_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

# -->>  Export a text file with the results
file ="outputbudgetdata.txt"


with open(file, "w") as text:

    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write("Total Months: " + str(len(month_count)) +'\n')
    text.write(f"Net Total:  ${total_revenue}\n")
    text.write(f"Average Change:  ${average_change}\n")
    text.write(f"Greatest Increase in Profits:  {month_increase} (${profit_increase})\n")
    text.write(f"Greatest Decrease in Losses:  {month_decrease} (${profit_decrease})\n")


