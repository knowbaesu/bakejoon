x = input()
c = x
count = 0
while True:
   if len(c)==1:
      c= "0"+ c   # c 가 한자리수 일 경우 앞에 0을 붙임
   plus = str(int(c[0]) + int(c[1])) #뒷자리 수 구하기. 두 수를 합한것만 적어줌.
   c = c[-1] + plus[-1] # C의 뒷자리, 즉 수의 뒷자리를 앞으로 내세우고 두수를합한것의 뒷자리를 뒤로배치. 여기서 중요한건 -1 숫자가 한자리일 경우 1로 하게되면 오류가발생(0부터시작인데 1은 없으므로) . 따라서 -1로 불러와야한다.
   count = count +1
   if c == x:
      break
print(count)


