"""
:type height: List[int]
:rtype: int
"""

maxcolHeight = 0
maxcolHeight = 0
maxcolHindx = 0

for (i, col) in enumerate(height, start=1):
    print(i, col)
    if col > maxcolHeight:
        maxcolHeight = col
        maxcolHindx = i
        print(maxcolHeight, maxcolHindx)

    for i in range(maxcolHindx, 1, -1):
        print(height[i])
        # print(i)
