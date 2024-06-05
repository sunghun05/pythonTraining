def solution2():
    with open('data1/Goldensaying.txt.txt', 'r') as f:
        lines = f.readlines()
        say1 = []
        say2 = []
        for i in range(len(lines)):
            #lines[i].split(' ')
            lines[i] = lines[i].rstrip('\n')
            lines[i] = lines[i].rstrip(',')
            lines[i] = lines[i].rstrip('.')
            lines[i] = lines[i].split(' ')

            if i == 0 :
                for j in range(len(lines[i])):
                    if lines[i][j] != '':           #단어가 빈칸이면 단어로 간주하지 않음
                        say1.append(lines[i][j])
            if i == 2 :
                for k in range(len(lines[i])):
                    if lines[i][k] != '':
                        say2.append(lines[i][k])
        say1 = set(say1)
        say2 = set(say2)

        print("첫번째 명언 집합 : ", say1)
        print("두번째 명언 집합 : ", say2)
        print("공통 단어 : ", say1.intersection(say2))
#solution2()

def solution3():
    file1 = open('data1/sample1.txt.txt')
    file2 = open('data1/sample2.txt.txt')

    sen1 = file1.readlines()
    sen2 = file2.readlines()

    word1 = []
    word2 = []

    for i in range(len(sen1)):

        sen1[i] = sen1[i].split(' ')
        for j in range(len(sen1[i])):
            sen1[i][j] = sen1[i][j].rstrip('\n')
            sen1[i][j] = sen1[i][j].rstrip('.')
            sen1[i][j] = sen1[i][j].rstrip(' ')
            sen1[i][j] = sen1[i][j].rstrip(',')
            if sen1[i][j] != '': word1.append(sen1[i][j])
    for i in range(len(sen2)):

        sen2[i] = sen2[i].split(' ')
        for j in range(len(sen2[i])):
            sen2[i][j] = sen2[i][j].rstrip('\n')
            sen2[i][j] = sen2[i][j].rstrip('.')
            sen2[i][j] = sen2[i][j].rstrip(' ')
            sen2[i][j] = sen2[i][j].rstrip(',')
            if sen2[i][j] != '': word2.append(sen2[i][j])
    word1 = set(word1)
    word2 = set(word2)

    print("{:=^18}"
          "\n"
          "총 문장의 수 : {}\n"
          "총 단어의 수 : {}\n".format("1번 파일", len(sen1), len(word1)))

    print("{:=^18}"
          "\n"
          "총 문장의 수 : {}\n"
          "총 단어의 수 : {}\n".format("2번 파일", len(sen2), len(word2)))

    print("{:=^18}\n"
          "같은 단어의 수 : {}\n"
          "같은 단어 : {}".format("파일 비교", len(word1.intersection(word2)), word1.intersection(word2)))

    file1.close()
    file2.close()
solution3()