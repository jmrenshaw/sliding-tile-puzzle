# Run this program to provide a solution to the puzzle, the aim is to solve the puzzle in as few moves as possible.
from puzzle_functions import measure_all_moves


# First define the starting array and solution array.
def main():
    starting_array = [[5,2,7,3],[9,1,15,4],[10,6,8,12],[13,11,14,0]]
    finishing_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    print(measure_all_moves(starting_array, finishing_array))

main()