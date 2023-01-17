#importing needed packages 
import csv 
import os 


#set up path to get data
poll_csv = os.path.join('..','Resources', 'election_data.csv')

#open up the CSV file in order to read

with open(poll_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')

#initializing variables, need dictionary for unique candidates, and amount of votes for each
    results = {}
    total_votes = 0
    next(csvreader)


    # setting up loop to count total votes, and votes for each unique candidate 
    for rows in csvreader:
        
        total_votes += 1
        
        #reading the 3rd column in CSV file
        candidate = rows[2]

        #setting if else statement to cound total votes for each candidate
        if candidate in results:
            results[candidate] +=1
        else:
            results[candidate] =1
    
        



#testing to see if it prints out correctly for text file

print("\n Elections Results")
print("-------------------------\n")
print("Total Votes: " + str(total_votes) + "\n")    
print("-------------------------\n")

for values in results:
    percentage = round((results[values]/total_votes) * 100, 3)
    print(str(values) + ":", str(percentage) + "%", '(' + str(results[values]) + ') \n' )
winner = max(results, key = results.get)

print("-------------------------\n")
print("Winner: " + str(winner))
print("\n-------------------------")


#creating new file called "poll_results.txt" and placing it in Analysis folder

file2 = os.path.join('..', 'Analysis', 'poll_results.txt')


#opening file in order to write in it
with open(file2, 'w') as file:
    file.write("\nElections Results\n\n")
    file.write("-------------------------\n\n")
    file.write("Total Votes: " + str(total_votes) + "\n\n")


#using for loop to write out key and values from dictionary 
    for values in results:
        percentage = round((results[values]/total_votes) * 100, 3)
        file.write(f'{values}: {percentage}% ({results[candidate]})\n\n')

    file.write("-------------------------\n\n")
    file.write("Winner: " + str(winner))
    file.write("\n\n-------------------------")





    


    


