import os
import csv

bank_csv = os.path.join('..','PyPoll','resources','election_data.csv')
CCSVotes = 0
DDVotes = 0
RADVotes = 0
canList = []

totalVotes = 0
with open(bank_csv, 'r') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csv_reader)
    
    for row in csv_reader:
        
        totalVotes+=1
        if (row[2] == "Charles Casper Stockham"):
            CCSVotes +=1
        elif (row[2] == "Diana DeGette"):
            DDVotes +=1
        elif (row[2] == "Raymon Anthony Doane"):
            RADVotes +=1
Dictionary = {
   "Charles Casper Stockham": CCSVotes,
    "Diana DeGette": DDVotes,
    "Raymon Anthony Doane": RADVotes    
}

winner = max(zip(Dictionary.values(), Dictionary.keys()))[1] # this code came from https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
print(winner)
    
    
canList.append(RADVotes)    
canList.append(DDVotes)
canList.append(CCSVotes)

mostVotes = max(canList)
        
        
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