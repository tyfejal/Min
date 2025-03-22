def pingpong(value):
    tong = value
    return tong+10

def main():
    stone = int(input())
    ret = pingpong(stone)
    print(ret)


main()