s = "WelcomeToCryptography"
key = 5

#Problem 1
def caesarencryption (s, key):
    listA = []
    for a in range(len(s)):
        k = ord(s[a])%32-1
        listA.append(k)
    print(f"Step 1: {listA}")
    for b in range(len(listA)):
        if ((listA[b]+key) > 26 ):
            j = listA[b]-26 + key
        else:
            j = listA[b] + key
        listA[b] = j
    print(f"Step 2: {listA}")
    for c in range(len(listA)):
        listA[c] = chr(listA[c] + 65)
    # print(f"Step 3: {listA}")

    ciphertext = ""
    for d in listA:
        ciphertext += d
    print(f"Step 3: ciphertext= {ciphertext}")

caesarencryption(s,key)

cipher = "BJQHTRJYTHWDUYTLWFUMD"
key = 5

#Problem 2
def caesardecryption(cipher, key):
    listB = []
    for a in range(len(cipher)):
        k = ord(cipher[a]) - 65
        listB.append(k)
    print(f"Step 1: {listB}")
    for b in range(len(listB)):
        if ((listB[b] - key) < 0):
            j = listB[b] + 26 - key
        else:
            j = listB[b] - key
        listB[b] = j
    print(f"Step 2: {listB}")
    for c in range(len(listB)):
        listB[c] = chr(listB[c] + 65)
    # print(f"Step 3: {listB}")

    plaintext = ""
    for d in listB:
        plaintext += d
    print(f"Step 3: plaintext= {plaintext}")


caesardecryption(cipher, key)
