#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """ Can Unlock All

        Args:
            boxes: a list of lists
    """
    if not boxes or not isinstance(boxes, list) or\
            not [isinstance(box, list) for box in boxes]:
        return (False)

    boxes_len = len(boxes)
    unlocked = False

    if boxes_len == 1:
        return (True)

    for i in range(1, boxes_len):
        unlocked = False
        for j in range(boxes_len):
            if j != i and i in boxes[j]:
                unlocked = True
                break

    return (unlocked)
