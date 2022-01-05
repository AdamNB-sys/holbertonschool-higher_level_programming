#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if x == 101 or x == 113:
        continue
    else:
        print("{:c}".format(x), end="")
\n
