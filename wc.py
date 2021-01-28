import sys
from collections import Counter

file = sys.argv[-1]


def file2list(a):
    f = open(a)
    f_str = f.read()
    f_str = f_str.replace(',', '')
    f_str = f_str.replace('.', '')
    f_str = f_str.replace(';', '')
    return f_str.split()


c = file2list(file)


def lines(a):
    f = open(a)
    f_str = f.read()
    count = f_str.count('\n')
    return count


b = lines(file)

print("Lines:", b)


def wordCount(listA):
    count = 0

    for w in listA:
        count += 1
    return count


z = wordCount(c)
print("Words:", z)


def mostfreq(l_words):
    dictA = {}
    for word in l_words:
        if word in dictA:
            dictA[word] += 1
        else:
            dictA[word] = 1
    m = max(dictA, key=dictA.get)
    for key, value in dictA.items():
        if m == key:
            return [key, value]

def leastfreq(l_words):
    dictA = {}
    for word in l_words:
        if word in dictA:
            dictA[word] += 1
        else:
            dictA[word] = 1
    m = min(dictA, key=dictA.get)
    for key, value in dictA.items():
        if m == key:
            return [key, value]

print("Most frequent word:", mostfreq(c))
print("Least Frequent word:", leastfreq(c))

def charCount(a):
    f = open(a)
    f_str = f.read()
    a_str = list(f_str)

    return len(a_str)

r = charCount(file)
print("chars:", r)

def unique(c):
    z = set()
    for word in c:
        z.add(word)
    return len(z)

print("Unique words:", unique(c))