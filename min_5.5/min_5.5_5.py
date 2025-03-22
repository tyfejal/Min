arr = [4,1,2,3,5]


st = input()

if st == 'a' or st =='b' or st == 'c':
    print(*arr[3::-1])

else:
    print(*arr[4:0:-1])