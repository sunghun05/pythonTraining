file = open("sample1.txt","r")
word = []
for line in file:
    word.append(line.split())
print(word)