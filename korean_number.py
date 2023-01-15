def korean_number(txt):
    kr_dic = {'1': '일', '2': '이', '3': '삼'}
    return kr_dic[txt]

a = korean_number(input())
print(a)
