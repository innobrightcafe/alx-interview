#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    """
    Set to track visited boxes
    """
    visited = set()
    stack = [0]  

    while stack:
        box = stack.pop()
        visited.add(box)
        for key in boxes[box]:
            if key not in visited and key < n:
                stack.append(key)

    return len(visited) == n
