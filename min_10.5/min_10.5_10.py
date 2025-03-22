arr = [[1,0,0,0,0],
       [1,0,1,0,0],
       [1,1,0,1,0],
       [1,0,1,0,0],
       [0,1,0,0,1],
       [0,0,0,1,0],
       [1,1,0,0,0]]

def output(num):
    print(num)

def process(num):
    cnt=0
    for i in range(7):
        if arr[i][num] == 1:
            cnt+=1
    return cnt

def input1():
    n = int(input())
    return n

def main():
    ret = input1()
    cntt=process(ret)
    output(cntt)

main()
