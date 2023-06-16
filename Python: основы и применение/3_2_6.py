import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.sub("human","computer",line):
        print(re.sub("human","computer",line))
    else:
        print(line)