n=int(input("type a binary number:-"))
k=n
if set(str(n)) - {'0', '1'}:
    print("invalid binary number")
    exit()
y=0
i=0
while(n!=0):
    x=n%10
    n=n//10
    y=y+(x)*2**i
    i=i+1
print(f"the decimal form of the binary number {k} is {y}")

