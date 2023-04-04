count_input = int(input("입력값: ")) #입력값을 저장하는 함수
count = count_input    #실질적인 카운트에 사용되는 변수
i = 1   #더해지는 수

while count > 0:    #계산
    i += i
    count -= 1

print("input: s(" + str(count_input) + ") =", i)
