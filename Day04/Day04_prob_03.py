'''Dictionary로 이루어진 list를 전달 받아 
모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 
dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오. '''

def dic_list_sum(data):
    total = 0
    for i in data:
        total += i['age']
    return total

print(dic_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))