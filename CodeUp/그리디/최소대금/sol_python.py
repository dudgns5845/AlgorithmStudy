pasta = []
juice = []
result = []
for i in range(3):
    pasta.append(int(input()))

for i in range(2):
    juice.append(int(input()))

for i in pasta:
    for j in juice:
        result.append((pasta[i]+juice[j])*1.1)

print("%.1f"%result[0])
