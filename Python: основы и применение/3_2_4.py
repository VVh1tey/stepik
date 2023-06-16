import sys

for line in sys.stdin:
    line = line.rstrip()
    if "\\" in line:
        print(line)