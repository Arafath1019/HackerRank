n = input()
n = int(n)
arr = [int(x) for x in input().split()]
output = []
for x in arr:
    if x not in output:
        output.append(x)

output.sort()

print(output[len(output)-2])