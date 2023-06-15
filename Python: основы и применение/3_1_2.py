s, t = (input() for i in range(2))
i = 0
count = 0
while s.find(t, i) != -1:
    count += 1
    i = s.find(t, i) + 1
else:
    print(count)