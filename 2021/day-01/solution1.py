#!/usr/bin/python

counter = 0
resetDepth = None
with open('input') as f:
    while True:
        line = f.readline()
        if not line:
            break

        depth = int(line)

        if not resetDepth:
            resetDepth = depth

        if depth > resetDepth:
            counter += 1

        resetDepth = depth


print(counter)
