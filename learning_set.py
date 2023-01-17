total = int(input('게시글의 총 갯수를 입력하세요 : '))
count = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))
if total % count == 0:
    print(total // count)
else:
    print(total // count + 1)