import os
import random
import daedalus
os.system('clear')

symbol_wall = '|'
symbol_floor = ' '
num_columns = 50
num_lines = 20
my_labyrinth = []


def create_tile(num_columns, num_lines, column_number, line_number):
    random_even = [symbol_wall] * 6 + [symbol_floor] * 6
    random_odd  = [symbol_wall] * 4 + [symbol_floor] * 4
    if line_number == 0 or column_number == 0 \
    or column_number == num_columns - 1 or line_number == num_lines - 1:
        tile = symbol_wall
    else:
        if (line_number % 2 == 0 or column_number % 2 == 0):
            tile = random.choice(random_even)
        else:
            tile = random.choice(random_odd)
    return tile


def create_line(num_columns, num_lines, line_number):
    curr_line = []
    for i in range(num_columns):
        curr_line.extend(create_tile(num_columns, num_lines, i, line_number))
    return curr_line


def create_labyrinth(num_columns, num_lines):
    for i in range(num_lines):
        my_labyrinth.append(create_line(num_columns, num_lines, i))
    return my_labyrinth


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

create_labyrinth(num_columns, num_lines)

print_labyrinth(my_labyrinth)
