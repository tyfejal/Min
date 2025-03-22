arr = [3,4,1,3,2,7,3]

num = int(input())
flag = False
for i in range(7):
    if num == arr[i]:
        flag = True
if flag:
    print("발견")
else:
    print("미발견")