N = int(input())
lst = []

for i in (range(1, N // 2 + 1)):
    if N % i == 0:
        lst.append(i)

print(*lst, N)


# ---

# N = int(input())
# numbers = range(1, N // 2 + 1)

# def div_list(i):
#     if N % i == 0:
#         return i

# result = filter(div_list, numbers)
# print(sorted(result.append(N)))

