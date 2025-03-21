arr = [['a','b','a','c','z'],
       ['c','t','a','c','d'],
       ['c','c','c','c','a']]

char = input()

cnt=0
for i in range(3):
    for j in range(5):
        if arr[i][j]==char:
            cnt+=1

if 3<=cnt<5:
    print("이야")
elif 5<=cnt<7:
    print("와우")
elif 7<=cnt:
    print("세상에")
else:
    print("이런")
