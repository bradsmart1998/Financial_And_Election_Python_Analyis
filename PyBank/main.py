# import os and csv
import os
import csv 
from statistics import mean
# the path to open the csv file from the resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# open the csv file 
with open(csvpath, 'r', encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # What are the headers of the csv file
    csv_header = next(csvreader)
    print(f"This is the header: {csv_header}")

    # creating empty lists to store the months and profit
    month = []
    profit = []
    change_list = []
    # start loop through rows
    for row in csvreader:
        # add the months and variables to a list
        month.append(row[0])
        profit.append(row[1])  

     # Count the amount of rows contained in the date column
    totalmonth = (len(month))

    # sum the total from the profit/losses column
    profit_total = sum(list(map(int, profit)))
    profit_num = (list(map(int, profit)))
    
    for i in range(len(profit_num)):
        change = (profit_num[i] - profit_num[i-1])
        change_list.append(change)
    total_change = sum(change_list)

    # calculate average change
    avg_change = (total_change / totalmonth)


# the output path to write the analysis text file
output_path = os.path.join('Analysis', 'analysis.txt')

# open the textfile
with open(output_path, 'w') as textfile:
    # active the text writer
    txtwriter = csv.writer(textfile)
    
    # writefinancial analysis total
    txtwriter.writerow(['Financial Analysis'])
    
    # write remaining sections to text file
    txtwriter.writerow(['-------------------------------------------------------'])
    txtwriter.writerow([f"Total Months: {totalmonth} "])
    txtwriter.writerow([f'Total: ${profit_total}'])

   

# print the financial analysis output section
print("\n\n")
print("Financial Analysis \n")
print("-------------------------------------------------------")
print(f"Total Months: {totalmonth} ")
print(f"Total: ${profit_total} ")
print(f"Average Change: ${avg_change}")




    
        

