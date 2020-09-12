n = input().strip()
n = int(n)

if 1 <= n and n <= 100:
    if n % 2 != 0:
        print("Weird")
    elif 2<= n and n <= 20: 
        if 2 <= n and n <= 5:
            print("Not Weird")
        else:
            print("Weird")
    else: 
        print("Not Weird")