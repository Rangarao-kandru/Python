
def newtonsqrt(a,x):

    y=(x+a/x)/2

    return y



a = int(input("Enter a number:"))

x = int(input("Enter another number:"))

res = newtonsqrt(a,x)

print(res)