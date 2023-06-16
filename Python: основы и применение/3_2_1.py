import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.match(r".*(cat).*\1.*",line):
        print(line)

