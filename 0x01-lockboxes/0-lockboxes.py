#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """ Can Unlock All

        Args:
            boxes: a list of lists
    """

    boxes_len = len(boxes)

    for i in range(1, boxes_len):
        unlocked = False
        for j in range(boxes_len):
            if j != i and i in boxes[j]:
                unlocked = True
                break

    return (unlocked)
