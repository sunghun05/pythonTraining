# a = int(input("Enter a number: "))
# for i in range(9):
#     print("{} x {} = {}".format(a, i+1, a * (i+1)))


for i in range(1,10):
    for j in range(1, 4):
        print("{} x {} = {}".format(j, i, j * i), end="   ")
    print("\n")


# if (j*i >= 10):
#     print("   ", end="")
# elif (j*i < 10): print("    ", end="")