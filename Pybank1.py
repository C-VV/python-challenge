# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:05:14 2019

@author: Cody
"""


import os
import csv

bud_data = os.path.join("budget_data.csv")

months = []
net_total = []


with open(bud_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
   
    
    for row in csvreader:
        
        months.append(row[0])
        net_total.append(row[1])
total= 0 
for i in range(0,len(net_total)):  
    total = total+ int(net_total[i])
 
    
A = [int(net_total[i+1])-int(net_total[i])for i in range (len(net_total)-1)]
Avg = (sum(A) / (len(net_total)-1))

Min_diff = (min(A))
Max_diff = (max(A))
	
print("Finicial Data",
     "----------------------------------------------",sep = "\n")
print ("Months:", len(months))
print ("Net Total", total)
print ("Average Difference", Avg)
print ("Greatest Increase in profits",Max_diff)
print("Greatest Decrease in profits", Min_diff)

file = open("Output.txt","w")
file.writelines(f"Finicial Data\n")
file.writelines(f"----------------------------------------------\n")
file.writelines(f"Months:{ len(months)}\n")
file.writelines(f"Net Total:{ total}\n")
file.writelines(f"Average Difference: {Avg}\n")
file.writelines(f"Greatest Increase in profits:{Max_diff}\n")
file.writelines(f"Greatest Decrease in profits: {Min_diff}\n")
file.close()


