arr = [0]*5

num = int(input())

for i in range(5):
    arr[i] = num-i

def KFC():
    print(''.join(map(str,arr)))

KFC()