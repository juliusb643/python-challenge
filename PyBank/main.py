import os 
import csv

budget_data_csv = "C:\\Users\\juliu\\OneDrive\\Desktop\\python-challenge starter code\\PyBank\\Resources\\budget_data.csv"

with open(budget_data_csv, encoding='UTF-8') as csvfile:
	data = list(csv.reader(csvfile))

num_months = 0
profit = 0
previous_profit = 0
changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

for row in data[1:]:
    date = row[0]
    num_months = num_months +1 
    profit = profit + int(row[1])
    profit_loss = int(row[1])

    if num_months > 1:
        change = profit_loss - previous_profit
        changes.append(change)

        if change > greatest_increase["amount"]:
             greatest_increase["date"] = date
             greatest_increase["amount"] = change
        elif change < greatest_decrease["amount"]:
             greatest_decrease ["date"] = date
             greatest_decrease ["amount"] = change

    previous_profit = profit_loss

average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

print (profit)
print (num_months) 
print (average_change)
print (greatest_increase)
print (greatest_decrease) 

output = os.path.join("PyBank\Resources","budget.txt")

with open(output, "w") as txt_file:
    budget = (
        f"\n\nFinancial Analysis\n\n"
        f"--------------------\n\n"
        f"Total Months: {num_months}\n\n"
        f"Total: {profit}\n\n"
        f"Average Change: {average_change}\n\n"
        f"Greatest Increase in Profits: {greatest_increase}\n\n"
        f"Greatest Decrease in Profits: {greatest_decrease}"
    )

    txt_file.write(budget)