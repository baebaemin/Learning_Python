number = [1, 2, 3]
# def odd(n):
#     return n % 2
# rlt = [n for n in filter(odd, number)]
# print(rlt)

lst = [a for a in filter(lambda n: n % 2, number)]
print(lst)