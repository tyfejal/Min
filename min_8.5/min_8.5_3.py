char = [None]*5
n = int(input())
arr = input().split()

for i in range(n):
    char[i] = arr[i]
    print(char[i],end='')
