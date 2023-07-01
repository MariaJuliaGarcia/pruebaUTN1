n=0
r=0
n=input (int("/n ingrese un número entero positivo"))     
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
print (factorial(4))

def factorial2(n):
    r = 1 
    for i in range (1, n+1):
        r = r * i
    return r
print (factorial2(4))