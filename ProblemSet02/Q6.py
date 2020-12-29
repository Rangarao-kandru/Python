def findAnEven(list1):

    try:

        for i in list1:

            if i%2==0:

                print("The even numbers are ",i)

                exit()

        raise ValueError



    except ValueError as ve:

        print("Enter atleast one even ")



list1=[1,3,5,9]

findAnEven(list1)

