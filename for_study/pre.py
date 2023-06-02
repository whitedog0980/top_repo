
# # Lab 21 온도변환함수
# def F_to_C(temp_F):
#     temp_C = (5.0 * (temp_F - 32.0)) / 9.0
#     return temp_C

# temp_F = float(input("화씨온도를 입력하세요."))
# print(F_to_C(temp_F))

# Lab 23 소수찾기
# def is_prime(n):
#     for i in range(2, n): #1은 제외
#         if n%i == 0: #자기 자신을 제외한 수로 나눌때 나머지가 없는지? 
#             return False #만약 있다면
#     return True #만약 없다면(소수)

# n = int(input("정수를 입력하세요"))
# print(is_prime(n))

# # Lab 27 구의부피계산
# import math
# def sphere_V(r):
#     V = (4 / 3) * (math.pi * r * r * r)
#     return V

# r = float(input("구의 반지름을 입력하시오"))
# print(sphere_V(r))

# Lab 29 패스워드생성기
# import random

# def createPassword():
#     password = ""
#     alpa_nums = "qwertyuiopasdfghjklzxcvbnm1234567890"
#     for i in range(6):
#         rand_index = random.randrange(len(alpa_nums))
#         password = password + alpa_nums[rand_index]
#     return password

# print(createPassword())
# print(createPassword())
# print(createPassword())

# 실습과제 1
# def C_to_F(temp_C):
#     temp_F = ((temp_C * 9.0) / 5.0) + 32 #섭씨를 화씨로 바꾸는 계산식
#     return temp_F   #화씨값을 반환

# temp_C = float(input("섭씨온도를 입력하세요")) #섭씨를 입력받음
# print(C_to_F(temp_C))

# # 실습과제 2
# def is3Mult(n):
#     if n%3 == 0:
#         return True
#     return False #만약 없다면(소수)

# n = int(input("정수를 입력해주세요."))
# print(is3Mult(n))

# 실습과제 3
# import random

# def createPassword():
#     password = ""
#     alpa_nums = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
#     for i in range(8):
#         password = password + random.choice(alpa_nums)
#     return password

# print(createPassword())
# print(createPassword())
# print(createPassword())
# print(createPassword())
# print(createPassword())


# 최소공배수 구하기 20까지

# primes = []
# primes_mult = 1

# def is_prime(n): #소수인지 아닌기 판별하는 함수
#     for i in range(2, n): # 1은 제외
#         if n % i == 0: # 자기 자신을 제외한 수로 나눌 때 나머지가 없는지? 
#             return False # 만약 있다면
#     return True # 만약 없다면 = (소수)

# def all_primes(): # primes 리스트에 소수를 추가
#     for n in range(2, 21): # 1에서 20까지 모두 검사
#         if is_prime(n): # 만약 소수라면?
#             primes.append(n) #소수 리스트에 추가
#     return primes

# def lcm(): #최소 공배수 구하기
#     lcm = 1
#     for p in primes: #p는 소수 (primes 리스트 내부의)
#         max_count = 0
#         for i in range(1, 21): 
#             count = 0
#             while i % p == 0: 
#                 count += 1
#                 i //= p
#             max_count = max(max_count, count)
#         lcm *= p ** max_count
#     return lcm

# print(all_primes())
# print(lcm())


# #Lab_4_키워드 인수 연습 0412
# num_1, num_2 = input("두 수의 값을 띄어쓰기로 구분해서 입력해주세요.").split()

# def add(a, b):
#     return int(a) + int(b)
# def sub(a, b):
#     return int(a) - int(b)
# def mul(a, b):
#     return int(a) * int(b)
# def div(a, b):
#     return int(a) / int(b)

# result_1 = add(num_1, num_2)
# result_2 = sub(num_1, num_2)
# result_3 = mul(num_1, num_2)
# result_4 = div(num_1, num_2)

# print("더하기는", result_1, ",빼기는", result_2, ",곱하기는", result_3, ",나누기는", result_4)


# #Lab_6_온도변환기 0412
# def select_option():
#     print("""\'c\' 섭씨온도에서 화씨온도로 변환
# \'f\' 화씨온도에서 섭씨온도로 변환
# \'q\' 종료""")

# def c_to_f(tem_c):
#     return 9.0 / 5.0 * tem_c + 32

# def f_to_c(tem_f):
#     return (tem_f - 32) * 5.0 / 9.0

# choice = None
# while choice != "q":
#     select_option()
#     choice = input("메뉴에서 선택하세요.")
#     if choice == "c":
#         tem_c = float(input("섭씨온도 :"))
#         print("화씨온도 :", c_to_f(tem_c))
#     elif choice == "f":
#         tem_f = float(input("화씨온도 :"))
#         print("섭씨온도 :", f_to_c(tem_f))


# #Lab_17_상수 0412
# pi = 3.141592

# def main():
#     r = float(input("원의 반지름 :"))
#     print("원의 면적 :", area(r))
#     print("원의 둘레 :", len(r))

# def area(r):
#     return pi * r * r

# def len(r):
#     return r * 2 * pi

# main()


#Lab_추가_0412
# horizontal = float(input("가로길이를 입력해주세요 :"))
# vertical = float(input("세로길이를 입력해주세요 :"))

# def main():
#     if (horizontal < 0 or vertical < 0):
#         print("음수의 값을 입력했습니다.")
#     return horizontal * vertical

# print("넓이는", main(), "입니다.")


# #실습과제1 0412
# side_len = float(input("정사각형의 한변의 길이를 입력해주세요")) #값 입력

# def cul(): #계산
#     all_side_len = side_len * 4 #둘레 길이
#     area = side_len ** 2  #면적
#     return all_side_len, area
# result = list(cul())  #튜플에서 리스트로

# print("둘레의 길이는", result[0], "입니다.")
# print("면적은", result[1], "입니다.")


# #실습과제2 0412
# nums = list(map(int, input("정수인 숫자 4개를 띄어쓰기로 구분해서 적어주세요.").split()))
# #max, min함수에서 의도대로 작동시키기위해 map() 함수로 int자료형으로 변환및, list로 저장함

# def cul():
#     max_num = max(nums) #최댓값
#     min_num = min(nums) #최솟값
#     return max_num, min_num
# result = list(cul())  #반환값을 새로운 변수에 list형태로 저장

# print("가장 작은 숫자는", (result[1]), "이고,") #슬라이스를 사용해 list에서 값 선택
# print("기징 큰 숫자는", (result[0]), "이다.")


# #실습과제3 0412
# import math
# #첫번째 점 좌표 입력
# xy_1 = input("첫번째 점의 x와 y좌표를 차례대로 띄어쓰기로 구분해서 적으시오").split()
# #두번째 점 좌표 입력
# xy_2 = input("두번째 점의 x와 y좌표를 차례대로 띄어쓰기로 구분해서 적으시오").split()

# def between_distance(): #사이 거리 계산
#     x = float(xy_1[0]) - float(xy_2[0]) # x값의 차, 계산을 위해 float 자료형으로 변환
#     y = float(xy_1[1]) - float(xy_2[1]) # y값의 차, 계산을 위해 float 자료형으로 변환
#     #x, y값의 차를 제곱하여 더한값을 제곱근해서 거리값을 추출
#     distance = math.sqrt((x ** 2) + (y ** 2))
#     return distance

# print("두 점의 거리는", between_distance(), "입니다.") # 출력

# #실습과제4 0412
# tem_c = int(input("섭씨온도를 입력해주세요.")) #섭씨온도 입력

# #print 함수안에 lambda로 무명함수를 넣어서 출력
# print("화씨온도는", (lambda tem_c: 9.0 / 5.0 * tem_c + 32)(tem_c), "입니다.")


# #Lab8 0417
# weight = float(input("짐의 무게는 얼마입니까?"))

# if weight >= 20:
#     print("무거운 짐은 20,000원을 내셔야 합니다.")
# else:
#     print("짐에대한 수수료는 없습니다.")

# print("감사합니다.")


# # Lab12 0417
# num = int(input("정수를 입력하시오: "))
# if (num % 2) == 0:
#     print("입력된 정수는 짝수입니다.")
# elif (num % 2) == 1:
#     print("입력된 정수는 홀수입니다.")


# # Lab14 0417
# num_1 = int(input("첫 번째 정수: "))
# num_2 = int(input("두 번째 정수: "))

# if num_1 > num_2:
#     print("큰 수는", num_1)
# if num_1 < num_2:
#     print("큰 수는", num_2)
# else:
#     print("두수가 같습니다.")


# # Lab18 0417
# cost = float(input("구입 금액을 입력하시오: "))

# if cost >= 100000:
#     cost -= (cost/20)

# print("지불 금액은", cost, "입니다.")


# #Lab20 0417
# string = input("문자열을 입력하시오: ")
# str_len = len(string)

# if str_len % 2 == 1:
#     mid_ch_1 = string[0]
#     print("첫 문자는 :", mid_ch_1)
# else:
#     mid_ch_1 = string[-1]
#     print("마지막 문자는 :", mid_ch_1)


# #Lab25 0417
# st_point = int(input("이수한 학점수를 입력하시오: "))
# p = float(input("평점을 입력하시오: "))
# is_F = bool(input("(True,False)F가 없습니까?: "))

# if (st_point >= 140) and (p >= 2.0) and (is_F == True):
#     print("졸업이 가능합니다!")
# else:
#     print("졸업이 힘듭니다!")


# #Lab29 0417
# integer = int(input("정수를 입력하시오: "))

# if integer > 0:
#     print("입력된 정수는 양수입니다.")
# elif integer < 0:
#     print("입력된 정수는 음수입니다.")
# else:
#     print("입력된 정수는 0입니다.")


# #Lab33 0417
# id = ["wd0980", "wd0981", "wd0982"]
# pw = "0980"

# input_id = input("아이디를 입력하시오: ")
# if input_id in id:
#     input_pw = input("패스워드를 입력하시오: ")
#     if pw == input_pw:
#         input_pw = input("패스워드를 다시 한번 입력하시오: ")
#         if pw == input_pw:
#             print("정확히 저장되었습니다.")
#     else:
#         print("잘못된 비밀번호 입니다.")
# else:
#     print("알 수 없는 사용자 입니다.")


# # Lab35 0417
# month = int(input("월을 입력하시오: "))
# if month == 4 or month == 6 or month == 9 or month == 11:
#     m_days = 30
# elif month == 2:
#     m_days = 28
# else:
#     m_days = 31

# print("월의 날수는", m_days)

# # Lab37 0417
# year = int(input("연도를 입력하시오: "))

# if (year % 400) == 0:
#     print(year, "년은 윤년입니다.")
# elif not (year % 100) == 0:
#     if (year % 4) == 0:
#         print(year, "년은 윤년입니다.")
# else:
#     print(year, "년은 윤년이 아닙니다.")


# # Lab39 0417
# import math

# a = float(input("a ="))
# b = float(input("b ="))
# c = float(input("c ="))

# D = (b ** 2) - 4 * a * c
# if a == 0:
#     print("x =", -c / b)

# if D == 0:
#     print("x =", -b / (2 * a))
# elif D > 0:
#     print("x1 =", (-b + math.sqrt(D)) / (2.0 * a))
#     print("x2 =", (-b + math.sqrt(D)) / (2.0 * a))
# else:
#     print("실근이 존재하지 않음")


# #Lab43 0417
# import random

# print("숫자 게임에 오신 것을 환영합니다.")
# rand_num = random.randint(1, 100)
# guess_num = int(input("숫자를 맞춰보세요: "))

# if rand_num == guess_num:
#     print("정답입니다.")
# elif rand_num > guess_num:
#     print("작습니다.")
# else:
#     print("큽니다.")

# print("게임종료")


# # Lab45 0417
# import random

# user_rsp_str = input("(가위, 바위, 보) 중에서 하나를 선택하세요: ")
# if user_rsp_str == "가위":
#     user_rsp_int = 1
# elif user_rsp_str == "바위":
#     user_rsp_int = 2
# else:
#     user_rsp_int = 3

# com_rsp_int = random.randint(1,3)
# if com_rsp_int == 1:
#     com_rsp_str = "가위"
# elif com_rsp_int == 2:
#     com_rsp_str = "바위"
# else:
#     com_rsp_str = "보"

# print("사용자: " + user_rsp_str + "\n컴퓨터: " + com_rsp_str)

# if user_rsp_int == com_rsp_int:
#     print("비겼습니다.")
# elif (((user_rsp_int == 1) and (com_rsp_int == 2))
#     or ((user_rsp_int == 2) and (com_rsp_int == 3))
#     or ((user_rsp_int == 3) and (com_rsp_int == 1))):
#     print("졌습니다.")
# else:
#     print("이겼습니다.")


# #Lab추가 0419
# import math

# shape = input("도형을 입력하세요.(1: 사각형, 2: 삼각형, 3: 원): ")
# if shape == "1":
#     wide = float(input("가로: "))
#     height = float(input("세로: "))
#     print("면적: " + str(wide * height))
# elif shape == "2":
#     wide = float(input("가로: "))
#     height = float(input("세로: "))
#     print("면적: " + str(wide * height * (1/2)))
# else:
#     r = float(input("반지름: "))
#     print("면적: " + str((r ** 2) * math.pi))


# #실습과제1 0417
# height = int(input("키를 입력하세요 [cm]: ")) #키 입력

# if 130 <= height <= 195: #130 아상 195 미만이라면?
#     print("키" + str(height)+ "cm는 이용가능합니다.") #긍정 출력
# else: #이외로는
#     print("키" + str(height)+ "cm는 이용할 수 없습니다.") #부정 출력


# #실습과제2 0417
# month = int(input("월을 입력하세요 : ")) #월 입력

# if 3 <= month <= 5: #3월 이상 5월 이하일때?
#     print(str(month) + "월은 봄입니다.") #봄
# elif 6 <= month <= 8: #6월 이상 8월 이하일때?
#     print(str(month) + "월은 여름입니다.") #여름
# elif 9 <= month <= 11: #9월 이상 11월 이하일때?
#     print(str(month) + "월은 가을입니다.") #가을
# else: #이외(12월 아상, 2월 이하)일때?
#     print(str(month) + "월은 겨울입니다.") #겨울


# # 실습과제3 0418
# print("부모님과 함께왔나요?")
# is_with_p = input("1:예, 0:아니요: ") #부모님과 함께왔는지 여부
# age = int(input("나이를 입력하세요: ")) #나이 입력

# if (is_with_p == "1"): #부모님과 함께 왔을 때
#     if (age >= 10): #나이가 10 이상일때
#         print("영화를 볼 수 있습니다.") # 긍정1
# elif (is_with_p == "0"): #부모님과 함께 오지 않았을 때
#     if (age >= 15): #나이가 15 이상일때
#         print("영화를 볼 수 있습니다.") # 긍정2
# else:# 이외 (나이 미달)
#     print("영화를 볼 수 없습니다.") # 부정


# #실습과제4 0418
# gd_p = int(input("점수를 입력하세요: ")) #점수 입력
# gd = "" # 학점
# if gd_p >= 95: #95 이상이라면?
#     gd = "A+"
# elif 95 > gd_p >= 90: #90이상, 95미만이라면?
#     gd = "A0"
# elif 90 > gd_p >= 85: #85이상, 90미만이라면?
#     gd = "B+"
# elif 85 > gd_p >= 80: #80이상, 85미만이라면?
#     gd = "B0"
# elif 80 > gd_p >= 75: #75이상, 80미만이라면?
#     gd = "C+"
# elif 75 > gd_p >= 70: #70이상, 75미만이라면?
#     gd = "C0"
# elif 70 > gd_p >= 65: #65이상, 70미만이라면?
#     gd = "D+"
# elif 65 > gd_p >= 60: #60이상, 65미만이라면?
#     gd = "D0"
# else: #이외 (해당 점수 미만)
#     gd = "F0"

# print(str(gd_p) + "점은 " + gd + " 학점 입니다.") #출력

# #Lab27 0426
# mult = 1
# while mult <= 9:
#     print("3 * %d = %d" % (mult, 3 * mult))
#     mult += 1

# #Lab34 0426
# n = 0
# sum = 0
# score = 0
# print("종료하려면 음수를 입력하시오")

# while score >= 0:
#     score = int(input("성적을 입력하시오: "))
#     if score >= 0:
#         sum += score
#         n += 1

# if n > 0 :
#     aver = sum / n
# print("성적의 평균은 %f입니다." % aver)

# #Lab36 0426
# import random

# tries = 0
# number = random.randint(1, 100)

# print("1부터 100 사이의 숫자를 맞추시오")
# while tries < 10:
#     guess = int(input("숫자를 입력하시오: "))
#     tries = tries + 1
#     if guess > number:
#         print("낮음!")
#     elif guess < number:
#         print("높음!")
#     else:
#         break
# if guess == number:
#     print("축하합니다. 시도횟수=", tries)
# else:
#     print("정답은 ", number)


#Lab44 0426
# str = input("문자열을 입력하시오")

# alp = 0
# dig = 0
# spaces = 0

# for i in str:
#     if i.isalpha():
#         alp += 1
#     elif i.isdigit():
#         dig += 1
#     else:
#         spaces += 1

# print("알파벳 문자의 개수 =", alp)
# print("숫자 문자의 개수 =", dig)
# print("스페이스 문자의 개수 =", spaces)


# #Lab46 0426
# acount = input("계좌번호를 입력하시오: ")
# acount_result = ""

# for i in acount:
#     if i == "-":
#         pass
#     else:
#         acount_result += i

# print(acount_result)


# #예제40 0426
# for y in range(6):
#     for x in range(12):
#         print("*", end="")
#     print("")


# #실습예제1 0426
# level = int(input("원하는 단은: ")) #구구단 값 입력

# for i in range(1, 10):
#     print("%d * %d = %d" % (level, i, level * i))


# #실습예제2 0502
# max_num = int(input("임의의 수를 입력하시오: ")) #임의의 수 입력

# print("1부터 " + str(max_num) + "까지의 숫자중 짝수는 다음과 같습니다")

# for i in range(1, max_num + 1): #i = 1 ~ 임의의 수 까지 반복
#     if (i % 2) == 0:  # 만약 2로 나누어서 나머지가 0이라면? = i는 2의 배수라면?
#         print(i)  #i를 출력


#실습예제 3~5 0502
# #3
# for i in range(1, 11):
#     print(i, end=" ")
# print("")

# for i in range(0, 9):
#     print(i * 4, end=" ")
# print("")

# for i in range(9, 0, -1):
#     print(i, end=" ")


#4
# import math

# score = [] #빈 리스트 생성
# for i in range(1, 6): #5번 반복
#     i = int(input("성적을 입력해주세요: ")) #성적 입력받기
#     score.append(i) #score리스트에 성적 추가
# print("") #줄바꿈

# print("입력한 성적들: " + str(score))
# print("최고 성적: " + str(max(score)))
# print("최저 성적: " + str(min(score)))
# print("평균: " + str(sum(score) / len(score))) #총합값 / 리스트 수


# #5
# def plusInt(n1, n2): #n1, n2를 매개변수로 받고 더힌깂을 반환하는 함수
#     return (n1 + n2)

# print(plusInt(int(input("n1 입력 : ")), int(input("n2 입력 : ")))) #매개변수에 input으로 값을 입력받음



# # 실습예제 0510
# board = [[" " for x in range(3)] for y in range(3)]

# while True:
#     for r in range(3):
#         print(" " + board[r][0] + "  | " + board[r][1] + "  | " + board[r][2])
#         if (r != 2):
#             print("----|----|----")

#     x = int(input("다음 수의 x좌표를 입력하시오: ")) - 1
#     y = int(input("다음 수의 y좌표를 입력하시오: ")) - 1

#     if board[x][y] != ' ':
#         print("잘못된 위치입니다.")
#         continue
#     else:
#         board[x][y] = 'X'
#     done = False
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == ' ' and not done:
#                 board[i][j] = "O"
#                 done = True
#                 break
#         if done:
#             break
#     else:
#         for r in range(3):
#             print(" " + board[r][0] + "  | " + board[r][1] + "  | " + board[r][2])
#             if (r != 2):
#                 print("----|----|----")
#         print("둘곳이 없습니다.")
#         break


# #실습과제1 0511
# met = [] #빈 리스트 생성

# while True: #무한루프
#     met_input = input("재료를 입력하세요(종료시에는 앤터키) :") #재료 입력받아 변수에 저장
#     if met_input == "": #만약 입력받은값이 "" 라면?
#         break #루프 탈출
#     met.append(met_input) #met 리스트에 입력받은 값 추가하기

# print("필요한 재료 : ")
# print(met)


# # 실습과제2 0511
# import random

# pre_result = [] # 빈 리스트 생성
# pre_times = int(input("몇 번 연습할까요? :")) # 연습 횟수 입력
# pre_total = pre_times # 계산에 사용하기 위해 다른 변수에 저장

# while pre_times > 0: #연습 횟수가 0일때까지 반복
#     pre_hit = int(input("자~ 칩니다!!(1 ~ 9) :")) # 예측위치 입력
#     hit = random.randint(1, 9) #투구 위치
    
#     if pre_hit == (hit + 1) or pre_hit == (hit - 1) or pre_hit == hit: #만약 예측 위치와 투구 위치의 편차가 1일때,
#         pre_result.append('O') # O를 리스트에 추가
#         print("투구위치 : " + str(hit) + ", 예측위치 : " + str(pre_hit) + " => 쳤습니다!!")
#     else: # 빗나감
#         pre_result.append('X') # X를 리스트에 추가
#         print("투구위치 : " + str(hit) + ", 예측위치 : " + str(pre_hit) + " => 헛스윙...")
#     pre_times -= 1 #연습 횟수 소모

# print("연습결과:", pre_result) #리스트 출력
# print("타율은", pre_result.count('O') / pre_total, "입니다") #타율 계산및 출력


# # 실습과제3 0512
# stu_grades = [] #학생 성적 리스트
# upper_80 = [] #80점 이상 리스트
# students = 8

# def append_grade(): #학생성적 리스트, 80점 이상 리스트에 추가하는 함수
#     i = True 
#     global students
#     while i:
#         grade_input = int(input("성적 " + str(9 - students) + " 입력: ")) #점수를 입력받음
#         if 0 <= grade_input <= 100: #0~100인 유효숫자인가?
#             stu_grades.append(grade_input) #학생 성적 리스트에 추가
#             if 80 <= grade_input <= 100: #80~100 이라면?
#                 upper_80.append(grade_input) #80점 이상 리스트에 추가
#             i = False #반복 종료
#             continue 

#         print("성적 입력 오류!! 다시 입력하세요") #continue 가 발동하지 않았을때 출력

# while students > 0: #남은 학생수가 0명 일 때까지
#     append_grade()
#     students -= 1 #한명 감소

# print("성적 평균은 " + str(sum(stu_grades) / len(stu_grades)) + "입니다.") #평균 출력
# print("80점 이상 성적을 받은 학생은 " + str(len(upper_80)) + " 명 입니다.") #80 명 이상 출력


# #실습과제 1 0519
# grades = [] # 빈 리스트 생성

# for i in range(1,11): #1 ~ 10 반복
#     grades.append(int(input(str(i) + "번 학생의 점수를 입력해 주세요"))) #i 번의 학생을 입력받음

# grades.sort()#파이썬 내장함수 이용한 정렬
# grades.reverse()#순서를 뒤집어서 큰값부터 나열
# print(grades)



# #실습과제 2 0519
# import random

# target = random.randint(1,99) #정답값

# li = [] #빈 리스트 생성
# for i in range(1,100): #0~99의 수를 리스트에 추가
#     li.append(i)
# li.reverse() #리스트를 반전시킴

# def find_num(): #2진탐색
#     start = 0
#     end = len(li) - 1
#     count = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if li[mid] < target:
#             count += 1
#             break
#         elif li[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#         count += 1
#     return target, count

# print("""이진탐색 결과:
# 검색값: {0}
# {1}번 만에 찾았습니다""".format(find_num()[0], find_num()[1]))


# #실습과제3 0521
# import random

# target = random.randint(1,99)
# Try = 0
# li = []

# for i in range(1, 100): #1~99의 리스트 생성
#     li.append(i)

# #숫자 찾기 메인 함수
# def find_num():
#     start = 0 
#     end = len(li) - 1
#     count = 0 #컴퓨터 횟수
#     j = False #컴퓨터의 게임이 끝났는가?

#     while True:
#         i = list(try_find()) #i에 함수값을 저장
#         if i[0] == True: #만약 User가 값을 맞추었다면?
#             return i[1], count #User 시도 횟수, Computer 시도 횟수 반환
#         mid = (start + end) // 2
#         if j == False: #컴퓨터의 게임이 끝나지 않았다면
#             if li[mid] == target: 
#                 j = True
#             elif li[mid] < target:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#             count += 1

# def try_find():
#     global Try #전역변수 호출
#     Try += 1 #시도 횟수 증가
#     input_num = int(input("숫자를 입력해주세요(0~99): "))
#     if input_num == target: #정답일때
#         print("축하합니다! 정답입니다!")
#         return True, Try #정답을 맟췄음을 의미하는 True, 시도횟수 반환
#     elif input_num > target:
#         print("정답보다 큽니다")
#     else:
#         print("장딥보디 작습니다")
#     return False, Try   #정답을 맞추지 못함을 의미하는 False, 시도횟수 반환

# i = list(find_num())
# print("Computer", i[1], "번, User", i[0], "번" )



# #실습과제_1 0522
# tuple_A = (4,2,1,5,6,7,9) #튜플 선언
# print(tuple_A)

# tuple_A = list(tuple_A) #튜플을 리스트로 변환
# print(tuple_A)

# tuple_A.append(3) #리스트에 3 을 추가
# print(tuple_A)

# tuple_A.append(8) #리스트에 8 을 추가
# print(tuple_A)

# tuple_A.sort()   #리스트를 작은수 순서로 정렬
# tuple_A.reverse()#리스트를 역수로 정렬
# print(tuple_A)

# tuple_A = tuple(tuple_A) #리스트를 튜플로 변환
# print(tuple_A)



# #실습과제2_0522
# def p_num_input():
#     p_num = input("전화번호를 입력하시오(- 포함): ") #전화번호를 입력받아 변수에 선언
#     return p_num.replace("-", ", ") #replace를 이용해서 하이픈(-)을 쉼표와 띄어쓰기로 변환

# print(p_num_input())



# #실습과제3_0522
# def sep_email_form():
#     email_ad = input("이메일 주소를 입력해주세요 :") #이메일 주소를 입력받은 후, email_ad 변수에 선언
#     email_ad = email_ad.replace("@", ", ")  # replace를 사용해서 @값을 , 값으로 치환 
#     email_ad = email_ad.replace(".", ", ")  # replace를 사용해서 .값을 , 값으로 치환
#     return email_ad 

# print(sep_email_form())



# #실습과제4_0522

# #학생들의 점수가 쓰인 사전
# grades = {1 : [80, 90, 86], 2 : [78, 88, 85],
#           3 : [85, 85, 92], 4 : [70, 69, 65],
#           5 : [90, 95, 100]}

# for i in grades: 
#     average = grades[i] #key값이 i인 value리스트를 변수에 선언
#     print(i, "번 :", (sum(average) / len(average))) #평균값을 구하는 계산식



# #lab09 0524
# import math

# r =float(input("원의 반지름을 입력하시오: "))
# print("원의 넓이는", (r ** 2) * math.pi, "이고 원의 둘레는",
#       r * 2 * math.pi, "이다.")


# #lab19 0524
# partyA = set(["Park", "Kim", "Lee"])
# partyB = set(["Park", "Choi"])

# print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
# print(partyA.intersection(partyB))


# #lab30 0524
# eng_dict = {"one" : "하나", "two" : "둘", "three" : "셋"}

# print(eng_dict.get(input("단어를 입력하시오: "), "없음"))


# #lab32 0524
# table = {
#     "B4" : "Before",
#     "TX" : "Thanks",
#     "BBL": "Be Back Later",
#     "BCNU": "Be Seeing You",
#     "HAND": "Have A Nice Day"
# }

# message = input("번역할 문장을 입력하시오: ")
# words = message.split()
# result = ""
# for word in words:
#     if word in table:
#         result += table[word] + " "
#     else:
#         result += word

# print(result)


# #Lab 46 0524
# def check_pal(s):
#     low = 0
#     high = len(s) - 1
#     while True:
#         if low > high:
#             return True;
#         a = s[low]
#         b = s[high]
#         if a != b:
#             return False
#         low += 1
#         high -= 1

# s = input("문자열을 입력하시오: ")
# s = s.replace(" ", "") 
# if check_pal(s)==True:
#     print("회문입니다.")
# else:
#     print("회문이 아닙니다.")


# #lab48 0524
# phrase = input("문자열을 입력하세요 : ")

# acronym = ""
# for word in phrase.upper().split():
#     acronym += word[0]
# print( acronym )


# #lab50 0524
# sentence = input("문자열을 입력하시오: ")
# table = { "alphas": 0, "digits":0, "spaces": 0 }
# for c in sentence: # c : char in sentence
#     if c.isalpha():
#         table["alphas"] += 1
#     if c.isdigit():
#         table["digits"] += 1
#     if c.isspace():
#         table["spaces"] += 1
# print(table)



# #Lab 20
# import math
# class Circle:
#     def __init__(self, radius=1.0):
#         self.__radius = radius
#     def setRadius(self, r):
#         self.__radius = r
#     def getRadius(self): 
#         return self.__radius
#     def calcArea(self):
#         area = math.pi*self.__radius*self.__radius
#         return area
#     def calcCircum(self):
#         circumference = 2.0*math.pi*self.__radius
#         return circumference

# c1 = Circle(30)
# print("원의 반지름=", c1.getRadius())
# print("원의 넓이=", c1.calcArea())
# print("원의 둘레=", c1.calcCircum())


# #Lab22 0531
# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
#     def withdraw(self, amount):
#         self.__balance -= amount
#         print("통장에서 ", amount, "가 출금되었음")
#         return self.__balance
#     def deposit(self, amount):
#         self.__balance += amount
#         print("통장에 ", amount, "가 입금되었음")
#         return self.__balance
    
# a = BankAccount()
# a.deposit(100)
# a.withdraw(10)



# #Lab24 0531
# class Cat:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def setName(self, name):
#         self.__name = name
#     def getName(self):
#         return self.__name
#     def setAge(self, age):
#         self.__age = age
#     def getAge(self):
#         return self.__age

# missy = Cat('Missy', 6)
# lucky = Cat('Lucky', 11)
# print (missy.getName(), missy.getAge())
# print (lucky.getName(), lucky.getAge())



# #Lab26 0531
# class Box:
#     def __init__(self, width=0, length=0, height=0):
#         self.__width = width
#         self.__length = length
#         self.__height = height
#     def setWidth(self, width):
#         self.__width = width
#     def setLength(self, length):
#         self.__length = length
#     def setHeight(self, height):
#         self.__height = height
#     def getVolume(self):
#         return self.__width*self.__length*self.__height
#     def __str__(self):
#         return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)
    
# box = Box(12, 34, 56)
# print(box)
# print('상자의 부피는 ', box.getVolume())



#Lab28 0531
# class Car:
#     def __init__(self, speed=0, gear=1, color="white"):
#         self.__speed = speed
#         self.__gear = gear
#         self.__color = color
#     def setSpeed(self, speed):
#         self.__speed = speed
#     def setGear(self, gear):
#         self.__gear = gear
#     def setColor(self, color):
#         self.__color = color
#     def __str__(self):
#         return '(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)

# myCar = Car()
# myCar.setGear(3)
# myCar.setSpeed(100)
# print(myCar)




# #실습과제1 0531
# class Square:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def get_width(self): #접근자(getter)
#         return self.width
    
#     def set_width(self, width): #설정자(setter)
#         self.width = width
    
#     def get_height(self): #접근자(getter)
#         return self.height
    
#     def set_height(self, height): #설정자(setter)
#         self.height = height
    
#     def calculate_area(self): #넓이 계산
#         return self.width * self.height
    
#     def calculate_perimeter(self): #둘레 길이 계산
#         return 2 * (self.width + self.height)
    
# sq1 = Square(20, 30)
# print("가로 :", sq1.get_width(), ", 세로 :", sq1.get_height())
# print("넓이 :", sq1.calculate_area())
# print("둘레 :", sq1.calculate_perimeter())
# sq1.set_width(40) 
# print("가로 :", sq1.get_width(), ", 세로 :", sq1.get_height())
# print("넓이 :",sq1.calculate_area())
# print("둘레 :",sq1.calculate_perimeter())



# #실습과제2 0531
# import math

# class position:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def set_x(self, x): #설정자(setter)
#         self.x = x

#     def get_x(self): #접근자(getter)
#         return self.x
    
#     def set_y(self, y): #설정자(setter)
#         self.y = y

#     def get_y(self): #접근자(getter)
#         return self.y
    
#     def calculate_distance(self): #거리 계산
#         return math.sqrt((self.x ** 2) + (self.y ** 2))

#     def __str__(self):
#         return "<{},{}>".format(self.x, self.y)

# my_position = position(20, 30)
# print(my_position)
# print(my_position.calculate_distance())



# # 실습예제3 0602
# from fractions import Fraction #분수 라이브러리 import

# class FractionConversion: 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.f = Fraction(x, y)

#     def set_xyf(self, x, y): # 설정자(setter)
#         self.x = x
#         self.y = y
#         self.f = Fraction(x, y)

#     def get_f(self): # 접근자(getter)
#         return self.f
    
#     def add(self, other): # 덧셈
#         return (Fraction(self.f) + Fraction(other))

#     def subtract(self, other): # 뺄셈
#         return (Fraction(self.f) - Fraction(other))
    
#     def multiply(self, other): # 곱셈
#         return (Fraction(self.f) * Fraction(other))
    
#     def divide(self, other): #나눗셈
#         return (Fraction(self.f) / Fraction(other))
    
#     def floater(self): # float자료형 변경
#         return float(self.f)
    
#     def reciprocal(self): # 역수
#         return Fraction(self.y, self.x)
    
#     def __str__(self):
#         return "{}/{}".format(self.x, self.y)
    

# f1 = FractionConversion(1, 2)
# f2 = FractionConversion(2, 3)

# print("덧셈 결과 :", f1.add(f2.get_f()))
# print("뺄셈 결과 :", f1.subtract(f2.get_f()))
# print("곱셈 결과 :", f1.multiply(f2.get_f()))
# print("나눗셈 결과 :", f1.divide(f2.get_f()))
# print("점 표기법 결과 :", f1.floater())
# print("역수 결과 :", f1.reciprocal())
