# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:07:50 2019

@author: Cody
"""
import os
import csv

e_data = os.path.join("election_data.csv")

Total_id=[]
County = []
Candidate = []




with open (e_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    next(csvreader)
    
    for row in csvreader:
        Total_id.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        
    Total_votes = len(Total_id)
    Candidate_list = set(Candidate)
    print(Candidate_list)
    
    Khan = (Candidate.count("Khan"))
    Correy = (Candidate.count("Correy"))
    Li = (Candidate.count("Li"))
    Otooley = (Candidate.count("Otooley"))
    
    Khan_Per = round(Khan / Total_votes, 2) * 100
    Correy_Per = round(Correy / Total_votes, 2) * 100
    Li_Per = round(Li / Total_votes, 2) * 100
    Otooley_Per = round(Otooley / Total_votes, 2) * 100
    
    import statistics
    from statistics import mode
    
    winner = mode(Candidate) 
    
    


print("Election Results"
     "----------------------------------------------",sep = "\n")
print("Total_votes:",Total_votes)
print("---------------------------------")
print ("Khan:",Khan_Per,"Percent","(",Khan,")")
print ("Correy: ", Correy_Per, "Percent", "(", Correy, ")")
print ("Li: ", Li_Per, "Percent", "(", Li, ")")
print ("O'Tooley: ", Otooley_Per, "Percent", "(", Otooley, ")")

print("---------------------------------")
print ("The winner is", winner)

file = open("OutputElection.txt","w")
file.writelines(f"Election Results\n")
file.writelines(f"----------------------------------------------\n")
file.writelines(F"Total_votes:{Total_votes}\n")
file.writelines(f"----------------------------------------------\n")
file.writelines(f"Khan:{Khan_Per}% ({Khan})\n")
file.writelines(f"Correy:{Correy_Per}%({Correy})\n")
file.writelines(f"Li:{Li_Per}% ({Li})\n")
file.writelines(f"O'Tooley:{Otooley_Per}% ({Otooley})\n")
file.writelines(f"The winner is: {winner}\n")
file.close()
        

