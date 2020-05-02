# Define a function which finds the location of 0 in an 4x4 array and returns it as a tuple (x,y) where the top
# left corner is (0,0).
def find_zero(array):
    location = (0,0)
    y = 0
    for row in array:
        if row.count(0) == 1:
            location = (row.index(0), y)
        else:
            y += 1
    return location

# Now define the functions which allow the 0 tile, representing the blank tile from the puzzle,
# to move up, down, left and right.

def move_up(array):
    # If the 0 is in the top row return an error code
    if array[0].count(0) == 1:
        return 1

    # If the 0 is not in the top row swap the 0 with the number above it.
    else:
        x, y = find_zero(array)
        # Find the number to swap with
        number_to_swap = array[y-1][x]
        # Set the 0 to the new number
        array[y][x] = number_to_swap
        # Set the number to swap with to 0.
        array[y-1][x] = 0

    return array
