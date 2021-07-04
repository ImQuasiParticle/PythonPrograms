def intToBin(n):
    return str(bin(n))[2:]

def binToInt(n):
    return int(n,2) 
print("Enter the number of Test Cases")
t = int(input())
while t:
    print("Enter an Integer")
    a = int(input())
    print(intToBin(a))
    t = t-1