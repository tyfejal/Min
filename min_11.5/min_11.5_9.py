arr = list(map(int,input().split()))
array_2 = [[arr[5],arr[4],arr[3]],
           [arr[2],arr[1],arr[0]]]

array_1 = []
for row in array_2:
    array_1.extend(row)

array_1[0],array_1[5] = array_1[5],array_1[0]
print(*array_1)
