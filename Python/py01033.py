import math

l, r = map(int, input().split())
for i in range(l, r+1, 1):
    for j in range(i+1, r+1, 1):
        for k in range(j+1, r+1, 1):
            if(math.gcd(i, j) == 1 and math.gcd(j, k) == 1 and math.gcd(k, i) == 1):
                print("(", end = "")
                print(i, end = ", ")
                print(j, end = ", ")
                print(k, end = ")\n")