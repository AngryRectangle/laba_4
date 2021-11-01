def radix_sort(a, result, power, l, r):
    if power == -1:
        return

    c = [0] * (ord('z') + 1)
    for i in range(l, r):
        c[ord(a[i][power])] += 1

    count = 0
    for j in range(0, len(c)):
        tmp = c[j]
        c[j] = count
        count += tmp

    for j in range(l, r):
        d = ord(a[j][power])
        result[c[d] + l] = j
        c[d] += 1


file = open("input.txt", "r")
data = file.readline().split()
phases = int(data[2])
word_c = int(data[1])
word_l = int(data[0])
lines = list(map(lambda line: list(line), file.read().split('\n')))
file.close()

words = list()
for i in range(0, word_c):
    word = ''
    for j in range(0, word_l):
        word += lines[j][i]
    words.append(word)

positions = [0] * word_c
for i in range(0, word_c):
    positions[i] = i

res = [0] * word_c
temp = list(res)

for i in range(word_l - 1, word_l - phases - 1, -1):
    radix_sort(words, res, i, 0, word_c)
    for j in range(0, word_c):
        temp[j] = words[res[j]]
    for j in range(0, word_c):
        words[j] = temp[j]
    for j in range(0, word_c):
        temp[j] = positions[res[j]]
    for j in range(0, word_c):
        positions[j] = temp[j]

res = list(map(lambda x: x + 1, positions))
print(words)
print(positions)
file = open("output.txt", "w")
file.write(" ".join(map(lambda x: str(x), res)))
file.close()