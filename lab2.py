s = "hello HELLOTHERE 12340 2301234567"


def countLowerCase(s):
    count = 0
    for k in s:
        if ord('a') <= ord(k) <= ord('z'):
            count += 1
    return count
print(f"Problem 1: {countLowerCase(s)}")

def countUpperCase(s):
    count = 0
    for k in s:
        if ord('A') <= ord(k) <= ord('Z'):
            count += 1
    return count
print(f"Problem 2: {countUpperCase(s)}")

def countEvenDigits(s):
    count = 0
    for k in s:
        if k.isdigit():
            if k in ('2', '4', '6', '8', '0'):
                count += 1
    return count
print(f"Problem 3: {countEvenDigits(s)}")

def fncStrings(s):
    s0 =""
    for k in s:
        if k not in ['a', 'e', 'i', 'o', 'u']:
            s0 += k
    return s0

print(f"Problem 4: {fncStrings('illinois')}")


listV = [1, 2, 3, 3, 5]
def nonDecreasing(listV):
    result = True
    for i in range(1, len(listV)):
        if listV[i] <= listV[i-1]:
            result = False
            break
    return result

print(f"Problem 5: {nonDecreasing(listV)}")

listV = [5, 4, 3, 3, 1]
def nonIncreasing(listV):
    result = True
    for i in range(1, len(listV)):
        if listV[i] >= listV[i-1]:
            result = False
            break
    return result

print(f"Problem 6: {nonIncreasing(listV)}")

# def addSum(listA):
#     sum = 0
#     for i in range(len(listA)):
#         sum += listA[i]
#     return sum
#
# print(addSum(listA))
# print(addSum(listB))
listA = [1, 2, 6, 5]
listB = [2, 2, 2, 5]

def sumGreater(listA, listB):
    sum1 = 0
    sum2 = 0
    for i in range(len(listA)):
        sum1 += listA[i]
    for i in range(len(listB)):
        sum2 += listB[i]
    if sum1 > sum2:
        return True
    else:
        return False

print(f"Problem 7: {sumGreater(listA, listB)}")