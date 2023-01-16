#행 길이 할당
colwidth = 61
# 규칙 딕셔너리 생성 
rule90 = {'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'}

# 가운데에 1을 넣기 위해 '30'이라는 값을 half에 할당, 라인 생성
half = colwidth // 2
line = '0' * half + '1' + '0' * half
print(line)

# 라인의 두 번째 원소가 '0'일때 (예제의 마지막 라인까지 같게 하려고)
while line[1] == '0':
    #line을 prev에 할당
    prev = line
    #line 리셋
    line = '0' * colwidth
    #1부터 59번까지의 i(0, 60, 61 제외)까지 반복
    for i in range(1, colwidth - 1):
        #리셋된 line에 '0' + prev[0:3]부터 1:4... 2:5... 반복 마지막엔 [60:]
         line = line[:i] + rule90[prev[i-1:i+2]] + line[i+1:]
    print(line)