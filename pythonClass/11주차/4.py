import re
from collections import Counter

with open('sample1.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    # print(data)
    print("=====파일 내용 분석=====")

    sentences = re.split(r'[.!?]', data)

    # 빈 문자열을 제거합니다.
    sentences = [sentence for sentence in sentences if sentence.strip()]

    # 총 문장의 갯수를 출력합니다.
    total_sentences = len(sentences)

    # 단어를 공백을 기준으로 나누어 리스트로 만듭니다.
    words = re.findall(r'\b\w+\b', data)

    # 단어의 빈도를 계산합니다.
    word_counts = Counter(words)

    # 중복되는 단어의 수를 계산합니다.
    duplicate_words = sum(count > 1 for count in word_counts.values())

    # 전체 단어 수를 계산합니다.
    total_words = len(words)

    # 중복되는 단어의 비율을 계산합니다.
    duplicate_ratio = duplicate_words / total_words

    print("총 문장의 갯수:", total_sentences)
    print("총 단어의 갯수:", total_words)
    print("중복제거 단어의 수:", total_words - duplicate_words)
    print("중복되는 단어의 비율: %3d%%" %  (duplicate_ratio * 100))