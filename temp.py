word = 'SsaFyYabcdefgz'
new = ''

# 대문자를 소문자로 바꾸기
# for ch in word:
#     if 65 <= ord(ch) <= 90:
#         new += chr(ord(ch) + ord('a') - ord('A'))
#     else: new += ch
# print(new)

# 소문자를 대문자로 바꾸기

for ch in word:
    if 97 <= ord(ch) <= 122:
        new += chr(ord(ch) - 32)
    else: new += ch
print(new)