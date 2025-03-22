arr = [['A','B','C','D','E'],
       ['E','A','B','A','B'],
       ['A','C','D','E','R']]

char = input()
cnt = 0
for i in range(3):
    for j in range(5):
        if arr[i][j] == char:
            cnt+=1
if cnt >= 3:
    print("대발견")
elif 0<cnt<3:
    print("발견")
elif cnt ==0:
    print("미발견") 
