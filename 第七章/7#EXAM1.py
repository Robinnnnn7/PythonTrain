f = open('latex.log', 'r', encoding='utf-8')
ff = f.readlines()
s = 0
c = 0
for line in ff:
    line = line.strip("\n")
    if line == "":
        continue
    s += len(line)
    c += 1
print(round(s / c))
    
