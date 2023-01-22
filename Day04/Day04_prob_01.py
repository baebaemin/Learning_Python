N = int(input())
lst = []

for i in (range(1, N // 2 + 1)):
    if N % i == 0:
        lst.append(i)

print(*lst, N) # 애스터리크를 써서 리스트를 프린트하면 띄어쓰기 적용 

# # 함수랑 filter()를 활용하는 방법

# N = 10
# n = range(1, N // 2 + 1)

# def div_list(i):
#     if N % i == 0:
#         return i

# rlt = filter(div_list, n)
# print(*rlt, N)

