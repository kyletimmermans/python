#!/usr/bin/env python3


def shift_array(arr: list[any], direction: str, distance: int) -> list[any]:
	if direction != "left" and direction != "right":
		print("Direction must be 'left' or 'right'!")
		exit(0)
	elif distance < 0:
		print("Distance cannot be a negative number!")
		exit(0)
	elif distance == 0 or len(arr) == 1:
		return arr
	elif len(arr) == 2:
		return [arr[1], arr[0]]

	final_arr = []

	if direction == "left":
		# Take everything that is not being moved to the end, and put in the start
		final_arr.extend(arr[distance::1])
		# Take everything from the start, that will be moved to the end, and move to the end
		final_arr.extend(arr[:distance:1])
	elif direction == "right":
		# Take everything from the end that will be in the start, and put it in the start
		final_arr.extend(arr[len(arr)-distance::1])
		# Take everything from the start that won't be moved back to the start, and move to the end
		final_arr.extend(arr[:len(arr)-distance:1])

	return final_arr



print(shift_array([1, 2, 3, 4], "right", 1))
print(shift_array([1, 2, 3, 4], "right", 2))

print(shift_array([1, 2, 3, 4], "left", 1))
print(shift_array([1, 2, 3, 4], "left", 2))
