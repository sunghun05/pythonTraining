#구구단 구현 for문, 2차원 배열, class
#print("{} X {} = {}".format(k + 1, j + 1, (k + 1) * (j + 1)), end='     ')
import forMul
def menu() :
    print("{:=^100}".format("multiplication table mode"))
    print("by for syntax ----> 0", end="\n")
    m = int(input("select menu number : "))
    if m == 0:
        data = forMul.enter()
        forMul.mul(data[0], data[1])
    else:
        print("enter the valid menu number")
        menu()
if __name__ == "__main__":
    menu()