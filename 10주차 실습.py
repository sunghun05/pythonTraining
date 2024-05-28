def solution0():
    f = open("data/data.txt")
    ele = f.readlines()
    odd = []
    even = []
    try:
        for i in range(len(ele)):
            if int(ele[i]) % 2 == 0:
                even.append(int(ele[i].rstrip()))
            else :
                odd.append(int(ele[i].rstrip()))
    except ValueError:
        print("Invalid Data.")
    for i in range(len(even)):
        print("Even Numbers: ",even[i])
    for i in range(len(odd)):
        print("Odd Numbers: ", odd[i])
    total = sum(even) + sum(odd)
    cnt = len(odd) + len(even)
    print("정수의 개수 : ", cnt)
    print("정수의 총 합 : ", total)
    print("정수의 평균 : {:.2f}".format(total / cnt))
# solution0()

def solution1():
    with open("data/text.txt", 'r') as file :
        sentences = file.readline()
    print(sentences)
    sentences_count = len(sentences)
    word_count = 0
    for sentence in sentences:
        print(sentence.strip())
        words = sentence.split()
        word_count += len(words)

    print("문장의 수 : ", sentences_count)
    print("단어의 수 : ", word_count)

# solution1()

def solution2():
    with open('data/smart_contact.txt', 'r', encoding='utf8') as file :
        text = file.read()
    text = text.lower()
    words = text.split()
    word_count = {}

    for word in words :
        if word in word_count : #딕셔너리에 이미 단어가 추가되어있는 경우
            word_count[word] += 1
        else :                  #딕셔너리에 처음 등록하는 단어인 경우
            word_count[word] = 1

    print(word_count)

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_word_count:
        print(count, ' : ', word)
# solution2()

def solution3():
    with open('data/students.txt', 'r', encoding='utf8') as file :
        lines = file.readlines()

    print(lines)

    student_scores = {}

    for line in lines :
        parts = line.strip().split()
        name = parts[0]
        score = int(parts[1])
        student_scores[name] = score

    print(student_scores)
    for name in sorted(student_scores):
        print("{} : {}".format(name, student_scores[name]))

# solution3()
def solution4():
    import csv

    dates = []
    rates = []
    changes = []

    with open('data/dollar.csv', 'r', encoding='utf8') as file :
        csv_reader = csv.reader(file)
        for index, row in enumerate(csv_reader) :
            if index == 0 :
                dates = row
            elif index == 1:
                rates = list(map(float, row))
            elif index == 2:
                changes = list(map(float, row))

    min_rates = min(rates)
    max_rates = max(rates)
    print("최저 환율 : {:.2f} 최고환율 : {:.2f}".format(min_rates, max_rates))
# solution4()

def solution5():
    while(True):
        try :
            num = int(input("숫자를 입력하시오 : "))
        except ValueError:
            print("정수가 아닙니다. 다시 입력하시오.")
            continue
        print("정수 입력이 성공하였습니다.")
        break
solution5()