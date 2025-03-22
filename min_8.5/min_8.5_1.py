arr = [0]*6
inarr = list(map(int, input().split()))

for i in range(6):
    arr[i] = inarr[i]
    if arr[i] < 5:
        a = "불합격"
    elif arr[i] >= 5:
        a = "합격"

    print(f'{i}번은 {arr[i]}점 {a}')
