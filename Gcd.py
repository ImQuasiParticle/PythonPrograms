def gcd(a,b): # gcd(10,20) = 10
    if a==0:
       return b
    return gcd(b%a,a)

def lcm(a,b):
    prod = a*b
    return prod//gcd(a,b)

print("Enter value of N")
n = int(input())
print("Enter value of M")
m = int(input())
g = gcd(n,m)
l = lcm(n,m)
k = 0
print("gcd = {} lcm = {}" .format(g,l))
