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



# w_res = input().split() #첫번째 입력 (리스트)
# rest_time = int(w_res[1]) #남은 시간
# all_work = int(w_res[0]) #모든 일 갯수
# works_time = input().split() #일들의 시간들 입력(리스트)
# work_done = 0 #해결한 일

# # works_time 리스트 내용을 전부 int자료형으로 변경
# int_works_time = []
# for i in range(len(works_time)):
#     int_works_time.append(int(works_time[i]))

# # 계산 반복식
# for i in range(all_work):
#     if rest_time > int_works_time[i]: #만약 남은시간이 i번쨰 일보다 많으면
#         rest_time -= int_works_time[i] #남은시간 뺌 (일 수행)
#         work_done += 1 #해결한 일 추가
#     else:
#         break 

# print(work_done)


# import turtle

# star_size = 20  # 별 크기
# num_rows = 7   # 층 수

# # 터틀 초기화
# t = turtle.Turtle()
# t.speed(0)  # 최대 속도로 설정

# # 층 수 만큼 반복
# for row in range(num_rows):
#     # 현재 층에 필요한 변수 계산
#     num_stars = row + 1
#     row_width = num_stars * star_size
#     row_start = -row_width / 2

#     # 현재 층의 별 출력
#     for star in range(num_stars):
#         t.penup()
#         t.goto(row_start + star * star_size, -row * star_size)
#         t.pendown()
#         t.begin_fill()
#         for i in range(5):
#             t.forward(star_size)
#             t.right(144)
#         t.end_fill()

# # 화면 유지
# turtle.done()


#참여자수 = N, 문제 수 = M, 채점기 기록 수 = Q
nmq = input().split()
results = [] #채점기 기록 추가할 리스트 선언
w = 0 #문제를 틀린 갯수
a = 0 #문제를 맞춘 갯수
g = 0 #패널티의 합

def reset_score():
    global a, w, g
    a = 0
    w = 0
    g = 0


#채점기 기록 입력받기
for i in range(int(nmq[2])): #채점기 기록 수 만큼 반복
    results.append(input().split())


#계산
# i = 참가자 번호
for i in range(1, int(nmq[0]) + 1): 
    # j = 문제 번호
    for j in range(1, int(nmq[1]) + 1):
        # k = 입력받은 리스트 값
        for k in results:
            if (j == int(k[1])) and int(k[0]) == i: #리스트값과 현재 진행중인 i 값과 j가 일치 할때,
                if k[3] == "WA": #문제가 틀렸을 경우
                    w += 1
                else: #문제가 맞았을 경우
                    a += 1
                    g += int(k[2]) + (20 * w)
                    w = 0
                    break #해당 문제 계산 종료
            else:
                continue
    #최종 출력
    print(i, a, g)
    reset_score()



