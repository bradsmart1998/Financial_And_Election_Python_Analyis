# Import dependencies
import os
import csv 
from statistics import mean

# the path to open the budget data csv file from the resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# open the csv file in read mode
with open(csvpath, 'r', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # i dentify what are the headers of the csv file
    csv_header = next(csvreader)
    print(f"This is the header: {csv_header}")

    # creating empty lists to store the months and profit and changelist 
    month = []
    profit = []
    change_list = []
    
    # start loop through rows in the csv file
    for row in csvreader:
        # add the months from the first row and the profit from the second row
        # store them both in appropriate lis
        month.append(row[0])
        profit.append(row[1])  

     # Count the amount of rows contained in the date column
     # this will equal the total amount of months im the dataset
    totalmonth = (len(month))

    # sum the total from the profit/losses column to work out the sum of the profit and loss
    profit_total = sum(list(map(int, profit)))

    # convert the profit list from a list of strings to a list of integers
    profit_num = (list(map(int, profit)))

    # start the loop on the first value and set as previous value
    previous_value = profit_num[0]

    # start the loop at the 2nd value of the profit number list
    for i in range(1,len(profit_num)):

        # work out the change between the second and first values of the list 
        change = (profit_num[i] - previous_value)

        # add the result to the change list 
        change_list.append(change)

        # move the previous value up
        previous_value = profit_num[i]

    # sum the change list to work out the total change
    total_change = sum(change_list)
    
    # calculate average change by dividing the total change - 1 to two decimal places
    avg_change = round((total_change / (totalmonth - 1)),2)

# Identify the maximum and minimum values from the change list 
max_pl = max(change_list)
min_pl = min(change_list)

# index the values to find where that value occurs in the list 
max_index = change_list.index(max_pl)
min_index = change_list.index(min_pl)

# add 1 to the index value and identify what date occurs on the index
max_month = month[max_index + 1]
min_month = month[min_index + 1]

# Create the output path to the analysis text file
output_path = os.path.join('Analysis', 'analysis.txt')

# open the textfile in write mode and apply the appropriate encoding
with open(output_path, 'w', encoding="utf8") as textfile:
    
    # write the title of the output
    textfile.write(f'Financial Analysis\n')
    
    # write remaining sections to text file
    textfile.write(f'-------------------------------------------------------\n')
    textfile.write(f"Total Months: {totalmonth} \n")
    textfile.write(f'Total: ${profit_total}\n')
    textfile.write(f"Average Change: ${avg_change}\n")
    textfile.write(f"Greatest Increase in Profits: {max_month} (${max_pl})\n")
    textfile.write(f"Greatest Decrease in Profits: {min_month} (${min_pl})\n")

# print results in the terminal
print(f'Financial Analysis')
print(f'-------------------------------------------------------')
print(f"Total Months: {totalmonth}")
print(f'Total: ${profit_total}')
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_pl})")
print(f"Greatest Decrease in Profits: {min_month} (${min_pl})")