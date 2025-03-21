arr = [[3,1,6],
       [7,8,4],
       [9,2,3]]

Max_value = -21e8
Min_value = 21e8
a,b,c = map(int, input().split())
arr[a][b] = c
for i in range(3):
    for j in range(3):
        if j+1 ==3: break
        com = arr[i][j]
        pare = arr[i][j+1]
        Max = max(com,pare)
        Max_value = max(Max_value,Max)
        Min = min(com,pare)
        Min_value = min(Min,Min_value)
print(Min_value+Max_value)
