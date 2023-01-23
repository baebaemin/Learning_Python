'''정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 
all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.'''

def all_list_sum(num):
    total = 0
    for i in num:
        for j in range(len(i)):
            total += i[j]
    return total

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11]]) # => 55