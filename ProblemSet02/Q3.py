def factI(n):

	"""Assumes that n is an int > 0

	Returns n!

	Uses Iterative Implementation"""

	

def factR(n):

	"""Assumes that n is an int > 0

	Returns n!

	Uses Recursive Implementation"""







def factR(a):

    if a==0:

        return 1

    else:

        return a*factR(a-1)



print(factR(4))



---------------------------------------------or----------------------------





def factI(a):

    if a==0:

        return 1

    temp=a

    for i in range(1,a):

        if a>0:

            temp=temp*(a-1)

            a=a-1

    return temp

print(factI(4))
