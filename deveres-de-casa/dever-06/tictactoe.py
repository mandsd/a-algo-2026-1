import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    possible = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible.add((i, j))
    return possible


def result(board, action):
    if action not in actions(board):
        raise Exception("Ação inválida")
    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    lines = []
    # linhas
    for row in board:
        lines.append(row)
    # colunas
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])
    # diagonais
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] is not None:
            return line[0]
    return None


def terminal(board):
    if winner(board) is not None:
        return True
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))


def utility(board):
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0


def minimax(board):
    if terminal(board):
        return None

    current = player(board)

    if current == X:
        best_val = float("-inf")
        best_action = None
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_action = action
        return best_action
    else:
        best_val = float("inf")
        best_action = None
        for action in actions(board):
            val = max_value(result(board, action))
            if val < best_val:
                best_val = val
                best_action = action
        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
