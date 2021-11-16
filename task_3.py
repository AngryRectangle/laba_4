import TrueStack

tStack = TrueStack.TrueStack()
file = open("input.txt", "r")
result = []
count = int(file.readline())

def inversed(last, current):
    if current == "(":
        return last == ")"
    return last == "[" and current == "]"

for i in range(0, count):
    b = True
    for char in file.readline():
        if char == "\n":
            continue

        if char == "(" or char == "]":
            tStack.add(char)
        else:
            if tStack.length == 0 or inversed(tStack.last(), char):
                b = False
                break
            else:
                tStack.pop()
    if b and tStack.length == 0:
        result.append("YES")
    else:
        result.append("NO")
    tStack.clear()

write = open("output.txt", "w")
write.write("\n".join(result))
file.close()
write.close()