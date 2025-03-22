def BBQ(k):
    for i in range(1,k+1):
        print(i, end='')

def KFC(char):
    print(char*7)



n = int(input())
if n%2 != 0:
    k = int(input())
    BBQ(k)
else: 
    char = input()
    KFC(char)
    
