'''import sys
import re

pattern = r'\b(\w{2,})\b'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r"\2\1", line))
'''

import sys
import re

pattern = r'\b(\w)(\w)'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, r"\2\1", line))