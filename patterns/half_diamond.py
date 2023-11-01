n=5

for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    for j in range(n-1):
        print(" ",end="")
    print("\n")
for i in range(n-1):
    for j in range(n-1-i):
        print("* ",end="")
    for j in range(i+1):
        print(" ", end="")
    print("\n")
    


