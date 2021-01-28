# #Problem 1
# def splitlist(listA, k):
#     listB = [x for x in listA if x < k]
#     listC = [x for x in listA if x >= k]
#     return listB, listC
#
# listA = [1,2,3,5,6,5,1,0,-10]
# list1, list2 = splitlist(listA, 4)
#
# print(list1)
# print(list2)
#
#Problem 2
a = ord('A') #converts char to ascii code
list3 = [chr(a+x) for x in range(26)] #chr converts ascii code to character
print(f"Problem 2: {list3}")
#
# #Problem 3
# list4 = [x for x in list3 if x not in ['A', 'E', 'I', 'O', 'U']]
# print(list4)

#Problem 4
keys = [1, 2, 2, 5, 1, 20, 5, 1, 0, -10]
values = ['A', 'B', 'C','D','E','F','G','H','I','J']

dictA = {}

for i in range(len(keys)):
    if keys[i] not in dictA.keys():
        dictA[keys[i]] = values[i]

print(dictA)

#Problem 5
def elements(listA):
    listB = [x for x in listA if x >= 0]
    listC = [x for x in listA if x < 0]
    listD = [x for x in listA if x % 2 != 0]
    listE = [x for x in listA if x % 2 == 0]
    return listB, listC, listD, listE

listA = [1,2,-3,5,6,-5,1,0,-10, -7, 4, 9]
list1, list2, list3, list4 = elements(listA)

print(list1)
print(list2)
print(list3)
print(list4)

