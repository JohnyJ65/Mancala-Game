
# Starting pocket amounts and players
board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
player = "A"

# Print the game board
def print_board():
    print("\t13\t12\t11\t10\t9\t8")
    print("----------------------------------------------------------")
    print("B:\t" + str(board[13]) + "\t" + str(board[12]) + "\t" + str(board[11]) +
          "\t" + str(board[10]) + "\t" + str(board[9]) + "\t" + str(board[8]))
    print("   " + str(board[0]) + "\t\t\t\t\t\t\t" + str(board[7]))
    print("A:\t" + str(board[1]) + "\t" + str(board[2]) + "\t" + str(board[3]) +
          "\t" + str(board[4]) + "\t" + str(board[5]) + "\t" + str(board[6]))
    print("----------------------------------------------------------")
    print("\t1\t2\t3\t4\t5\t6\n")

# Determine if the move is allowed for the specific player
def is_valid_move(pocket):
    if player == "A":
        return pocket >= 1 and pocket <= 6 and board[pocket] > 0
    else:
        return pocket >= 8 and pocket <= 13 and board[pocket] > 0

# Move the stones, adding one to each pocket and reseting the original
def move_stones(pocket):
    global player

    stones = board[pocket]
    board[pocket] = 0
    index = pocket

    while stones > 0:
        index = (index + 1) % 14

        if player == "A" and index == 7:
            continue
        if player == "B" and index == 0:
            continue

        board[index] += 1
        stones -= 1

    
    if player == "A" and index >= 1 and index <= 6 and board[index] == 1:
        opposite = 14 - index
        board[0] += board[opposite] + 1
        board[index] = 0
        board[opposite] = 0

    if player == "B" and index >= 8 and index <= 13 and board[index] == 1:
        opposite = 14 - index
        board[7] += board[opposite] + 1
        board[index] = 0
        board[opposite] = 0

    print_board()

    # Extra turn if landing in that players own store
    if (player == "A" and index == 0) or (player == "B" and index == 7):
        print("Go again!\n")
        return

    # Switch player
    if player == "A":
        player = "B"
    else:
        player = "A"

#Get input and save it if valid.
def take_turn():
    global player

    print("Player " + player + "'s Turn!")



    pocket = int(input("Choose a pocket: "))

   
    if is_valid_move(pocket):
        move_stones(pocket)
    

# If the stores are empty, set a bool to true
def game_over():
    empty_A = True
    empty_B = True

    i = 1
    while i <= 6:
        if board[i] != 0:
            empty_A = False
        i += 1

    j = 8
    while j <= 13:
        if board[j] != 0:
            empty_B = False
        j += 1

    return empty_A or empty_B

# Add the stones to the resepctive store, then determine which one is higher.
def calculate_winner():
    i = 1
    while i <= 6:
        board[0] += board[i]
        board[i] = 0
        i += 1

    j = 8
    while j <= 13:
        board[7] += board[j]
        board[j] = 0
        j += 1

    print_board()

    if board[0] > board[7]:
        print("Player A wins!")
    elif board[7] > board[0]:
        print("Player B wins!")
    else:
        print("It's a tie!")

# Main Program

print_board()

#Game loop
while game_over() == False:
    take_turn()

calculate_winner()
