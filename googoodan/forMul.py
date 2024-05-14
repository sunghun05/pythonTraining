def mul(num, row):
    loop = 1
    for i in range(1, num+1):
        if (i % (row) == 0 or (i == num)):
            print('')
            for j in range(1, 10):
                for k in range(loop, i+1):
                    print("{: >3} X {: >3} = {: >3}".format(k, j, k*j), end='    ')
                print('')
            print('')
            loop += row
def enter():

    while True:

        n = (input("Enter a number : "))

        try:
            if int(n) <= 1 :
                print("2보다 큰 단수를 입력하세요.")
                continue
            elif int(n) >= 100 :
                print("100보다 작은 수를 입력하세요.")
                continue
        except ValueError:
            print("Invalid number, Try again.")
            continue

        r = (input("Enter a row : "))

        try:
            if int(r) < 1:
                print("행은 1보다 커야 합니다.")
            elif int(r) > int(n) :
                print("입력한 수보다 많은 행을 출력할 수 없습니다.")
            else:
                return int(n), int(r)
                break
        except ValueError:
            print("Invalid number, Try again.")
