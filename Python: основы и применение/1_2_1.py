objects = [1, 2, 1, 2, 3]
ans = 0
for i in range(len(objects)):
    matches = 0
    for j in range(i + 1, len(objects)):
        if objects[j] is objects[i]:
            matches += 1
    if matches == 0:
        ans += 1
print(ans)

#print(len(set(map(id, objects))))
#print(len(set([id(obj) for obj in objects])))
