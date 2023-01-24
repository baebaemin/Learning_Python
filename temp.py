def dic_list_sum(data):
    total = 0
    for i in data:
        total += i.get('age')
    return total

a = dic_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])
print(a)