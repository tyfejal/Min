arr = [['a','b','E'],
       ['E','2','W'],
       ['3','2','4']]

for i in range(3):
    for j in range(3):
        if arr[i][j].isupper():
            print(arr[i][j].lower(),end=' ')
        elif arr[i][j].islower():
            print(arr[i][j].upper(), end=' ')
        else: 
            print(int(arr[i][j])+5,end=' ')
    print()    
print(arr)