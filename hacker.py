# import curses
# import random
# import time

# def print_random_number(win, row, col):
#     number = random.randint(1000, 9999)
#     color = random.randint(1, curses.COLORS - 1)
#     win.addstr(row, col, str(number), curses.color_pair(color))
#     win.refresh()

# def prank_terminal(stdscr):
#     curses.start_color()
#     curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
#     curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
#     curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
#     curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
#     curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
#     curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

#     curses.curs_set(0)  # Hide the cursor
#     stdscr.clear()

#     max_y, max_x = stdscr.getmaxyx()

#     while True:
#         row = random.randint(0, max_y - 1)
#         col = random.randint(0, max_x - 5)
#         print_random_number(stdscr, row, col)
#         time.sleep(0.2)

# curses.wrapper(prank_terminal)

























import curses
import random
import time

def print_random_number(win, row, col, number, color):
    win.addstr(row, col, str(number), curses.color_pair(color))
    win.refresh()

def prank_terminal(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    max_y, max_x = stdscr.getmaxyx()

    numbers = []

    while True:
        for number in numbers:
            row, col, value, color = number
            print_random_number(stdscr, row, col, value, color)

        # Add a new number at the top
        new_number = (0, random.randint(0, max_x - 5), random.randint(1000, 9999), random.randint(1, curses.COLORS - 1))
        numbers.append(new_number)

        # Remove numbers that have reached the bottom
        numbers = [(row + 1, col, value, color) for row, col, value, color in numbers if row + 1 < max_y]

        time.sleep(0.1)
        stdscr.clear()

curses.wrapper(prank_terminal)
