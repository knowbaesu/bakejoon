s = int(input())
x = list(map(int, input().split()))
sum = 0
count = 0
for i in x:
    sum = sum+i
avr = sum / s
for i in x:
    if i > avr :
        count = count+1
l = round((count/s * 100),3)
print(l,"%",sep='') 