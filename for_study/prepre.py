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





# t_size = int(input()) #입력
# cells_count = 0
# cells_time = [] #n분 성장한 t세포들을 추가할 예정인 리스트


# # 입력한 크기에 크기n 을 나누어서 몫이 1이 나올때까지 n을 2배로 곱함 (입력한 크기보다 작은 가장 큰 2의 배수를 구하기 위해)
# # 이후 몫이 1이 나오면 (입력한 값 - n) 값과 경과한 시간을 반환함
# def cell_cul(size):
#     time = 0
#     n = 1
#     while True:
#         if (size // n) == 1:
#             size -= n
#             return size, time
#         else:
#             n *= 2
#             time += 1


# # 사이즈가 0이 될때까지 반복
# while t_size > 0:
#     cells_time.append(cell_cul(t_size)[1]) #cell_cul 함수의 time 값을 cell_time 리스트에 추가함 (굳이 리스트에 추가하는 이유는 역순으로 만들기 위해)
#     t_size = cell_cul(t_size)[0] #cell_cul 함수에서 (입력한 크기 - n) 했던 값으로 다시 선언
#     cells_count += 1 #세포의 갯수 계산

# print(cells_count) #세포 갯수 출력

# for i in range(len(cells_time) - 1, -1, -1): #리스트에 있는값을 역순으로 출력하는 for문
#     print(cells_time[i], end=" ")

# #위에 for 문 말고도 .reserve() 를 이용해 리스트를 역순으로 만들어 출력하는 방법
# # cells_time.reverse()
# # for i in range(0, len(cells_time)):
# #     print(cells_time[i], end=" ")

#https://developer.mozilla.org/ko/docs/Web/HTTP/Status