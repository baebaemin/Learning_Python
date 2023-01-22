'''문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 
get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.'''

def get_secret_number(word):
    num = 0
    for i in list(word):
        num += ord(i)
    return num
print(get_secret_number('happy')) # => 546
 