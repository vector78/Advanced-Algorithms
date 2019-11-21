#Devin Koehl
#CS652 - Advanced Algorithms
#Problem 13
  

'''
READ ME:

You can just run this program in your command line by
cd to directory
type in command line: python power.py

This program will return the number of recurive calls
with the power of a number when run in the command line.
Sample output: (-2, 10) = 2014- takes 10 recursive calls
              
help from:
https://codereview.stackexchange.com/questions/120082/python-power-function
https://docs.python.org/2/library/math.html
https://codereview.stackexchange.com/questions/184260/check-if-a-given-number-n-is-a-power-of-k

This was written in the IDE Pyzo version 2.4. 
'''
def power(x, y):
    '''
    @param: x - integer which is the base of the number you wish to exponeniate
    @ param y - non-negative integer which is the power to what you wish to multiply
    '''
    #Start a counter to count recursion
    power.counter += 1;
    
    #If the base case, return 1
    if y == 0:
        return 1
        
    #Else, recursively call the power function
    if y >= 1:
        return x * power(x, y - 1)
      
#############################TEST CASE#############################
#Counts the number of recursive calls
power.counter = 0
answer = power(-2, 10)
print("-2 to the power of 10 takes " + str(power.counter) + " recursive calls and the answer is " + str(answer))

power.counter = 0
answer2 = power(3, 100)
print("3 to the power of 100 takes " + str(power.counter) + " recursive calls and the answer is " + str(answer2))

power.counter = 0
answer3 = power(14, 50)
print("14 to the power of 50 takes " + str(power.counter) + " recursive calls and the answer is " + str(answer2))

  
  