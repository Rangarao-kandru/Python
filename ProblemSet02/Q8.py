def eval_loop():

    while True:

        n = input("Enter a string:")

        if n == 'done':

            break

        else:

            result = eval(n)

            print(result)

    print(result)



eval_loop()


