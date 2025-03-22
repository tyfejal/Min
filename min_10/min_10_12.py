def input_data():
    n = int(input())
    return n

def CountDown(index):
    num = index
    for i in range(index):
        index = num
        index-=i
        print(index,end=' ')

def main():
    index=input_data()
    CountDown(index)

main()