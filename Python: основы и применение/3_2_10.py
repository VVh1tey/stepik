import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.match(r'^[01]+$', line):
        decimal = int(line, 2)
        if decimal % 3 == 0:
            print(line)