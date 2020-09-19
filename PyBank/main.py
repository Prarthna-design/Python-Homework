import os
import csv

#create path for the filename
output_csv = os.path.join("Resources", "budget_data.csv")

# print header
print('Financial Analysis')
print('----------------------')


#open file, read and print header

with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    

    # total number of months included in the dataset

    next(csvreader)
    months = len(list(csvreader))
    print(f'Total Months: {months}')


    #The net total amount of "Profit/Losses" over the entire period

with open(output_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    net = []
    months = []
    for row in csvreader: 
        net.append(float(row[1]))
        months.append(row[0])
        # print(type(row[1]))
# print(months)

print(f'Total: $ {sum(net)}')

# average of change in "Profit_Losses"
profitlosschange = []
for value in net[1:]:
    i = net[net.index(value) - 1]
    change = value - i
    profitlosschange.append(change)
# print(profitlosschange)


average = sum(profitlosschange) / len(profitlosschange)
  
print(f'Average Change: $ {str(round(average, 2))}')

GreatestIncrease = max(profitlosschange)
# print(GreatestIncrease)
g = profitlosschange.index(GreatestIncrease) +1
maxmonth = months[g]
print(f'Greatest Increase in Profits: {maxmonth} $ {str(GreatestIncrease)}')

GreatestDecrease = min(profitlosschange)
# print(GreatestDecrease)
d = profitlosschange.index(GreatestDecrease) +1
minmonth = months[d]
# print(minmonth)
print(f'Greatest Decrease in Profits: {minmonth} $ {str(GreatestDecrease)}')

output_csv = os.path.join("analysis", "analysis.csv")
with open(output_csv, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')


    csvwriter.writerow(["Total Months: 86"])
    csvwriter.writerow(["Total: $38382578"])
    csvwriter.writerow(["Average Change: $-2315.12"])
    csvwriter.writerow(["Greatest Increase in Profits: Feb-2012  $ 1926159"])
    csvwriter.writerow(["Greatest Decrease in Profits: Sep-2013 $ -2196167"])

        









