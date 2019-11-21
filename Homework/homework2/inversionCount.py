#Devin Koehl
#CS652 - Advanced Algorithms - Homework 2

'''
READ ME:

You can just run this program in your command line by

cd to directory
type in command line: python inversionCount.py

TEXT FILES MUST BE IN THE SAME Directory! You will need

10.txt, 50.txt, 100.txt, 150.txt, 200.txt, 250.txt, 300.txt, 350.txt,
400.txt, 450.txt, 500.txt, 1000.txt, 5000.txt, 10000.txt, 100000.txt
This program will run brute force count inversions and also divide and conquer count inversions. 

It reads in the text files given for the question and will output the number of inversions and the time
in seconds it takes to run each. You must change the name to whatever text file you want it to process (I want
to make this more dynamic, still learning Python!)

Program written in IDE Pyzo 2.4.

The Brute force method was straight forward, yet the divide and conquer was tough for me.

I became flustered and stuck and had to use this person's code and also used the Merge Algorithms from Cormen book. Sorry!!! Just wanted to turn in something atleast :/ 

Cormen book page 31, merge algorithm
Cormen book page 24, merge-sort algorithm

https://codereview.stackexchange.com/questions/12922/inversion-count-using-merge-sort
'''

#Import time to measure the time in ms
import time
import datetime


def invCountBruteForce(array, number): 
    
    #Set the number of inversions to 0
    inversionCount = 0
    
    #Loop through the arrat
    for i in range(number):
         
        
        for j in range(i+1, number): 
            
            #if the element is greater, increase the counter
            if (array[i] > array[j]): 
                
                #Increment the counter
                inversionCount += 1
  
    #Return the number of inversions
    return inversionCount 
 
#Initialize a global variable count
count = 0

def merge_sort(A):
    
    #If the array does not have enough elements, return the array
    if len(A) < 2: 
        return A 
        
    #Find the middle element
    middle = len(A) // 2 
    
    #Return the merge of the two half of the array sorted
    return merge(merge_sort(A[:middle]), merge_sort(A[middle:])) 

#Merge, from Cormen page 31 and also help from resource listed above
def merge(l, r):
    
    #Glocal variable to count the inversions
    global count
    
    #Initialize our array that we will use
    result = [] 
    
    #Initialize our counters to 0
    i = 0 
    j = 0
    
    #While this condition is true, append the values
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            
            #We know we have an inversion if this is met
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result

################################READ IN FILES####################################
#I really don't think this is the most efficient way to do this but I'm on a time crunch so oh well

#The text file to read into Python
with open('10.txt') as f:
    content = f.read()
    array = content.split()
    array_10 = list(map(int, array))
    
#The text file to read into Python
with open('50.txt') as f:
    content = f.read()
    array = content.split()
    array_50 = list(map(int, array))
    
#The text file to read into Python
with open('100.txt') as f:
    content = f.read()
    array = content.split()
    array_100 = list(map(int, array))
    
    
#The text file to read into Python
with open('150.txt') as f:
    content = f.read()
    array = content.split()
    array_150 = list(map(int, array))

#The text file to read into Python
with open('200.txt') as f:
    content = f.read()
    array = content.split()
    array_200 = list(map(int, array))
    
#The text file to read into Python
with open('250.txt') as f:
    content = f.read()
    array = content.split()
    array_250 = list(map(int, array))
    
#The text file to read into Python
with open('300.txt') as f:
    content = f.read()
    array = content.split()
    array_300 = list(map(int, array))
        
#The text file to read into Python
with open('350.txt') as f:
    content = f.read()
    array = content.split()
    array_350 = list(map(int, array))
    
#The text file to read into Python
with open('400.txt') as f:
    content = f.read()
    array = content.split()
    array_400 = list(map(int, array))
    
#The text file to read into Python
with open('450.txt') as f:
    content = f.read()
    array = content.split()
    array_450 = list(map(int, array))

#The text file to read into Python
with open('500.txt') as f:
    content = f.read()
    array = content.split()
    array_500 = list(map(int, array))
 
#The text file to read into Python
with open('1000.txt') as f:
    content = f.read()
    array = content.split()
    array_1000 = list(map(int, array))

#The text file to read into Python
with open('5000.txt') as f:
    content = f.read()
    array = content.split()
    array_5000 = list(map(int, array))
  
#The text file to read into Python
with open('10000.txt') as f:
    content = f.read()
    array = content.split()
    array_10000 = list(map(int, array))

  
#The text file to read into Python
with open('100000.txt') as f:
    content = f.read()
    array = content.split()
    array_100000 = list(map(int, array))

    

###################################TESTING############################################
###################################DIVIDE AND CONQUER###################################
#Start the timer to measure how long it takes

start = datetime.datetime.now()

merge_sort(array_200)

end = datetime.datetime.now()
elapsed = end - start

#Print how long in microseconds 
#Prints how many recursive calls were made
print("The array using divide and conquer has " + str(count) + " inverions and took " + str(elapsed.microseconds) + " ms to run")

##################################BRUTE FORCE###########################################

start2 = datetime.datetime.now()

A = invCountBruteForce(array_200,len(array_200))

end2 = datetime.datetime.now()
elapsed2 = end2 - start2

print("The array using brute force has " + str(A) + " inverions and took " + str(elapsed2.microseconds) + " ms to run")

#50




  