#!/usr/bin/python3
"""
A method that determines if the given data set represents a valid UTF-8 encoding.
"""
def validUTF8(data):
    """Masks to check the number of bytes in a UTF-8 character"""
    mask1 = 0b10000000
    mask2 = 0b11100000
    mask3 = 0b11110000
    mask4 = 0b11111000

    """Iterate through the list of integers"""
    i = 0
    while i < len(data):
        """Check for a single-byte character"""
        if (data[i] & mask1) == 0:
            i += 1
            """Check for a two-byte character"""
        elif (data[i] & mask2) == 0b11000000:
            if i + 1 >= len(data) or (data[i + 1] & mask2) != 0b10000000:
                return False
            i += 2
            """Check for a three-byte character"""
        elif (data[i] & mask3) == 0b11100000:
            if i + 2 >= len(data) or (data[i + 1] & mask2) != 0b10000000 or (data[i + 2] & mask2) != 0b10000000:
                return False
            i += 3
            """Check for a four-byte character"""
        elif (data[i] & mask4) == 0b11110000:
            if i + 3 >= len(data) or (data[i + 1] & mask2) != 0b10000000 or (data[i + 2] & mask2) != 0b10000000 or (
                    data[i + 3] & mask2) != 0b10000000:
                return False
            i += 4
        else:
            return False

    return True
