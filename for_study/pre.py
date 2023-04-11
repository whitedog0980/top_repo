
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


