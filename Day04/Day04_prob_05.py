''' 정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 
이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오.
단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.
'''

def get_secret_word(nums):
    word = ''
    for i in nums:
        word += chr(i)
    return word
        
get_secret_word([83, 115, 65, 102, 89])   # => ‘SsAfY’
