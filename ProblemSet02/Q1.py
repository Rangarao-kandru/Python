def gcd(a,b):

    if b==0:

        return a

    else:

        return gcd(b, a%b)



"""a=int(input("Enter the 1st value : "))

b=int(input("Enter the 2nd value : "))

print(gcd(a,b))"""





print(gcd(int(input("Enter the 1st value : ")),int(input("Enter the 2nd value : "))))
