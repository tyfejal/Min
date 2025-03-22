arr = [[0]*3 for _ in range(6)]

a,b = map(int, input().split())

for i in range(3):
    for j in range(3):
        arr[i][j] = a
        row = arr[i][j]
        print(row, end='')
    print()
for i in range(3,6):
    for j in range(3):
        arr[i][j] = b
        row = arr[i][j]
        print(row, end='')
    print()