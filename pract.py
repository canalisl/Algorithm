a = 3
b = 4

cnt = 0
while True:
    cnt += 1
    if a == 3:
        print(f'cnt는 {cnt}고, a는 {a}다~')
        if b == 4:
            print('b는 5다~')
        else:
            break
    continue

print('반복문 끝')