t = int(input())
while t:
    n = int(input())
    if n % 2 == 0:
        sum = 0
        for i in range(2, n+1, 2):
            sum += 1/i
        print(f"{sum:.{6}f}")
    else: 
        sum = 0
        for i in range(1, n+1, 2):
            sum += 1/i
        print(f"{sum:.{6}f}")
    t -= 1