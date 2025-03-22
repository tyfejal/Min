def starBox():
    for i in range(1,21):
        if i%2 !=0:
            print(i, end=' ')

def macDoll():
    arr = ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
    for i in arr:
        print(i, end=' ')

def copyBean():
    for i in range(-5,6):
        print(i, end=' ')


n = int(input())

if 3500<= n <= 5000:
    starBox()
elif 2500 <= n <3500:
    macDoll()
else:
    copyBean()

