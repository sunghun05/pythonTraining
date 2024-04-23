def test1(n):
    score = []
    for i in range(n):
        score.append(int(input("{}번째 학생의 점수는?: ".format(i+1))))
    av = sum(score)/len(score)
    print(av)
    a = 100
    x = []
    for i in range(n):
        if abs(score[i] - av) <= a:
            a = abs(score[i] - av)
            if abs(score[i] - av) == a:
                x.append(i + 1)
            else:
                x[0] = i+1
    return x
print(test1(int(input("n ? : "))))