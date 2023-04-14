
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


