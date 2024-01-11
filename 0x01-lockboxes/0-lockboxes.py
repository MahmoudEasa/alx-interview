#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened
"""


def append_to_set(index, boxes_len, boxes, set_to_append):
    """ Append keys to array """
    for key in boxes[index]:
        if key < boxes_len and key not in set_to_append:
            set_to_append.add(key)
            for k in boxes[key]:
                if k not in set_to_append:
                    set_to_append.add(k)


def canUnlockAll(boxes):
    """ Can Unlock All

        Args:
            boxes: a list of lists
    """
    if not isinstance(boxes, list):
        return (False)

    boxes_len = len(boxes)

    if boxes_len <= 1:
        return (True)

    unlocked_keys = {0}

    for i in range(boxes_len):
        if i in unlocked_keys:
            append_to_set(i, boxes_len, boxes, unlocked_keys)

    if not all(i in unlocked_keys for i in range(boxes_len)):
        return (False)

    return (True)
