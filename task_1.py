""" Github: """

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path, "r") as file:
        result = [ line.replace("\n", "") for line in file ]
    return result

# print(read_input("check.txt"))

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    streak = 0
    needed_streak = pivot
    bigest = 0
    line = input_line[1:-1]
    for i in line:
        if int(i) > bigest:
            streak += 1
            bigest = int(i)
    if streak == needed_streak:
        return True
    return False

def check_left_to_right(input_line: str):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    >>> check_left_to_right("412453*")
    True
    >>> check_left_to_right("452453*")
    False
    """
    if input_line[0] == "*":
        return True
    streak = 0
    needed_streak = int(input_line[0])
    bigest = 0
    line = input_line[1:-1]
    for i in line:
        if int(i) > bigest:
            streak += 1
            bigest = int(i)
    if streak == needed_streak:
        return True
    return False

# print(check_rows("452453*"))


def check_right_to_left(input_line: str):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    >>> check_right_to_left("*123451")
    True
    >>> check_right_to_left("*543211")
    False
    """
    if input_line[-1] == "*":
        return True
    streak = 0
    needed_streak = int(input_line[-1])
    bigest = 0
    line = reversed(input_line[1:-1])
    for i in line:
        if int(i) > bigest:
            streak += 1
            bigest = int(i)
    if streak == needed_streak:
        return True
    return False

# print(check_right_to_left("*123451"))

def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', \
'4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', \
'423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        if "?" in line:
            return False
    return True

# print(check_not_finished_board(['***21**', '412453*', \
# '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', \
'423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1:-1]:
        if len(set(line[1:-1])) != len(line[1:-1]):
            return False
    return True

# print(check_uniqueness_in_rows(['***21**', '452453*', \
# '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**','452453*', \
'423145*','*543215','*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', \
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    if not check_uniqueness_in_rows(board):
        return False
    for line in board[1:-1]:

        if not check_left_to_right(line):
            return False

        elif not check_right_to_left(line):
            return False
    return True

# print(check_horizontal_visibility(['***21**', '412453*', \
# '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', \
'*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', \
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    if not check_columns_to_top(board):
        return False
    towers = [line[1:-1] for line in board[1:-1]]
    for i in range(len(towers[0])):
        numbers = set()
        for line in towers:
            if line[i] not in numbers:
                numbers.add(line[i])
            else:
                return False
    for num,lenght in enumerate(board[0]):
        if lenght != "*":
            streak = 0
            bigest = 0
            for i in board[1:-1]:
                if int(i[num]) > bigest:
                    streak += 1
                    bigest = int(i[num])
            if streak != int(lenght):
                return False
    return True


# print(check_columns_to_down(['***21**', '412453*', '423145*', \
# '*543215', '*35214*', '*41532*', '*2*1***']))

def check_columns_to_top(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.
    >>> check_columns_to_top(["*1","*5","*4","*3","*3"])
    True
    """
    board = list(reversed(board))
    for num,lenght in enumerate(board[0]):
        if lenght != "*":
            streak = 0
            bigest = 0
            for i in board[1:-1]:
                if int(i[num]) > bigest:
                    streak += 1
                    bigest = int(i[num])
            if streak != int(lenght):
                return False
    return True

# print(check_columns_to_top(["*1","*5","*4","*3","*3"]))

def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if check_horizontal_visibility(board) and \
check_columns(board) and check_columns_to_top(board):
        return True
    return False


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    # print(check_skyscrapers("check.txt"))
    print(check_columns(['***21**', 
                         '412453*', 
                         '423145*', 
                         '*543215', 
                         '*35214*', 
                         '*41532*', 
                         '*2*4***']))