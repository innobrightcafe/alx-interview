#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    if not boxes:
        return False

    n = len(boxes)
    status = ["T"] + ["F"] * (n - 1)

    for box in range(n):
        if status[box] == "T" or box == 0:
            for key in boxes[box]:
                if 0 <= key < n and status[key] == "F": 
                    status[key] = "T"
                    for k in boxes[key]:
                        if 0 <= k < n:
                            status[k] = "T"

    return "F" not in status
