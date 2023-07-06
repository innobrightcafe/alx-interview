#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    """
    Set to track visited boxes
    """
    visited = set()
    """
    Start with the first box
    """ 
    stack = [0]  

    while stack:
        box = stack.pop()
        visited.add(box)
        """
        check to open all boxes
        """
        for key in boxes[box]:
            if key not in visited and key < n:
                stack.append(key)

    return len(visited) == n
