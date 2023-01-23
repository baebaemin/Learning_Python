number = 10

for i in range(1, number + 1):  # 1 ~ 입력값 동안
        if number % i == 0:    # 만약 입력값을 i로 나눴을 때, 나누어 떨어진다면
            print(i, end=' ')