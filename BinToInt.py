
def binToInt(n):
    return int(n,2) 
print("Enter the number of Test Cases")
t = int(input())
while t:
    print("Enter a Binary Number")
    a = int(input())
    print(binToInt(str(a)))
    t = t-1