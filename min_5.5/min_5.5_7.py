data = [0]*4

num = int(input())

for i in range(4):
    data[i] = num-i

print(*data)