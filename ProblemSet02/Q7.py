def isPalindrome(s):

    s1=s[::-1]

    if s==s1:

        print(s)

    else:

        print("not a palandrome")





s=str(input("Enter the string "))

isPalindrome(s)







------------------------------------or--------------------------------







def is_palindrome(s):

    if len(s)==1:

        print("palindrome")

    elif len(s) > 1:

        if s[0]==s[-1]:

            print('palindrome')

    else:

        print('not a palindrome')

s = input("enter the string: ")

is_palindrome(s)
