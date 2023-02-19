<<<<<<< HEAD
print('32')
=======
while 1:
    div_lst = []
    n = int(input())
    div_lst.append(n)
    i = n // 2
    
    while i > 1:
        if n % i == 0:  # i가 약수라면 !?
            div_lst.append(i)
            n = n // i
            i -= 1
    
    print(div_lst)
>>>>>>> bb60515b29eb8bd0618d187b540668b0358eecc1
