count = int(input())
g = list(map(int, input().split()))
min = g[0]
max = g[0]
for i in g[1:] :
    if i > max :
        max = i
    elif i < min :
        min = i
print(min, max)