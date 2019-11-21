#Devin Koehl
#CS652 - Advanced Algorithms

def monotonic(A):
    
    '''
    @param: A of type Array
    @return: Boolean - True if monotonically increasing or decreasing
                       False otherwise
    '''
    #define counters for each case#
    lc = 0
    rc = 0
    
    #loop through the input array
    for i in range(len(A)-1):
        
        #if the second element is less than the first, we have a decreasing case and we count
        if (A[i] < A[i+1]):
            lc += 1
            
        #else we have an increasing case and we count
        elif (A[i] > A[i+1]):
            rc+=1
            
        #Now if BOTH of these counters are greater than zero, it is such the case that it is both increasing and decreasing and this
        #cannot be so. So it MUST be false.
        if (rc > 0 and lc > 0):
      
            return False
        
    #Return false otherwise
    return True
  
  
####################TEST CASES######################  
s = [4,5,1,1,1]
s2 = [4,5,6,7,1,2]
s3 = [1,1,1]
s4 = [1,2,3,4,5]
s5 = [5,4,3,2,1]
print(monotonic(s))
print(monotonic(s2))
print(monotonic(s3))
print(monotonic(s4))
print(monotonic(s5))
    
