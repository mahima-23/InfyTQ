# Assignment on recursion - Level 1 - Q1


def is_palindrome(word):
    word1=word.lower()
    word_rev=word1[::-1]
    wordrev=word_rev.lower()
    if word1==wordrev:
        return True
    return False
    
   
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
