#Write all your code here
# Import module
import random

# Constants
EASY_RATE = 10/100
MEDIUM_RATE = 30/100
HARD_RATE = 50/100

def init_board(nb_rows, nb_cols, value):
    """
    (int,int, any immutable type) -> list
    Constructs a 2D list, consisted of (nb_rows) nested lists, and (nb_cols)
    elements in each nested list. These elements are associated to the argument
    (value).
    >>> init_board(3, 3, 0)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>>init_board(2, 2, 2)
    [[2, 2], [2, 2]]
    >>>init_board(3, 2, 'hello')
    [['hello', 'hello'], ['hello', 'hello'], ['hello', 'hello']]
    """
    list_2D = []

    for i in range(nb_rows):
        # Creating a nested list
        new_list = []

        for j in range(nb_cols):
            # Add element to each sublist
            new_list.append(value)

        # Adding the nested list as an element in the list_2D
        list_2D.append(new_list)

    return list_2D

def count_total(board, value):
    """
    (list, any type of input) -> int
    Checks how many times (value) occurs in the given 2D list (board)
    by going through the nested list.
    >>> count_total([['?','4','?'], ['2','?','?']],'?')
    4
    >>> count_total([[2,'4',2], ['2',2,1]],2)
    3
    >>> count_total([[2,'4',2], ['2','G','g']],'g')
    1
    """
    # Initiate counter
    counter = 0

    # Going through the sublists in the list
    for sublist in board:
        # Going through the elements in the sublist
        for element in sublist:
            if element == value:
                counter+=1
    return counter
            
def is_valid_position(board, row, col):
    """
    (list, int, int) -> bool
    Checks if (row) is in the range of the number of nested lists in board, and 
    if (col) is in the range of the number of the elements in the nested lists of
    board.
    >>> board = init_board(5, 5, 0)
    >>> is_valid_position(board, 2, 2)
    True
    >>> board = init_board(3, 4, 3)
    >>> is_valid_position(board, 3, 4)
    False
    >>> board = init_board(3, 3, 1)
    >>> is_valid_position(board, 0, 2)
    True
    """
    # Conditions for not out-of-range row indices 
    if row >= 0 and row <= len(board) - 1:
        for sub_list in board:
            # Conditions for not out-of-range column indices
            if col >= 0 and col <= len(sub_list) - 1:
                return True

    # In case indices are out-of-range
    else:
        return False
                
def get_neighbour_positions(board, row, col):
    """
    (list, int, int) -> list
    Gives back the positions (list of nested lists containing integers) of the
    neighbouring elements of (row, col) in the list (board).
    
    >>> board = init_board(3, 3, 0)
    >>> get_neighbour_positions(board, 1, 1)
    [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]

    >>> board = init_board(1, 2, 0)
    >>> get_neighbour_positions(board, 0, 0)
    [[0, 1]]
    
    >>> board = init_board(6, 4, 0)
    >>> get_neighbour_positions(board, 3, 2)
    [[2, 1], [2, 2], [2, 3], [3, 1], [3, 3], [4, 1], [4, 2], [4, 3]]
    """
    neighb_pos = []

    # Let i be the row index 
    for i in range(len(board)):
        # Adjacent rows condition
        if i == row - 1 or i == row or i == row + 1:
            sub_list = board[i]
            # Let j be the column index
            for j in range(len(sub_list)):
                # Adjacent columns condition and verifying that the coordinate
                # obtained (i,j) is valid and that its not (row,col) itself
                if (j == col - 1 or j == col or j == col + 1) and (
                    is_valid_position(board, i, j) == True) and (
                        (i, j) != (row, col)):
                    
                    neighb_pos += [[i, j]]
                    
    return neighb_pos

def count_neighbours(board, row, col, value):
    """
    (list, int, int, any type of input) -> int
    Gives how many elements at the neighbouring positions of (row, col) in
    the 2d list (board) are associated to the value.
    >>> count_neighbours([[1, 1, 0, 0], [-1, 2, 1, 1], [1, 3, -1, 2],
    [0, 2, -1, 2]], 2, 1, -1)
    3
    
    >>> count_neighbours([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 1, 5)
    1
    
    >>> count_neighbours([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 1, 1)
    0
    """
    # Initializing counter
    counter = 0

    # Get the list of neighboring positions at (row, col)
    neigh_pos = get_neighbour_positions(board, row, col)

    # Going through the positions of the adjacent cell
    for pos in neigh_pos:
        # First element of the position represents the row index 
        i = pos[0]
        # Second element of the position represents the column index 
        j = pos[1]
        # Increases the counter by 1 if the element at position (i,j) is (value)
        if board[i][j] == value:
            counter += 1
    return counter
  
def new_mine_position(board):
    """
    (list)->(int,int)
    Gives a random position (int,int) of an element in the 2d list (board) that
    is not associated to -1. By calling the function is_valid_position(board, 
    row, col), one can verify that the position returned is a valid one.
    >>>random.seed(202)
    >>>new_mine_position([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    (1, 2)
    >>>random.seed(202)
    >>>new_mine_position([[0, -1, 0], [-1, 0, -1], [0, -1, 0]])
    (1, 1)
    >>>random.seed(202)
    >>>new_mine_position([[-1, -1, -1], [0, -1, -1], [-1, -1, -1]])
    (1, 0)
    """
    # Creating a generator of random positions until we obtain a valid one
    test = True
    while test == True:
        
        # Generate random row position
        rand_i = random.randint(0,len(board)-1)
        
        # Generate random column position
        rand_j = random.randint(0,len(board[0])-1)
        
        # Verifying that the position is valid
        if is_valid_position(board, rand_i, rand_j) == True:
            
            # Checking if the element at this position is not -1
            if board[rand_i][rand_j] != -1:
                test == False
                return rand_i, rand_j

def new_mine(board):
    """
    (list) -> None
    Modifies the element at the randomly generated position on the list (board)
    (from the function new_mine_position) to -1. Also, inscreases by 1 the
    values of the elements at the adjacent positions if they're not equal to -1.
    
    >>> random.seed(202)
    >>> board = init_board(3, 3, 0)
    >>> board
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> new _mine(board)
    >>> board
    [[0, 1, 1], [0, 1, -1], [0, 1, 1]]
    
    >>> random.seed(202)
    >>> board = init_board(4, 4, 1)
    >>> board
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    >>> new _mine(board)
    >>> board
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 2, 2], [1, 1, 2, -1]]
    
    >>> random.seed(202)
    >>> board = init_board(2, 2, 0)
    >>> board
    [[0, 0], [0, 0]]
    >>> new_mine(board)
    >>> board
    [[1, 1], [1, -1]]
    """
    #Calling the new position for mine
    new_mine_i, new_mine_j = new_mine_position(board)
    
    # Changing the value of the element at that position to -1, turning it
    # into a mine
    board[new_mine_i][new_mine_j] = -1
    
    # Get all valid adjacent positions
    adj_pos = get_neighbour_positions(board, new_mine_i, new_mine_j)
    
    for position in adj_pos:
        # Associating each coordinate in position to its corresponding element
        # in board, and increasing it by 1
        row = position[0]
        column = position[1]
        if board[row][column] != -1:
            board[row][column] += 1
        
def generate_helper_board(nb_rows, nb_cols, nb_mines):
    """
    (int, int, int) -> list
    Generates a 2d list of (nb_rows) sublists and (nb_cols) elements in the
    sublists (which is why nb_rows and nb_cols must be positive integers). Then,
    by calling new_mine(board), adds a limited number of mines (nb_mines) on 
    the list
    
    >>> random.seed(202)
    >>> generate_helper_board(5, 5, 7)
    [[0, 0, 2, -1, -1], [1, 1, 3, -1, 3], [2, -1, 4, 2, 2], [2, -1, 3, -1, 2],
    [1, 1, 2, 2, -1]]
    >>> generate_helper_board(7, 7, 0) == init_board(7, 7, 0)
    True
    
    >>> random.seed(202)
    >>> generate_helper_board(3, 3, 4)
    [[2, -1, 3], [2, -1, -1], [1, 3, -1]]
    >>> generate_helper_board(3, 3, 0) == init_board(3, 3, 0)
    True
    
    >>> random.seed(202)
    >>> generate_helper_board(3, 3, 4)
    [[2, -1, 3], [2, -1, -1], [1, 3, -1]]
    >>> generate_helper_board(3, 3, 0) == init_board(3, 3, 0)
    True
    """
    #Creating a 2d list containing 0s
    board = init_board(nb_rows, nb_cols, 0)
    
    #Adding (nb_mines) mines in the list 
    curr_nb_mines = 1
    while curr_nb_mines <= nb_mines:
        new_mine(board)
        curr_nb_mines += 1
        
    return board

def flag(board, row, col):
    """
    (list, int, int) -> None
    Associates the flag character '\u2691' to the element at position (row, col)
    on the 2d list of characters (board) that is '?', or vice versa.
    
    >>> board = [['1', '1', '1', '0'], ['1', '?', '1', '0'], ['?','?', '?',
    '?']]
    >>> flag(board, 1, 1)
    >>> board
    [['1', '1', '1', '0'], ['1', '⚑', '1', '0'], ['?', '?', '?', '?']]
    
    >>> board = [['⚑', '1', '⚑', '0'], ['1', '?', '1', '⚑'], ['?','⚑', '?',
    '?']]
    >>> flag(board, 0, 0)
    >>> board
    [['?', '1', '⚑', '0'], ['1', '?', '1', '⚑'], ['?', '⚑', '?', '?']]
    
    >>> board = [['⚑', '1', '⚑', '0'], ['1', '?', '1', '⚑'], ['?','⚑', '?',
    '?']]
    >>> flag(board, 2, 0)
    >>> board
    [['?', '1', '⚑', '0'], ['1', '?', '1', '⚑'], ['⚑', '⚑', '?', '?']]
    """
    #Flags an unknown cell
    if board[row][col] == '?':
        board[row][col] = '\u2691'
        return
    
    #Unflags a flagged cell
    if board[row][col] == '\u2691':
        board[row][col] = '?'
        return 

def reveal(helper_board, game_board, row, col):
    """
    (list, list, int, int) -> None
    Reveals if the element at position (row, col) in the 2d list of integers
    (helper_board) is a mine or not. If it's a mine, so associated to the value
    -1, then the function raises an AssertionError with the message 'BOOM! You
    lost.' Otherwise, the element at the position (row, col) in the 2d list of
    characters (game_board) will be updated to the value of the corresponding
    element that's not -1 in (helper_board).
    
    >>> helper_board = [[2, -1, 1], [-1, 4, 3], [2, -1, -1]]
    >>> game_board = init_board(3, 3, '?')
    >>> game_board
    [['?', '?', '?'], ['?', '?', '?'], ['?', '?', '?']]
    >>> reveal(helper_board, game_board, 2, 2)
    Traceback (most recent call last):
    AssertionError: BOOM! You lost.
    
    >>> helper_board = [[2, -1], [-1, 4]]
    >>> game_board = init_board(2, 2, '?')
    >>> game_board
    [['?', '?'], ['?', '?']]
    >>>reveal(helper_board, game_board, 0, 1)
    Traceback (most recent call last):
    AssertionError: BOOM! You lost.
    
    >>> helper_board = [[2, -1], [-1, 4]]
    >>> game_board = init_board(2, 2, '?')
    >>> game_board
    [['?', '?'], ['?', '?']]
    >>> reveal(helper_board, game_board, 0, 0)
    >>> game_board
    [['2', '?'], ['?', '?']]
    """
    if helper_board[row][col] == -1:
        raise AssertionError('BOOM! You lost.')
    
    else:
        # Updates the string at position (row, col) on game_board to the string
        # representation of the integer found in helper board.
        game_board[row][col] = str(helper_board[row][col])
        

def print_board(board):
    """
    Prints the 2d list of characters (board) such that the rows are seperated by
    a new line and the colons are seperated by spaces.
    
    >>> board = [list('002⚑?'), list('113⚑?'), list('??4??'), list('?'*5),
    list('?'*5)]
    print_board(board)
    0 0 2 ⚑ ?
    1 1 3 ⚑ ?
    ? ? 4 ? ?
    ? ? ? ? ?
    ? ? ? ? ?
    
    >>> board = [list('⚑02⚑?'), list('?13⚑?'), list('??4?⚑'), list('⚑'*5),
    list('?'*5)]
    print_board(board)
    ⚑ 0 2 ⚑ ?
    ? 1 3 ⚑ ?
    ? ? 4 ? ⚑
    ⚑ ⚑ ⚑ ⚑ ⚑
    ? ? ? ? ?
    
    >>> board = [list('⚑02??'), list('??3⚑?'), list('??4?⚑'), list('⚑'*5),
    list('4'*5)]
    ⚑ 0 2 ? ?
    ? ? 3 ⚑ ?
    ? ? 4 ? ⚑
    ⚑ ⚑ ⚑ ⚑ ⚑
    4 4 4 4 4
    """
    for sub_list in board:
        # Converts the sublists to strings with spaces seperated between each
        # element of the sublists. 
        line = " ".join(sub_list)
        print(line)
        
def play():
    """
    (None) -> None
    
    First, it initializes the boards. To do so, it asks the user for number of
    rows number of columns of the helper and game boards, and the difficulty
    level. To generate boards, it calls the init_board() function, and the
    helper and the game board will respectively contain '0' and '?'.
    The number of mines depends on the level of difficulty. It will
    determine the number of values that will take the argument -1 in the helper
    board. To finalize the helper board, the function will call new_mine()
    
    Second, as long as the function doesn't raise an AssertionError, the
    function computes the number of elements associated to -1 in the helper
    board, while substracting the number of flags from it (call the function
    count_total()). This is will be printed as the number of mines remaining,
    along with the current board. The function will either use the reveal()
    function or the flag() function, depending on the user's choice (between
    0 or 1).
    
    Finally, once the user reveals all the cells that are not -1, the function
    prints a congratulation message, while also printing the final board by
    representing the mine characters as flags. 
    """
    # First part
    # Getting needed information to generate the boards by calling other
    # functions
    nb_rows = int(input("Enter number of rows for the boards: "))
    nb_cols = int(input("Enter number of columns for the boards: "))
    diff_level = input("Choose a difficulty from [EASY, MEDIUM, HARD]: ")
    
    # Generate game board
    game_board = init_board(nb_rows, nb_cols, '?')
    
    # Get number of mines
    if diff_level == 'EASY':
        nb_mines = int((EASY_RATE * nb_rows * nb_cols)//1)
    elif diff_level == 'MEDIUM':
        nb_mines = int((MEDIUM_RATE * nb_rows * nb_cols)//1)
    elif diff_level == 'HARD':
        nb_mines = int((HARD_RATE * nb_rows * nb_cols)//1)
    
    # Generate helper board
    helper_board = generate_helper_board(nb_rows, nb_cols, nb_mines)
    
    print('Current Board: ('+ str(nb_mines), "mines remaining)")
    print_board(game_board)

    # Computes the number of non-mine cells in the helper board
    nb_non_mines = nb_rows * nb_cols - nb_mines
    
    # Number of revealed non mines
    nb_curr_non_mines = 0

    # Launching a continuous loop 
    gameplay = True
    while gameplay == True:
        user_choice = int(input("Choose 0 to reveal or 1 to flag: "))
        row_choice = int(input("Which row? "))
        col_choice = int(input("Which column? "))
        
        # Applying game conditions depending on the user's choice 
        if user_choice == 0:
            reveal(helper_board, game_board, row_choice, col_choice)
            nb_curr_non_mines += 1
            
        elif user_choice == 1:
            flag(game_board, row_choice, col_choice)
            nb_mines -= 1
            
        # Verify if all of the non-mines are revealed
        if nb_curr_non_mines == nb_non_mines:
            for i in range(0, nb_rows):
                for j in range(0, nb_cols):
                    if game_board[i][j] == '?':
                        game_board[i][j] = '⚑'
            print("Congratulations! You won!")
            print("Final Board:")
            print_board(game_board)
            return
        
        else:
            print('Current Board: ('+ str(nb_mines), "mines remaining)")
            print_board(game_board)
        
def left_click(row, col):
    reveal(helper_board, game_board, row, col)

def right_click(row,col):
    flag(game_board, row, col)
    
def solve_cell(board, row, col, left_click, right_click):
    """
    (list, int, int, function, function) -> None
    The goal of this function is to solve a cell at position (row, col) on the
    game_board (board) by revealing or flagging its adjacent cells. It gets the
    number of adjacent mines and non-mines through the integer representation of
    the cell at (row, col), it finds the number of adjacent flagged cells and
    revealed neighbors by calling the function count_neighbours(board, row,
    col, value). Also, it calls the function left_click to reveal all of
    the adjacent non-mine cells, and it calls the function right_click to flag
    all of the adjacent mines. The function doesn't do anything if the cell if
    already solved, or if the conditions don't apply.
    """
    # Get number of flagged cells
    nb_adj_flags = count_neighbours(board, row, col, '\u2691')
    
    # Get neighboring positions of the cell (row, col)
    neigh_pos = get_neighbour_positions(board, row, col)
    
    # Get number of unrevealed cells
    nb_adj_unrev = count_neighbours(board, row, col, '?')
    
    # Get number of revealed neighbors
    nb_adj_rev = len(neigh_pos) - nb_adj_flags - nb_adj_unrev 
    
    
    # Verifying that the cell at (row, col) is an integer and not '?'
    if board[row][col] == '?' or board[row][col] == '\u2691':
        return
    else:
        # Get number of adjacent mines
        nb_adj_mines = int(board[row][col])
    
        # Get number of adjacent non-mines
        nb_adj_non_mines = len(neigh_pos) - nb_adj_mines
    
        # Reveal all the adjacent non-mine cells
        if nb_adj_flags == int(board[row][col]):
            for pos in neigh_pos:
                if board[pos[0]][pos[1]] != '\u2691' and \
                   board[pos[0]][pos[1]] == '?':
                        left_click(pos[0], pos[1])
                    
        # Flag all the adjacent mines         
        elif nb_adj_rev == nb_adj_non_mines:
            for pos in neigh_pos:

                if board[pos[0]][pos[1]] != '\u2691' and \
                   board[pos[0]][pos[1]] == '?':

                        right_click(pos[0], pos[1])
  

def solve(board, left_click, right_click):
    """
    (list, function, function) -> None
    This function solves all of the cells that still contain the character '?'
    on the game board (board). It will be calling solve_cell(board, row, col,
    left_click, right_click) on every single one of those cells. 
    """
    while count_total(board, '?') >= 1:
        for i in range(len(board)):
            for j in range(len(board[i])):
                solve_cell(board, i, j, left_click, right_click)
                

                

