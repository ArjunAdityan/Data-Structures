def gcd(a,b):
    a,b=max(a,b),min(a,b)
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
print(gcd(n1,n2))