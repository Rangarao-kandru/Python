  def sumOfDigits(s):

    list1 = []

    try:

        for i in s:

            if i.isdigit():

                list1.append(int(i))

        print(sum(list1))



    except ValueError as ve:

        print("Invalid ")



s='a2b3c'

sumOfDigits(s)

