def list_sum(n_list):
    total = 0
    total = (total + i for i in n_list)
    return total

print(list_sum([1, 2, 3, 4, 5]))