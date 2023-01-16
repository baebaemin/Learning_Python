pattern = {'111':'0', '110':'1', '101':'0', '100':'1', '011':'1', '010':'0', '001':'1', '000':'0'}
l = input()

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