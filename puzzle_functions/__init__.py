import numpy as np
import copy
import time

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

def move(array, direction):

    x, y = find_number(0,array)

    if direction == 'u':
        # If the 0 is in the top row return an error code
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

    if direction == 'd':
        # If the 0 is in the bottom row return an error code
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

    if direction == 'l':
        # If the 0 is in the left column return an error code
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

    if direction == 'r':
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
    moved_array = move(copy_array, direction)
    if moved_array == 1:
        return 1
    else:
        return measure_mean_std_dev(moved_array, result_array)

def measure_all_moves(input_array, result_array):
    results = {"up":0, "down":0, "left":0, "right":0}
    results["up"] = measure_move(input_array, result_array, 'u')
    results["down"] = measure_move(input_array, result_array, 'd')
    results["left"] = measure_move(input_array, result_array, 'l')
    results["right"] = measure_move(input_array, result_array, 'r')
    return results

def solved(input_array, result_array):
    if input_array == result_array:
        return True
    else:
        return False

def solve_using_mean(input_array, result_array):
    moving_array = copy.deepcopy(input_array)
    i = 0
    move_list = []
    while True:
        opposite_moves = {"up":"down","down":"up","left":"right","right":"left"}
        if solved(moving_array,result_array):
            break
        measured_moves = measure_all_moves(moving_array, result_array)
        key_list = ["up","down","left","right"]
        for key in key_list:
            if measured_moves[key] == 1:
                measured_moves.pop(key)
            else:
                continue
        if move_list:
            measured_moves.pop(opposite_moves[move_list[-1]])

        first_iteration = True
        for key in measured_moves:
            if first_iteration:
                lowest_mean = measured_moves[key]["mean"].item()
                smallest_key = key
                first_iteration = False
            else:
                current_mean = measured_moves[key]["mean"].item()
                if current_mean < lowest_mean:
                    smallest_key = key

        if smallest_key == "up":
            move(moving_array,'u')
            move_list.append("up")
        if smallest_key == "down":
            move(moving_array,'d')
            move_list.append("down")
        if smallest_key == "left":
            move(moving_array,'l')
            move_list.append("left")
        if smallest_key == "right":
            move(moving_array,'r')
            move_list.append("right")

        #print(find_number(0,moving_array))
        #time.sleep(1)

        i += 1
        if i == 1000:
            break
    return i

def solve_using_stddev(input_array, result_array):
    moving_array = copy.deepcopy(input_array)
    i = 0
    move_list = []
    while True:
        opposite_moves = {"up":"down","down":"up","left":"right","right":"left"}
        if solved(moving_array,result_array):
            break
        measured_moves = measure_all_moves(moving_array, result_array)
        key_list = ["up","down","left","right"]
        for key in key_list:
            if measured_moves[key] == 1:
                measured_moves.pop(key)
            else:
                continue
        if move_list:
            measured_moves.pop(opposite_moves[move_list[-1]])

        first_iteration = True
        for key in measured_moves:
            if first_iteration:
                lowest_stddev = measured_moves[key]["std_dev"].item()
                smallest_key = key
                first_iteration = False
            else:
                current_stddev = measured_moves[key]["std_dev"].item()
                if current_stddev < lowest_stddev:
                    smallest_key = key

        if smallest_key == "up":
            move(moving_array,'u')
            move_list.append("up")
        if smallest_key == "down":
            move(moving_array,'d')
            move_list.append("down")
        if smallest_key == "left":
            move(moving_array,'l')
            move_list.append("left")
        if smallest_key == "right":
            move(moving_array,'r')
            move_list.append("right")

        #print(find_number(0,moving_array))
        #time.sleep(1)

        i += 1
        if i == 1000:
            break
    return i