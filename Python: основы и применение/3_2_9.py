import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"(\w)\1+", r"\g<1>", line))