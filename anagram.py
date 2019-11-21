#Devin Koehl
#CS652 - Advanced Algorithms
import string 

    
def anagram(s1, s2):
    '''
    @param: s1 of type string
    @param: s2 of type string
    @return: Is s2 an annogram of s1?
    
    The join function - syntax -
    Source: https://www.geeksforgeeks.org/join-function-python/
    The join() method is a string method and returns a string in which the 
    elements of sequence have been joined by str separator.          
    Syntax: string_name.join(iterable) string_name: It is the name of string 
    in which joined elements of iterable will be stored.
    
    Resource: How to remove alpanumeric characters in Python 
    https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
    
    Resource: How to sort letters in a string:
    https://stackoverflow.com/questions/15046242/how-to-sort-the-letters-in-a-string-alphabetically-in-python
    '''
    #First, we need to remove all characters that are not alphabetic.
    remove_ws = set(string.ascii_letters)
    
    #Now we can sort each string, if they contain the same letters they will contain the same letters in the sorted array
    #lowercase everything so we can avoid things being case sensitive
    s1_sort = ''.join(sorted(s1)).lower()
    
    #Sort the second string to compare to the first
    #avoid things so we can avoid being case sensitive
    s2_sort = ''.join(sorted(s2)).lower()
    
    #compare the two strings
    if s1_sort == s2_sort:
        return True
    else:
        return False
        

#######################TESTING##################################################
s1 = "palindrome"
s2 = "dromepalin"
s3 = "fried"
s4 = "fired"
s5 = "sadder"
s6 = "dreads"
s7 = "dude"
s8 = "sweet"
print(anagram(s1,s2))
print(anagram(s3,s4))
print(anagram(s5,s6))
print(anagram(s7,s8))

