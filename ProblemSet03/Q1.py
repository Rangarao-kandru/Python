1)A string slice can take a third index that specifies the "step size;" that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'

def isPal(a):
    b=a[::-1]
    print(b)
    if a==b:
     return "Its a palindrome
    else:
        return "Its not a palindrome"

a=str(input("Enter the string : "))
print(isPal(a))

