def all_list_sum(args): #2차원 리스트 args를 받음
    arg_total = 0
    for arg in args: #2차원 리스트 args에서 1차원 리스트 arg를 받음
        for i in arg:
            arg_total += i
    return arg_total

print(all_list_sum([[1], [2,3], [4, 5, 6],  [7, 8, 9, 10]]))