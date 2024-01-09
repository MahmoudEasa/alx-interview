#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened
"""


def append_to_array(src, boxes_len, boxes, arr_to_append):
    """ Append keys to array """
    for key in src:
        if key < boxes_len and key > 0:
            if key not in arr_to_append:
                arr_to_append.append(key)
            for k in boxes[key]:
                if k not in arr_to_append:
                    arr_to_append.append(k)


def canUnlockAll(boxes):
    """ Can Unlock All

        Args:
            boxes: a list of lists
    """
    if not boxes or not isinstance(boxes, list) or\
            not all(isinstance(box, list) for box in boxes):
        return (False)

    boxes_len = len(boxes)

    if boxes_len == 1:
        return (True)

    unloced_keys = [0]

    for i in range(boxes_len):
        if i in unloced_keys:
            append_to_array(boxes[i], boxes_len, boxes, unloced_keys)

    if len(unloced_keys) < (boxes_len + 1):
        return (False)

    return (True)
