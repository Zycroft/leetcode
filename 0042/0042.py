"""
:type height: List[int]
:rtype: int
"""
"""
for (i, col) in enumerate(height, start=1):
    print(i, col)
    if col > maxcolHeight:
        maxcolHeight = col
        maxcolHindx = i
        # print(f"maxcolHeight: {maxcolHeight}, maxcolHindx: {maxcolHindx}")

for i in range(maxcolHindx, 0, -1):
    print(f"index i: {i}, height[{i}]: {height[i]}")
    # print(i)
    """

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = 0
l = 0
r = len(height) - 1
maxL = height[l]
maxR = height[r]

while l < r:
    if maxL < maxR:
        ans += maxL - height[l]
        l += 1
        maxL = max(maxL, height[l])
        print(f"Left l: {l}, maxL: {maxL}, height[l]: {height[l]}, ans: {ans}")
    else:
        ans += maxR - height[r]
        r -= 1
        maxR = max(maxR, height[r])
        print(
            f"Right r: {r}, maxR: {maxR}, height[r]: {height[r]}, ans: {ans}")
