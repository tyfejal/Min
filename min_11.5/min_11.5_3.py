arr = ['A','1','1','1','5','A','w','z']

char = input()

cnt=0
for i in arr:
    if i == char:
        cnt+=1

if 3<=cnt:
    print("THREE")
elif cnt==2:
    print("TWO")
elif cnt==1:
    print("ONE")
else:
    print("NOTHING")
