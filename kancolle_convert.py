#!/usr/bin/env python3

import sys

BAD_SUFFIX = "(kancolle)"
REPLACE_SUFFIX = "(kantai collection)"
REQUIRED_PREFIX = "character:"

BAD_SUFFIX_LEN = len(BAD_SUFFIX)

for line in sys.stdin:

    line = line.strip()
    if not line or not line.startswith(REQUIRED_PREFIX) or not line.endswith(BAD_SUFFIX):
        continue

    print(line)

    print(line[:-BAD_SUFFIX_LEN] + REPLACE_SUFFIX)
