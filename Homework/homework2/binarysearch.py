#Devin Koehl
#CS652 - Advanced Algorithms - Homework 2
#Question 14

'''
READ ME:

THIS PROGRAM TAKES INPUT FROM USER!!!! Must also ensure 100000.txt is in the 
same folder as the program

You can just run this program in your command line by

cd to directory
type in command line: python binarysearch.py

When run in the command line, it will ask
which number would you like to search for using binary search, input a number.
If you DO NOT input a number, it will fail and say YOU MUST ENTER AN INTEGER! 

The program will output if the element was found, how long it took to find in seconds, and 
how many recursive calls were invoked

After it outputs this information, it will ask the user a number to use ternary search on.
It will then again output if the element is found, how long it took to find in ms, and
how many recursive calls were invoked.

This was written in the IDE Pyzo version 2.4. 
*sources for help:

https://cs.stackexchange.com/questions/29755/why-is-binary-search-faster-than-ternary-search
http://www.techiedelight.com/ternary-search-vs-binary-search/
https://www.geeksforgeeks.org/binary-search-preferred-ternary-search/

'''


#Import time to measure the time in ms
import time
import datetime

#Definine a function binary search
def binarySearch(array,first,last,searchvalue):
    '''
    @param: array - the array of integers for which to binary search
    @param: first - the element marking the start index of the array
    @param: last - the element marking the end index of the array
    @searchvalue: the element to query the array and search for
    
    Source: Cormen algorithm on BinarySearch
    '''
     
    #Start a counter to count the number of recursive calls 
    binarySearch.counter += 1
    
    #While the last element is greater than the first element, do the following:
    if (last >= first):
   
        #Calculate the middle element
        midpoint = first + (last - first)//2;
  
        #If the index of the midpoint is equal to our search value, we have found the element we are searching for
        if (array[midpoint] == searchvalue):
            return midpoint
  
        #If the index at the midpoint is GREATER than what we are searching for we know it has to be in the
        #first half of the array, so we use first as a starting point and index to midpoint-first
        if (array[midpoint] > searchvalue): 
            return binarySearch(array, first, midpoint-1, searchvalue)
  
        #The last case must be if the index is greater. This means the value lies in the second half of the array
        return binarySearch(array, midpoint+1, last, searchvalue)

    #Else the value does not exist in the list
    return -1
 

def ternarySearch(array, first, last, searchvalue):
    '''
    Replicate the above code instead with a 3 way split
    
    @param: array - the array of integers for which to binary search
    @param: first - the element marking the start index of the array
    @param: last - the element marking the end index of the array
    @searchvalue: the element to query the array and search for
    
    Source: Cormen algorithm on BinarySearch but using it to extend ternary search
    '''
    ternarySearch.counter += 1
    
    #same as above, while the last element is greater than the first
    if (last >= first):
   
        #Calculate the middle element
        middle = first + (last - first)//3
            
        #Calculate a second middle to partition the array into 3 parts
        middle2 = middle + (last - first)//3
 
        #If the element in the middle is our search value, we have found the value
        if (array[middle] == searchvalue):  
            return middle
 
        #if the element in our other array is the search value, we have found the value
        if (array[middle2] == searchvalue):
            return middle2
 
        #if the element is greater than the middle, recursively find it in the first half
        if (array[middle] > searchvalue):
            return ternarySearch(array, first, middle-1, searchvalue)
 
        #if the element is less than our second middle, recursively find it in the second half
        if (array[middle2] < searchvalue): 
            return ternarySearch(array, middle2+1, last, searchvalue)
        
        #If not, it must be the case it is between the middle two calculated elements
        return ternarySearch(array, middle+1, middle2-first, searchvalue)
   
  
    return -1;
  
######################READ IN TEXT FILE######################

#The text file to read into Python
with open('100000.txt') as f:
    content = f.read()
    array = content.split()
    array = list(map(int, array))
 

#####################BINARY SEARCH#################################

#Start the timer to measure how long it takes
start = datetime.datetime.now()

#Make the user input the number they wish to search for
try:
    x = int(input("Enter number for binary search: "))
except ValueError:
    print("YOU MUST ENTER AN INTEGER! WHY U DO DIS?")
    
    
#Counts the number of recursive calls
binarySearch.counter = 0

#Taking the results from the user, find the element
result1 = binarySearch(array, 0, len(array)-1, x)


#If the element doesn't exist, let the user know
if result1 != -1: 
    print ("Element is present at index %d" % result1 )
else: 
    print ("Element is not present in array")

#Calculate the total time taken
end = datetime.datetime.now()
elapsed = end - start

#Print how long in microseconds 
#Prints how many recursive calls were made
print("Binary search made: " + str(binarySearch.counter) + " recursive calls and took " + str(elapsed.seconds) + " s to complete")


######################TERNARY SEARCH######################

#Start the timer to measure how long it takes
start2 = datetime.datetime.now()

#Make the user input the number they wish to search for
try:
    x = int(input("Enter number for ternary search: "))
except ValueError:
    print("YOU MUST ENTER AN INTEGER! WHY U DO DIS?")
    
    
#Counts the number of recursive calls
ternarySearch.counter = 0

#Taking the results from the user, find the element
result2 = ternarySearch(array, 0, len(array)-1, x)


#If the element doesn't exist, let the user know
if result2 != -1: 
    print ("Element is present at index %d" % result2 )
else: 
    print ("Element is not present in array")

#Calculate the total time taken
end2 = datetime.datetime.now()
elapsed2 = end2 - start2


#Print how long in microseconds i
#Prints how many recursive calls were made
print("Ternary search made: " + str(ternarySearch.counter) + " recursive calls and took " + str(elapsed2.seconds) + " s to complete")


