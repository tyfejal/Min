arr1 = ['B', 'D', '5', 'Q', 'A']
arr2 = ['Q', 'E', 'R', 'E', 'F']

def input_data():
    char = input()
    return char

def output_data():
    char = input_data()
    global arr1
    global arr2

    if char.isupper():
        print(''.join(arr2))
    elif char.islower():
        print(''.join(arr1))
    else: print("HGFEDCBA")

output_data()
