import random

randNum = random.randint(1,100)
count = 0

while True :
    inputNum = int(input("1~100까지 숫자를 입력하세요: "))
    count +=1
    if randNum == inputNum :
        break
    elif randNum > inputNum :
        print(inputNum, "보다 큽니다!")
    else :
        print(inputNum, "보다 작은수")
print(count, "번만에 정답을 맞추셨어요!")