a,b,c = input().split()

c = int(c)
for j in range(c):
    for i in range(ord(a),ord(b)+1):
        print(chr(i),end='')
    print()
