arr = list(map(int, input().split()))

for i in range(2):
    row = arr[i*3:(i+1)*3]

    print(''.join('#' if num==0 else str(num) for num in row))
