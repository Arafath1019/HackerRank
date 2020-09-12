n = input().strip()
n = int(n)

def myFunc(x):
    array = []
    while True:
        array.append(x-1)
        x = x-1
        if x == 0:
            break
    return array

array1 = myFunc(n)

array1 = array1[::-1]

for i in array1:
    print(i**2)
