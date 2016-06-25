import os
import daedalus
os.system('clear')


def print_labyrinth(my_labyrinth):
    max_cols = len(my_labyrinth[0])
    max_lines = len(my_labyrinth)
    print(max_cols)
    print(max_lines)
    for one_line in range(max_lines):
        my_line=''
        for one_column in range(max_cols):
            my_line = my_line+my_labyrinth[one_line][one_column]
        print(my_line + ' ' + str(one_line))

daedalus.create_labyrinth(daedalus.num_columns, daedalus.num_lines)

print_labyrinth(daedalus.my_labyrinth)
