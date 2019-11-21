#Devin Koehl
#CS652 - Advanced Algorithms
import string 

def reverse(s1):
    '''
    @param: s1 of type string
    @return: the reverse of s1
    '''
    return s1[::-1]


def palindrome(s):
    '''
    @param: s of type string
    @return: is s a palindrome?
    '''
    #First we need to strip all commas and other non-alphanumeric characters
    remove_na = set(string.ascii_letters)
    
    '''The join function - syntax -
    Source: https://www.geeksforgeeks.org/join-function-python/
    The join() method is a string method and returns a string in which the 
    elements of sequence have been joined by str separator.          
    Syntax: string_name.join(iterable) string_name: It is the name of string 
    in which joined elements of iterable will be stored.
    '''
    remove_ws = ''.join([ch for ch in s if ch in remove_na])
    
    #Make lowercase so this is not case sensitive and we are comparing only all lower case letters
    final_string = remove_ws.lower()
    
    #If the input string is equal to the reverse of the string, it is a palindrome.
    if final_string == reverse(final_string):
        return True
    #Else, it is not a palindrome
    else:
        return False

#######################TESTING##################################################
s = "meow"
s1 = "bob"
s2 = "KAYAK!KAYAK"
s3 = "MaDaM, !I'm ADAM"
s4 = ""
print(palindrome(s))
print(palindrome(s1))
print(palindrome(s2))
print(palindrome(s3))
