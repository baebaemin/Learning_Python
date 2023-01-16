width = 61
half = width // 2
half_zero = 'o' * half
l = half_zero + '*' + half_zero

pattern = {'***':'o', '**o':'*', '*o*':'o', '*oo':'*', 'o**':'*', 'o*o':'o', 'oo*':'*', 'ooo':'o'}

for j in range(len(l)):
    next = ''
    for i in range(len(l)):
        three = l[i:i + 3]

        if len(three) == 2:
            next = next + pattern[three + l[0]]
        elif len(three) == 1:
            next = pattern[three + l[:2]] + next
        else:
            next = next + pattern[three]
        
    print(next)
    l = next