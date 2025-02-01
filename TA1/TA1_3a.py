count = 5

for i in range(1, count+1):
    for j in range(count - i):
        print(" ", end="")
        
    for k in range(1, i + 1):
        print(k, end="")
        
    print()
   