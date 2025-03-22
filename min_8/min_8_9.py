arr = [[0]*3 for _ in range(2)]

def input_data():
    global arr

    values = list(map(int, input().split()))

    for i in range(2):
        arr[i] = values[i*3:(i+1)*3]
    return arr
def process():
    arr = input_data()
    cnt = 0
    for i in range(2):
        for j in range(3):
            cnt += arr[i][j]
    print(cnt)

def output_data():
    process()

output_data()