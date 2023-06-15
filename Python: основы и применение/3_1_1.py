s,a,b = (input() for i in range(3))
counter = 0

while a in s:
    if counter>1000:
        print("Impossible")
        break
    s = s.replace(a, b)
    counter += 1
else:
    print(counter)
