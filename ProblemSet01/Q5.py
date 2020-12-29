a=int(input("Enter an integer "))

root=0

pwr=0





while root<=a:

    root+=1

    while pwr<6:

        pwr+=1

        if root**pwr==a:

            print(root,pwr)



    pwr=0