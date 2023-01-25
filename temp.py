N = 10
n = range(1, N // 2 + 1)

def div_list(i):
    if N % i == 0:
        return i

rlt = filter(div_list, n)
print(*rlt, N)