import os
import csv
from pathlib import Path


#set path
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
total_months = 0
total_profit_losses = 0
previous_profit_losses = 0
monthly_changes = []
months = []


# with open csvfile:
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    header = next(csvreader)

    for row in csvreader:
        # total months
        total_months += 1
        # total profit/loses
        total_profit_losses += int(row[1])

        # monthly change
        if total_months > 1:
            change = int(row[1]) - previous_profit_losses
            monthly_changes.append(change)
            months.append(row[0])
        
        previous_profit_losses = int(row[1])

# average change
    if len(monthly_changes) > 0:
        average_change = sum(monthly_changes) / len(monthly_changes)
    else:
        average_change = 0
        
# Greatest increase and decrease
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

# Find out the month of greatest increase and decrease 

if monthly_changes:
    greatest_increase_month = months[monthly_changes.index(greatest_increase)]
    greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]

else:
    greatest_increase_month = ""
    greatest_decrease_month = ""


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

output_path = Path("Analysis", "financial_analysis.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")  