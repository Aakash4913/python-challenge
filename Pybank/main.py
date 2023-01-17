
#importing needed packages 
import csv
import os


#set up path to get data
budget_csv = os.path.join('..','Resources','budget_data.csv')

#open up the CSV file in order to read
with open(budget_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter =',')


#initializing variables, need lists to store values
    totalmonths = 0
    totalprofits = 0 
    profitlist = []
    monthslist = []

    #to skip header row 
    next(csvreader)

    #reads through each row in csv file, adding month for each row 
    for rows in csvreader:
        totalmonths += 1
        
      #adding all numbers in 2nd row for total profits  
        totalprofits += int(rows[1])

    #appending row 1 and 2 into respective list
        profitlist.append(int(rows[1]))
        monthslist.append(str(rows[0]))


#initialize list to store change and set counters
    deltalist = []
    i =1
    j= 0 

    #while loop to tell list when to stop, purpose to get the change between profits into a list
    while i < len(profitlist):
        delta = profitlist[i] - profitlist[j]

        deltalist.append(delta)
        i += 1
        j += 1
    
#formulas needed

    average_change = sum(deltalist)/len(deltalist)
    greatest_increase = max(deltalist)
    greatest_decrease = min(deltalist)

    greatest_increase_index = deltalist.index(greatest_increase)
    greatest_decrease_index = deltalist.index(greatest_decrease)

#added + 1 for index to line up between monthslist, and profitlist
    month_greatest_increase = monthslist[greatest_increase_index + 1]
    month_greatest_decrease = monthslist[greatest_decrease_index + 1]
        

#test 

print(" \n Financial Analysis \n")

print("-------------------------\n")

print("Total Months: " + str(totalmonths) + "\n")
print("Total: $" + str(totalprofits) + "\n")

print("Average Change $" + str(round(average_change, 2)) + "\n")
print("Greatest Increase in Profits: " + str(month_greatest_increase) + " ($" + str(greatest_increase) + ")\n")
print("Greatest Decrease in Profits: " + str(month_greatest_decrease) + " ($" + str(greatest_decrease) + ")\n")


#creating new file called "profit_results.txt" and placing it in Analysis folder
file2 = os.path.join('..', 'Analysis', ' profit_results.txt')

#opening file in order to write in it
with open(file2, 'w') as file:
    file.write(" \n Financial Analysis \n\n")
    
    file.write("-------------------------\n\n")
    file.write("Total Months: " + str(totalmonths) + "\n\n" )
    
    file.write("Total: $" + str(totalprofits) + "\n\n")
    file.write("Average Change $" + str(round(average_change, 2)) + "\n\n")
    file.write("Greatest Increase in Profits: " + str(month_greatest_increase) + " ($" + str(greatest_increase) + ")\n\n")
    file.write("Greatest Decrease in Profits: " + str(month_greatest_decrease) + " ($" + str(greatest_decrease) + ")")
