a,b = input().split()
arr = [[None]*6 for _ in range(3)]

for i in range(3):
    for j in range(4):
        arr[i][j] = a
        row = arr[i][j]
        print(row, end='')
    for j in range(4,6):
        arr[i][j] = b
        row = arr[i][j]
        print(row, end='')
    print()




