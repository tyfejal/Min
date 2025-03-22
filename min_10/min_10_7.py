def GOP():
    num1,num2 = map(int, input().split())
    cross = num1*num2
    return cross

def SUM():
     a,b = map(int, input().split())
     plus = a+b
     return plus  

def main(cross, plus):
    if cross > plus:
        print("GOP>SUM")
    else: 
        print("GOP==SUM")


cross = GOP()
plus = SUM()
main(cross, plus)