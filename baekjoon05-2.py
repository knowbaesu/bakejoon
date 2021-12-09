x = int(input())
c = x #가장 핵심인 부분임. 결국 c==x를 최종목표로 두고 x는반복문에 쓰지 않음
count = 0

while True:
    a = c // 10 # 십진수의 몫은 앞자리
    b = c % 10 # 십진수의 나머지는 뒤자리
    g = (a+b) % 10  #두개합한수의 나머지 -> 뒤자리
    c = (b * 10) + g # 십진수에서 뒷자리를 앞자리로 변경하는건 *10 + 뒤자리 

    count = count+1
    if(c == x):
        break 
print(count)