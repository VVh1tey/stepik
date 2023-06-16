import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\b[aA]+\b", line):
        print(re.sub(r"\b[aA]+\b", "argh", line, count=1))
    else:
        print(line)