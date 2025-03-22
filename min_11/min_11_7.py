# arr = list(map(int, input().split()))

# Maxv = -21e8
# Minv = 21e8
# for i in range(7):
#     if i+1==len(arr):break
#     Max = max(arr[i],arr[i+1])
#     Min = min(arr[i],arr[i+1])

#     if Maxv<Max:
#         Maxv=Max
#     if Minv>Min:
#         Minv=Min
# print(f'MAX={Maxv}\nMIN={Minv}')



# ========================================================================================

arr = list(map(int, input().split()))

Maxv = max(arr)
Minv = min(arr)

print(f'MAX={Maxv}\nMIN={Minv}')