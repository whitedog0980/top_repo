# primes = []
# primes_mult = 1


# def is_prime(n):
#     for i in range(2, n): #1은 제외
#         if n%i == 0: #자기 자신을 제외한 수로 나눌때 나머지가 없는지? 
#             return False #만약 있다면
#     return True #만약 없다면(소수)

# def all_primes():
#     for n in range(2, 20):
#         if is_prime(n) == True:
#             primes.append(n)
#     return(primes)

# print(all_primes())

# for i in all_primes():
#     primes_mult *= i


# print(primes_mult)

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



# h = int(input("Layers :"))
# n = []
# t = []

# for i in range (h):
#     n.append(1)
#     t.append(1)
#     print("  " * (h - i), end="")
#     if i < 2:
#         pass
#     else:
#         for j in range(1, len(n) - 1):
#             t[j] = n[j - 1] + n[j]

#     for j in range(len(n)):
#         n[j] = t[j]
#         if len(str(n[j])) == 3:
#             print(" " + str(n[j]), end="")
#         if len(str(n[j])) == 2:
#             print("  " + str(n[j]), end="")
#         if len(str(n[j])) == 1:
#             print("   " + str(n[j]), end="")

#     print("")