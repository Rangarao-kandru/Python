def binary2decimal(binary):

    decimal = 0

    i = 0

    while binary != 0:

        dec = binary % 10

        decimal = decimal + dec * pow(2, i)

        binary = binary // 10

        i += 1

    return decimal





result = binary2decimal(10011)

print(result)

