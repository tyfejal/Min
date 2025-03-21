arr = ['D','F','G','D','A','Q']

ch1, ch2 = input().split()

cnt = 0
for i in arr:
    if ord(ch1) <= ord(i) <= ord(ch2):
        cnt+=1

if cnt >= 1:
    print("발견!!!")

else:
    (print("미발견!!!"))
