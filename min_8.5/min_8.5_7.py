arr = [[0]*3 for _ in range(3)]

a,b,c = map(int, input().split())

arr[a][b] = c
for i in range(3):
    for j in range(3):
        row = arr[i][j]
        print(row, end=' ')
    print()