arr=['']*8
arr_char = list(input().split())
for i in range(8):
    arr[i] = arr_char[i]

big=['']*8
small=['']*8

for i in range(8):
    if arr[i].isupper():
        big[i] = arr[i]
    elif arr[i].islower():
        small[i] = arr[i]

print('big=',end='')
print(''.join(big))
print('small=',end='')
print(''.join(small))