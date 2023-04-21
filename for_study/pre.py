
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

