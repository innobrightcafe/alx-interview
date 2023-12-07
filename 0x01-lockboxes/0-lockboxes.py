#!/usr/bin/python3
def canUnlockAll(boxes):
    """Set to keep track of opened boxes"""
    opened_boxes = set()

    """Stack for DFS"""
    stack = [0]
    """Start with the first box"""

    while stack:
        current_box = stack.pop()
        opened_boxes.add(current_box)

        """Explore keys in the current box"""
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                stack.append(key)

    """Check if all boxes have been opened"""
    return len(opened_boxes) == len(boxes)
