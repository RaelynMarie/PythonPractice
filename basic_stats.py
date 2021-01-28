def avg(listA):
    sum = 0
    count = 0
    for k in listA:
        count += 1
        sum += k
    average = sum / count
    return average


def l_sqr(listA):
    listB = [x ** 2 for x in listA]
    return listB


def sum(listB):
    sum = 0
    for k in listB:
        sum += k
    return sum


def var(X):
    temp = 0
    listC = []
    for x in X:
        listC.append((x - avg(X)) ** 2)
    temp = sum(listC) / len(X)
    return temp


print(avg([23, 32, 43, 54]) == 38.0)
print(sum(l_sqr([23, 32, 43, 54])) == 6318)
print(var([23, 32, 43, 54]) == 135.5)
