def input_data():
    arr=[['']*3 for _ in range(2)]
    arr_char = list(input().split())
    index = 0
    for i in range(2):
        for j in range(3):
            arr[i][j] = arr_char[index]
            index+=1
    return arr
        

def findUpper(arr):
    cnt1 = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j].isupper():
                cnt1+=1
    print(f'대문자{cnt1}개')

def findLower(arr):
    cnt2 = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j].islower():
                cnt2+=1
    print(f'소문자{cnt2}개')

def main():
    arr = input_data()
    findUpper(arr)
    findLower(arr)

main()



# #input함수에 배열 입력받는 법
# def input_data():
#     arr=[['']*3 for _ in range(2)]
#     arr_char = list(input().split())
#     index = 0
#     for i in range(2):
#         for j in range(3):
#             arr[i][j] = arr_char[index]
#             index+=1
#     return arr


# def input_data():
#     arr=[['']*3 for _ in range(2)]
#     arr_char = list(input().split())
#     for i in range(2):
#         for j in range(3):
#             arr[i][j] = arr_char.pop(0)
#     return arr

