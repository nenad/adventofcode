#!/usr/bin/python

queue = []
counter = 0
resetDepth = None

with open('input') as f:
    while True:
        line = f.readline()
        if not line:
            break

        depth = int(line)

        queue.append(depth)
        # print(queue)

        if len(queue) == 4:
            a = sum(queue[0:3])
            b = sum(queue[1:4])
            # print(a, b)
            if b > a:
                counter += 1
                # print("Yes")
            queue = queue[1:4] # Pop the first element


print(counter)
