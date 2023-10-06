import os
import csv


bank_csv = os.path.join('..','PyBank','resources','budget_data.csv')

totalMonths = 0
total = 0

sum1 = 0
sum2 = 0
counter = 0
rowDate = [] #holds dates
rowData = [] #hold original profit/loss data
rowData2 = [] #hold data for increase
rowData3 = [] # holds data for decreases
greatestInc = 0
greatestDec = 0
with open(bank_csv, 'r') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csv_reader)
    counter = 0
    counter2 = 0
    for row in csv_reader:
        
        
        rowData.append(row[1]) #makes an array of the unaltered data
        rowDate.append(row[0]) #makes an array of the dates
        totalMonths +=1
        total += int(row[1])
        #this code creates the two arrays to find the average change
        if counter == 0:
            sum1 = sum1
            counter +=1
        else:
            sum1 += int(row[1])
            
 
        if counter2 ==85:
            sum2 = sum2
        else:
            sum2 += int(row[1])
            counter2+=1
        
    
  
    for x in range(85): #create array of the difference between the values to find the greatest increase
        
        if (int(rowData[x]) < int(rowData[x+1])):
            rowData2.append(int(rowData[x+1])-int(rowData[x]))
        else:
            rowData2.append(None) #appends a null value so that the array is the same size as the date array
      
        
        
         
    for x in range(85): #create array of the difference between the values to find the greatest decrease
    
        if (int(rowData[x]) > int(rowData[x+1])):
  
            y = int(rowData[x]) - int(rowData[x+1])
            rowData3.append(abs(y))
        else:
            rowData3.append(None) #appends a null value so that the array is the same size as the date array
        
            
        
        
            
              
            
       
    for x in rowData2: #sorts through data to find the largest vaslue
        if (x != None):
            if (greatestInc < x):
                greatestInc = x
            else:
                greatestInc = greatestInc
            
    for x in rowData3: #sorts through data to find smalles value
        if (x != None):

            if (greatestDec < x):
                greatestDec = x
            else:
                greatestDec = greatestDec
            
    #finds index in the array and its matching index in the array of dates        
    greatestIncDate = rowData2.index(greatestInc) + 1
    greatestDecDate = rowData3.index(greatestDec) +1
    
 
    
    avgChange = round(((sum1-sum2)/85),2)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgChange}")
    print(f"Greatest Increase in Profits: {rowDate[greatestIncDate]} (${greatestInc})")
    print(f"Greatest decrease in Profits: {rowDate[greatestDecDate]}($-{greatestDec})")
    #writes values to a txt file
    f = open("PyBank.txt", "a")
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(totalMonths)+"\n")
    f.write("Total: " +str(total)+"\n")
    f.write("Average Change: "+ str(avgChange)+"\n")
    f.write("Greatest Increase in Profits: " + str(rowDate[greatestIncDate])+" ($" + str(greatestInc)+")\n")
    f.write("Greatest decrease in Profits: " + str(rowDate[greatestDecDate]) + "($-" +str(greatestDec)+ ")" )
    f.close()

 
    