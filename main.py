from __future__ import print_function                     # Standard print function import
from collections import Counter                           # Dictionary like function
from prettytable import *                                 # Generating ASCII based tables
  
  
file_name = input("File name: ")                          # Gets file name from user input
doc = open(file_name, "r")                            
sampleLogEntry = doc.read()                               # Gets file contents
  
worms = [ ]                                               # Creates a empty list (Placeholder) of all worms found in document

with open(file_name) as logFile:      
    for eachRow in logFile:   
        if 'worm' in eachRow.lower():                     # Finds all strings starting with "Worm"
            split_data = eachRow.split(" ")  
            last_part = split_data[len(split_data)-3]     # Gets the name of the worm
            worms.append(last_part)                       # Puts just the worm name in the list


worm_count = Counter(worms)                               # Creates a dictionary like entry of words and their occurence
worm_sort = worm_count.most_common()                      # Sorts by occurence & converts the counter to a list of lists because im fimmiliar with lists! 
  
  
x = PrettyTable()                                         # Creates a instance of a ASCII table
x.field_names = [ "Worm", "Count" ]                       # Creates ASCII table column headers
  
i = 0                                                     # Length of list index for itteration purposes
for worm in worm_sort:                                    # Loops through all lists in list
    while i != len(worm_sort):                            # Stops loop at total number of list items
        i=i+1                                             # Increases the loop index by 1
        x.add_row([worm_sort[i-1][0], worm_sort[i-1][1]]) # Itterates through the list starting at [0][0] 

print(x) # Prints ASCII table


