arr = [[chr(65+j+i*3) for j in range(3)] for i in range(3)]

y1,x1 = map(int, input().split())
y2,x2 = map(int, input().split())

arr[y1][x1],arr[y2][x2] = arr[y2][x2], arr[y1][x1]

for row in arr:
    print(' '.join(row))