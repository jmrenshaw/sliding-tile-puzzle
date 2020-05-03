import numpy as np
import copy

# Define a function which finds the location of a number in an 4x4 array and returns it as a tuple (x,y) where the top
# left corner is (0,0).
def find_number(number, array):
    location = (0,0)
    y = 0
    for row in array:
        if row.count(number) == 1:
            location = (row.index(number), y)
        else:
            y += 1
    return location

# Now define the functions which allow the 0 tile, representing the blank tile from the puzzle,
# to move up, down, left and right.

def move_up(array):
    # If the 0 is in the top row return an error code
    x, y = find_number(0,array)
    if y == 0:
        return 1

    # If the 0 is not in the top row swap the 0 with the number above it.
    else:
        # Find the number to swap with
        number_to_swap = array[y-1][x]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y-1][x] = 0

    return array

def move_down(array):
    # If the 0 is in the bottom row return an error code
    x, y = find_number(0,array)
    if y == 3:
        return 1

    # If the 0 is not in the bottom row swap the 0 with the number below it.
    else:
        # Find the number to swap with
        number_to_swap = array[y+1][x]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y+1][x] = 0

    return array

def move_left(array):
    # If the 0 is in the left column return an error code
    x, y = find_number(0,array)
    if x == 0:
        return 1

    # If the 0 is not in the left column swap the 0 with the number to the left of it.
    else:
        # Find the number to swap with
        number_to_swap = array[y][x-1]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y][x-1] = 0

    return array

def move_right(array):
    # If the 0 is in the right column return an error code
    x, y = find_number(0,array)
    if x == 3:
        return 1

    # If the 0 is not in the right column swap the 0 with the number to the right of it.
    else:
        # Find the number to swap with
        number_to_swap = array[y][x+1]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y][x+1] = 0

    return array

def measure_mean_std_dev(input_array, result_array):
    measure_array = []
    for i in range(16):
        input_x, input_y = find_number(i,input_array)
        result_x, result_y = find_number(i, result_array)
        distance = abs(result_x - input_x) + abs(result_y - input_y)
        measure_array.append(distance)
    return {"mean":np.mean(measure_array), "std_dev":np.std(measure_array)}

def measure_move(input_array, result_array, direction):
    copy_array = copy.deepcopy(input_array)
    if direction == "up":
        moved_array = move_up(copy_array)
        if moved_array == 1:
            return 1
        else:
            return measure_mean_std_dev(moved_array, result_array)
    elif direction == "down":
        moved_array = move_down(copy_array)
        if moved_array == 1:
            return 1
        else:
            return measure_mean_std_dev(moved_array, result_array)
    elif direction == "left":
        moved_array = move_left(copy_array)
        if moved_array == 1:
            return 1
        else:
            return measure_mean_std_dev(moved_array, result_array)
    elif direction == "right":
        moved_array = move_right(copy_array)
        if moved_array == 1:
            return 1
        else:
            return measure_mean_std_dev(moved_array, result_array)

def measure_all_moves(input_array, result_array):
    results = {"up":0, "down":0, "left":0, "right":0}
    results["up"] = measure_move(input_array, result_array, "up")
    results["down"] = measure_move(input_array, result_array, "down")
    results["left"] = measure_move(input_array, result_array, "left")
    results["right"] = measure_move(input_array, result_array, "right")
    return results