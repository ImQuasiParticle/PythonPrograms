from math import*

def fun(n) : 
    #Time complexity of O(n)
    l = []
    for i in range(1,n+1):
        if  n%i==0 :
            l.append(i)
    return l

def fun1(n):
    #Time Complexity O(sqrt(n)) 
    l = set()
    for i in range(1,int(sqrt(n)+1)):
        l.add(i)
        l.add(n//i)
    return list(l)

print("Enter The number of time you want to run the program")
t = int(input())
while t : 
    n = int(input())
    tcN  = fun(n) 
    tcSN = fun1(n)
    print("TC of n {}".format(tcN))
    print("TC of sqrt(n) {}".format(tcSN))
    t = t-1
