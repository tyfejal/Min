arr = [None]*17

def input_data():
    global arr
    a,b,c = input().split()
    for i in range(17):
        if 0 <= i <7:
            arr[i] = a
        if 7<= i <13:
            arr[i] = b
        if 13 <=i <17:
            arr[i] = c
    for j in range(16,-1,-1):
        print(arr[j],end = '')

input_data()