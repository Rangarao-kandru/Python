5)Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t 
use any of the forbidden letters.

def fun(a,b):
    for a  in b:
        if b not in a:
            return False
        else:
            return True

a=input("Enter a word : ")
b=input("Enter a string : ")
res=fun(a,b)
print(res)

