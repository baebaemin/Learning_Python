'''문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 
더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.
단, 두 문자열의 아스키 숫자의 합이 같은 경우, 둘 다 반환하세요.
'''
def get_num(w):
    num = 0
    for i in w:
        num += ord(i)
    return num

def get_strong_word(w1, w2):
    n1 = get_num(w1)
    n2 = get_num(w2)

    if n1 == n2:
        return w1, w2
    return w1 if n1 > n2 else w2
        
print(get_strong_word('z', 'a')) # => 'z'
print(get_strong_word('delilah', 'dixon')) # => 'delilah'
print(get_strong_word('lilahde', 'delilah')) # => '('lilahde', 'delilah')'

# 괄호를 벗기려면 어떻게 해야할까?