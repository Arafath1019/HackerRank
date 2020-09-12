a = input().strip()
a = int(a)
b = input().strip()
b = int(b)

if (1<= a <=10**10) and (1 <= b <= 10**10):
    if a > b:
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print(b+a)
        print(b-a)
        print(b*a)

