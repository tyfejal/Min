# arr = input().split()

# cnt = 0
# for i in arr:
#     if i == "A":
#         cnt += 1
# print(f'문자A는 {cnt}개발견')

# for i in range(5):
#     if arr[i] == "A":
#         print(f'{i}번')

# ===============================================

arr = input().split()

count_arr = arr.count('A')
print(f'문자A는 {count_arr}개발견')

for index,char in enumerate(arr):
    if char == 'A':
        print(f'{index}번')

for i,j in enumerate(arr):
    print(j, end='')