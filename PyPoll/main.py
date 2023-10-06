import os
import csv

bank_csv = os.path.join('..','PyPoll','resources','election_data.csv')

#sets variables for canidates vote count
CCSVotes = 0
DDVotes = 0
RADVotes = 0


totalVotes = 0
with open(bank_csv, 'r') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csv_reader)
    
    for row in csv_reader:  #Keeps count of the amount of votes each canidate recieved
        
        totalVotes+=1
        if (row[2] == "Charles Casper Stockham"):
            CCSVotes +=1
        elif (row[2] == "Diana DeGette"):
            DDVotes +=1
        elif (row[2] == "Raymon Anthony Doane"):
            RADVotes +=1
Dictionary = { #creates a dictionary to hold all the votes for each canidate
   "Charles Casper Stockham": CCSVotes,
    "Diana DeGette": DDVotes,
    "Raymon Anthony Doane": RADVotes    
}
#this code goes through the dictionary find the value with the highest number and returns the key
winner = max(zip(Dictionary.values(), Dictionary.keys()))[1] # this code came from https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
print(winner)
    
        
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
print(f"Charles Casper Stockham: {round((CCSVotes/totalVotes)*100,3)}% ({CCSVotes})")
print(f"Diana Degette: {round((DDVotes/totalVotes)*100,3)}% ({DDVotes})")
print(f"Raymon Anthony Doane: {round((RADVotes/totalVotes)*100,3)}% ({RADVotes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

f = open("PyPoll.txt", "a")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(totalVotes) + "\n")
f.write("-------------------------\n")
f.write("Charles Casper Stockham: " + str(round((CCSVotes/totalVotes)*100,3)) + "%" + " (" + str(CCSVotes) + ")" + "\n")
f.write("Diana Degette: " + str(round((DDVotes/totalVotes)*100,3)) + "%" + " (" + str(DDVotes) + ")" + "\n")
f.write("Raymon Anthony Doane: " + str(round((RADVotes/totalVotes)*100,3)) + "%" + " (" + str(RADVotes) + ")" + "\n")
f.write("-------------------------\n")
f.write("Winner: " + str(winner) + "\n")
f.write("-------------------------\n")
f.close()