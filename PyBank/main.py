#modules
import os
import csv

PROFIT_INDEX = 1
MONTH_INDEX = 0

#PLvariable
total_profit = 0
months_count = 0
is_first_row = True
profit_loss_totalchange = 0

#lists
profits_list = []
months_list = []
monthly_profit_change = []

#Set path for file
csvpath = os.path.join("/Users/anico/Desktop/Boot Camp Work/Challenges/Python/python-challenge/PyBank/Resources/budget_data.csv")

#Open the CSV
with open(csvpath) as csvfile:
    data = csv.reader(csvfile)

    next(data)    #skip the header
    for row in data:
        months_list.append(row[MONTH_INDEX])
        profits_list.append(int(row[PROFIT_INDEX]))
        months_count += 1
        current_profit = int(row[PROFIT_INDEX]) 
        total_profit = total_profit + current_profit
        

    for i in range(len(profits_list)-1): #iterate through the profits in order to get the monthly change
        monthly_profit_change.append(profits_list[i+1]-profits_list[i])
       
# Get the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#Financial Analysis print statements
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months:  {months_count}")
print(f"Total: ${total_profit}")
print(f"Average Change: $ {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months_list[max_increase_month]} ${max_increase_value}")
print(f"Greatest Decrease in Profits: {months_list[max_decrease_month]} ${max_decrease_value}")

f = open("PyBank_Analysis2.txt", "a+") # open a file for writing and + create it if it does not exist

#Financial Analysis print statements to .txt
print("Financial Analysis", file=f)
print("------------------------------------", file=f)
print(f"Total Months:  {months_count}", file=f)
print(f"Total: ${total_profit}", file=f)
print(f"Average Change: $ {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}", file=f)
print(f"Greatest Increase in Profits: {months_list[max_increase_month]} ${max_increase_value}", file=f)
print(f"Greatest Decrease in Profits: {months_list[max_decrease_month]} ${max_decrease_value}", file=f)

f.close()