
def is_power(a,b):



    if a % b == 0:                          

        for i in range(1,a):                 

            if b ** i == a:                   

                return True

    else:

        return False





result = is_power(int(input()),int(input()))

print(result)
