#!/usr/bin/env python3

'''
Given an array of ints, and an index in that array, determine
which values in the index can be used to move that amount of indexes
across to the given index
'''

def can_jump(arr: list[int], dest: int) -> list[bool]:
        final = []
    
        for i in range(0, len(arr)):
                # If we need to wrap around
                if i > dest:
                        # Distance to get to end of arr + 1 to get to start from end + normal distance
                        if arr[i] >= (len(arr) - 1 - i) + 1 + dest:
                                final.append(True)
                        else:
                                final.append(False)
                        continue
    

                if arr[i] >= abs(dest - i): 
                        final.append(True)
                else:
                        final.append(False)

        return final
    


if __name__ == '__main__':
        print(can_jump([4, 0, 1, 3, 5, 3], 3)) 
        # True, False, True, True, True, False
