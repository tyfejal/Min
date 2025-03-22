arr = ['A','F','G','A','B','C']

char1, char2 = input().split()
cnt1 =0
cnt2 =0
for i in arr:
    if i == char1:
        cnt1 += 1
    elif i == char2:
        cnt2 += 1

if cnt1 >= 1 and cnt2 >= 1:
    print("와2개")
elif cnt1 >= 1 and cnt2 == 0:
    print("오1개")
elif  cnt1 == 0 and cnt2 >= 1:
    print("오1개")
elif cnt1 ==0 and cnt2==0:
    print("우0개")