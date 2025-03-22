arr = ['S','t','r','u','c','t','P','o','i','n','t','e','r']

char = input()
cnt = 0
for value in arr:
    if char == value:
        cnt+=1
        break
if cnt > 0:
    print("발견")
else:
    print("미발견")