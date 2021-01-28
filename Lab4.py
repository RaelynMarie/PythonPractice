M=b'Hello Python'

h32=0

#each block is four bytes (32-bit blocks)
for i in range(1, len(M), 4):
    tmp = (M[i] << 16) + M[i-1]
    h32 ^= tmp
print(h32)

for k in range(1, len(M), 4):
    b = M[k] & 1
    x = (b << 7) + (M[k-1] >> k)
    h32 ^= x

print(h32)