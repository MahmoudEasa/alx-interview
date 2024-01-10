#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

if __name__ == "__main__":
    boxes = []

    keys = []
    for n in range(1, 1000):
        keys = []
        for m in range(1, 1000):
            keys.append(m)
        boxes.append(keys)

    print(canUnlockAll(boxes))



"""

canUnlockAll = __import__('0-lockboxes').canUnlockAll
canUnlockAll2 = __import__('main_1').canUnlockAll


print("1")
boxes = [[4]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("2")
boxes = [[3], [2], [1], [0]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("11")
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("3")
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("10")
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("4")
boxes = [[4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [1, 6]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("5")
boxes = [[]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("6")
boxes = [[], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [1, 6]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("7")
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

print("8")
boxes = [[], [], []]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))
"""
