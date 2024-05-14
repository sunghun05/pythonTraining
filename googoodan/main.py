#구구단 구현 for문, 2차원 배열, class
import forMul
def menu() :
    while True:
        print("{:=^100}".format("multiplication table mode"))
        print("by for syntax ----> 0", end="\n")

        try:
            m = int(input("select menu number : "))
        except ValueError:
            print("invalid menu. Try again.")
            continue

        try:
            if m == 0:
                data = forMul.enter()
                forMul.mul(data[0], data[1])
                break
            else:
                print("enter the valid menu number")
                continue
        except ValueError:
            print("invalid menu. Try again.")
            continue

if __name__ == "__main__":
    menu()