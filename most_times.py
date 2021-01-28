import sys

count = 0
num = 0
tmpCount = 0

for i in sys.argv:
    tmpCount = sys.argv.count(i)
    if tmpCount > count:
        count = tmpCount
        num = i
print("Most frequent number:", num)

