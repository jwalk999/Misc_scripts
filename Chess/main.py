"""
Main.py

A two player chess game using pygame-ce

Original built using tutorial:
https://youtu.be/X-e0jk4I938?si=wiSazWKsKIcAOtfd&t=4049
https://github.com/plemaste+9-r01/pygameChess

Main.py refactored and cleaned up

Changes
- fixed nested single if statements with and


"""

# =============================================================================
# ================================ Imports ====================================
# =============================================================================
import pygame

# Initialize pygame
pygame.init()

# =============================================================================
# ================================= Variables =================================
# =================================    and    =================================
# ================================= Constants =================================
# =============================================================================

# Set window size
WIDTH = 1000
HEIGHT = 900
# Set window to scale to monitor? - make window resizeable
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode([WIDTH, HEIGHT], flags)

# Set window caption (top left)
pygame.display.set_caption('Chess!')

# Set 3 different size fonts
font_small = pygame.font.Font('freesansbold.ttf', 20)
font_medium = pygame.font.Font('freesansbold.ttf', 40)
font_large = pygame.font.Font('freesansbold.ttf', 50)

# Set timer and Frames per Second
timer = pygame.time.Clock()
fps = 60

# =============================================================================
# ================================  Game  =====================================
# ===============================  Pieces =====================================
# =============================================================================

# Make the game pieces and place them on the board

# White pieces // on top of board
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
# Set white piece location coordinates (x, y)
white_locations = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]

# Black pieces // on bottom of board
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
# Set black piece location coordinates (x, y)
black_locations = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]

# Create the captured pieces lists
captured_pieces_white = []
captured_pieces_black = []

# Set color turns
turn_step = 0
selection = 100 # dummy variable
valid_moves = []

# Flashing Counter
counter = 0

# Set win condition
winner = ""
game_over = False

# Variables for extra chess rules
# Pawn promotion, castling, en passant
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
check = False
castling_moves = []

# ==============================================================================
# =============================== Game =========================================
# ============================== Images ========================================
# ==============================================================================

 # Load in game piece images yay
 # Queen, King, Rook, Bishop, Knight, Pawn  x2

 # Black Pieces
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))

black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))

black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))

black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))

black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))

black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))

black_promotions = ['bishop', 'knight', 'rook', 'queen']
black_moved = [False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,]


# White Pieces
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_promotions = ['bishop', 'knight', 'rook', 'queen']
white_moved = [False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,]


white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, 
                    white_knight_small, white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]

small_black_images = [black_pawn_small, black_queen_small, black_king_small,
                    black_knight_small, black_rook_small, black_bishop_small]


# Indexing the piece list to associate names and images.
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']


# =============================================================================
# ==================================  Game   ==================================
# ================================== Drawing ==================================
# ================================== Section ==================================
# =============================================================================

# Draw Game board

def draw_board():
    """ Draw the game board"""
    for i in range(32):
        column = i % 4  # i remainder 4 (modulus)
        row = i // 4    # round down to nearest integer
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100]) # give the game some space
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
    pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
    pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
    pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                    'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(font_large.render(status_text[turn_step], True, 'black'), (20, 820))

    for i in range(9):
        pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
        pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
    screen.blit(font_small.render('FORFEIT', True, 'black'), (810, 830))

    # Pawn promote rules
    if white_promote or black_promote:
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH - 200, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH - 200, 100], 5)
        screen.blit(font_large.render('Select Piece to Promote Pawn', True, 'black'), (20, 820))



# Draw game pieces onto board

def draw_pieces():
    """Draw the pieces on the board in each square using above lists
        The piece selected is highlighted: Blue for black, Red for white
    """
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2 and selection == i:
            pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100], 2)


    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2 and selection == i:
            pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2)


# ==============================================================================
# ============================== Piece =========================================
# ============================== Check =========================================
# ==============================================================================

def check_options(pieces, locations, turn):
    # FIX 4: castling is no longer computed here (it used to overwrite a
    # global with whichever king was checked last)
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list



# =============================================================================
# ================================= Piece =====================================
# ================================= Moves =====================================
# ================================= Logic =====================================
# =============================================================================


# Check valid Pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position [1] + 1) not in white_locations and \
        (position[0], position [1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position [0], position[1] + 1))
            if (position[0], position [1] + 2) not in white_locations and \
            (position[0], position [1] + 2) not in black_locations and position[1] == 1:
                moves_list.append((position [0], position[1] + 2))
        if (position [0] + 1, position [1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position [1] + 1))
        if (position [0] - 1, position [1] + 1) in black_locations:
            moves_list.append((position[0]- 1, position [1] + 1))
        # Add en passant move check
        if (position[0] + 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] + 1, position [1] +1))
        if (position [0] - 1, position[1] + 1) == black_ep:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position [1] - 1) not in white_locations and \
        (position[0], position [1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position [0], position[1] - 1))
            if (position[0], position [1] - 2) not in white_locations and \
            (position[0], position [1] - 2) not in black_locations and position[1] == 6:
                moves_list.append((position [0], position[1] - 2))
        if (position [0] + 1, position [1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position [1] - 1))
        if (position [0] - 1, position [1] - 1) in white_locations:
            moves_list.append((position[0]- 1, position [1] - 1))
        # Add en passant move check
        if (position[0] + 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) == white_ep:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# Check valid Rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4): # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# Check valid Knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations

    # 8 squares to check for knights
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)

    return moves_list

# Check valid Bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4): # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False

    return moves_list    

# Check valid Queen moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])

    return moves_list


# Check valid King moves
# Check valid King moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations

    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# Check for valid moves for selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else: 
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# =============================================================================
# =================================   Move  ===================================
# ================================= Drawing ===================================
# =============================================================================


# Draw valid moves on screen as dots, red for white, blue for black
def draw_valid(moves):
    if turn_step < 2: # White's turn
        color = 'red'
    else:             # Black's turn
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

# Draw captured pieces on side of screen
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50*i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50*i))

# Draw a flashing square around King if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i] and counter < 15:
                    pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                        white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i] and counter < 15:
                    pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                        black_locations[king_index][1] * 100 + 1, 100, 100], 5)

# Draw a rectangle for the game winner
def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font_small.render(f"{winner} won the game!", True, 'white'), (210, 210))
    screen.blit(font_small.render("Press ENTER to Restart!", True, 'white'), (210, 240))


# ==============================================================================
# ================================= Special ====================================
# =================================  Moves  ====================================
# ==============================================================================

# Check en passant
def check_ep(old_coords, new_coords):
    if turn_step <= 1:
        index = white_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] - 1)
        piece = white_pieces[index]
    else:
        index = black_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] + 1)
        piece = black_pieces[index]
    
    if piece == 'pawn' and abs(old_coords[1] - new_coords[1]) > 1:
        pass # pass the coords as defined above if the pawn moved two spaces
    else:
        ep_coords = (100, 100)
    return ep_coords

# Castling rule
# King and Rook can flip flop 2 places
def check_castling(color):
    """FIX 4 + FIX 6: return castling moves for `color`.
 
    Each move is (king_destination, rook_destination, rook_origin).
    Rules: king and rook unmoved, squares between them empty, king not
    currently in check, and the king doesn't pass through or land on an
    attacked square.
    """
    if color == 'white':
        pieces, locations, moved = white_pieces, white_locations, white_moved
        enemy_options = black_options
    else:
        pieces, locations, moved = black_pieces, black_locations, black_moved
        enemy_options = white_options
 
    if 'king' not in pieces:
        return []
    king_index = pieces.index('king')
    king_pos = locations[king_index]
    if moved[king_index]:
        return []
 
    # Flatten the enemy's move lists into one set of attacked squares
    attacked = {square for moves in enemy_options for square in moves}
    if king_pos in attacked:  # FIX 6: can't castle out of check
        return []
 
    occupied = set(white_locations) | set(black_locations)
    castle_moves = []
    for i in range(len(pieces)):
        if pieces[i] != 'rook' or moved[i] or locations[i][1] != king_pos[1]:
            continue
        rook_pos = locations[i]
        step = 1 if rook_pos[0] > king_pos[0] else -1
        between = [(x, king_pos[1]) for x in range(king_pos[0] + step, rook_pos[0], step)]
        king_path = [(king_pos[0] + step, king_pos[1]), (king_pos[0] + 2 * step, king_pos[1])]
        if any(sq in occupied for sq in between):
            continue
        if any(sq in attacked for sq in king_path):
            continue
        castle_moves.append((king_path[1], king_path[0], rook_pos))
    return castle_moves



def draw_castling(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70), 8)
        screen.blit(font_small.render('king', True, 'black'), (moves[i][0][0] * 100 + 30, moves[i][0][1] * 100 + 70))
        pygame.draw.circle(screen, color, (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 8)
        screen.blit(font_small.render('rook', True, 'black'),
                    (moves[i][1][0] * 100 + 30, moves[i][1][1] * 100 + 70))
        pygame.draw.line(screen, color, (moves[i][0][0] * 100 + 50, moves[i][0][1] * 100 + 70),
                         (moves[i][1][0] * 100 + 50, moves[i][1][1] * 100 + 70), 2)


# Add pawn promotion
def check_promotion():
    pawn_indexes = []
    white_promotion = False
    black_promotion = False
    promote_index = 100
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if white_locations[pawn_indexes[i]][1] == 7:
            white_promotion = True
            promote_index = pawn_indexes[i]
    pawn_indexes = []
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        # FIX 1: was pawn_indexes[1]
        if black_locations[pawn_indexes[i]][1] == 0:
            black_promotion = True
            promote_index = pawn_indexes[i]
    return white_promotion, black_promotion, promote_index



# Draw the promotion on the board

def draw_promotion():
    pygame.draw.rect(screen, 'dark gray', [800, 0, 200, 420])
    if white_promote:
        color = 'white'
        for i in range(len(white_promotions)):
            piece = white_promotions[i]
            index = piece_list.index(piece)
            screen.blit(white_images[index], (860, 5 + 100 * i))
    elif black_promote:
        color = 'black'
        for i in range(len(black_promotions)):
            piece = black_promotions[i]
            index = piece_list.index(piece)
            screen.blit(black_images[index], (860, 5 + 100 * i))
    pygame.draw.rect(screen, color, [800, 0, 200, 420], 8)

def check_promo_select():
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x_pos = mouse_pos[0] // 100
    y_pos = mouse_pos[1] // 100
    if white_promote and left_click and x_pos > 7 and y_pos < 4:
        white_pieces[promo_index] = white_promotions[y_pos]
    elif black_promote and left_click and x_pos > 7 and y_pos < 4:
        black_pieces[promo_index] = black_promotions[y_pos]

# ==============================================================================
# ================================= Main =======================================
# ================================= Game =======================================
# ================================= Loop =======================================
# ==============================================================================
white_options = check_options(white_pieces, white_locations, 'white')
black_options = check_options(black_pieces, black_locations, 'black')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if not game_over:
        white_promote, black_promote, promo_index = check_promotion()
        if white_promote or black_promote:
            draw_promotion()
            check_promo_select()

    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
        # FIX 4: compute castling for the side to move, only when a king is selected
        if selected_piece == 'king':
            castling_moves = check_castling('white' if turn_step < 2 else 'black')
            draw_castling(castling_moves)
        else:
            castling_moves = []



    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    selected_piece = white_pieces[selection]
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_ep = check_ep(white_locations[selection], click_coords)
                    white_locations[selection] = click_coords
                    white_moved[selection] = True
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        black_moved.pop(black_piece)
                    # Check if en passant pawn was captured
                    if click_coords == black_ep and selected_piece == 'pawn':
                        black_piece = black_locations.index((black_ep[0], black_ep[1] - 1))
                        captured_pieces_white.append(black_pieces[black_piece])
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                        black_moved.pop(black_piece)


                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            white_locations[selection] = click_coords
                            white_moved[selection] = True
                            # FIX 4: rook origin comes from the castling move itself
                            rook_index = white_locations.index(castling_moves[q][2])
                            white_locations[rook_index] = castling_moves[q][1]
                            white_moved[rook_index] = True
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 2
                            selection = 100
                            valid_moves = []
                            break


            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    selected_piece = black_pieces[selection]
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_ep = check_ep(black_locations[selection], click_coords)
                    black_locations[selection] = click_coords
                    black_moved[selection] = True
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        white_moved.pop(white_piece)
                    # FIX 7: only a pawn can capture en passant
                    if click_coords == white_ep and selected_piece == 'pawn':
                        white_piece = white_locations.index((white_ep[0], white_ep[1] + 1))
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                        white_moved.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            black_locations[selection] = click_coords
                            black_moved[selection] = True
                            rook_index = black_locations.index(castling_moves[q][2])
                            black_locations[rook_index] = castling_moves[q][1]
                            black_moved[rook_index] = True
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 0
                            selection = 100
                            valid_moves = []
                            break


        if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_RETURN:
            game_over = False
            winner = ''
            white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
            white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
            black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
            black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
            # FIX 2: reset state that captures/moves change
            white_moved = [False] * 16
            black_moved = [False] * 16
            white_ep = (100, 100)
            black_ep = (100, 100)
            white_promote = False
            black_promote = False
            promo_index = 100
            castling_moves = []
            selected_piece = ''
            captured_pieces_white = []
            captured_pieces_black = []
            turn_step = 0
            selection = 100
            valid_moves = []
            black_options = check_options(black_pieces, black_locations, 'black')
            white_options = check_options(white_pieces, white_locations, 'white')


    if winner != "":
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()
