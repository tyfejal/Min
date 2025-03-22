arr = [[0]*4 for _ in range(3)]

n = int(input())

def process(n):
    global arr
    for i in range(3):
        for j in range(4):
            arr[i][j] = n
            n += 1

def output(n):
    global arr
    for i in range(3):
        for j in range(4):
            arr[i][j] = n+1
            n += 1
    for k in arr:
        print(' '.join(map(str,k)))

output(n)