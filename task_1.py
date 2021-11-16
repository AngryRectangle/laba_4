import TrueStack


# Meaningless code....
s = TrueStack.TrueStack()
file = open("input.txt", "r")
result = []
count = int(file.readline())
for i in range(0, count):
    data = file.readline().split()
    if data[0] == "-":
        result.append(str(s.pop()))
    else:
        s.add(int(data[1]))

write = open("output.txt", "w")
write.write("\n".join(result))
file.close()
write.close()