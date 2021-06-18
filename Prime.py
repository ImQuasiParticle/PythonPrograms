from math import*
def fun1(n):
    # TC of o(n)
    count = 0 
    for i in range(1,n+1): 
        if n%i==0:
            count = count + 1
    if count==2:
        return True
    else :
        return False 

def fun2(n):
    if n == 0 or n == 1: #TC of o(1)
        return False
    if n == 2 or n == 3: #TC of o(2)
        return True
    if n % 2 == 0  or n % 3 == 0:
        return False
    for i in range(5,int(sqrt(n))+1): #TC of o(sqrt(n))
        if n % i == 0 or n % i+2 == 0:
            return False
    return True

print("Enter the value of test case T")
t = int(input())
while t:
     print("Enter the value of N")   
     n= int(input())
     p = fun2(n)
     if p:
         print("{} is a Prime number".format(n))
     else:
         print("{} is not a Prime number".format(n))
     t = t-1
