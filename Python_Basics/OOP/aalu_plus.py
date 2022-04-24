""" A PROJECT ON PYTHON BY DARSHAN GAUTAM ,AMAN ANSARI,GOPAL K.C."""
import os
import random
import logging

logging.basicConfig(filename='TicTAC.log',
                    format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)


class GameBody():
    """THIS IS THE MAIN BODY OF THE GAME!!!"""

    def __init__(self, board):
        self.board = board
        # self.marker = marker
        # self.position = position

    def display_board(self, board):
        """ TO DISPLAY THE BOARD!!! """
        os.system("clear")
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def player_input(self):
        """ OUTPUT = (Player1_marker,Player2_marker) """
        marker = ' '
        while marker != 'X' and marker != 'O':
            marker = input(' Choose X or O: ').upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    def place_marker(self, board, marker, position):

        board[position] = marker

    def win_check(self, board, mark):
        """TO CHECK WHO HAS WON THE GAME!!!"""

        return ((board[1] == board[2] == board[3] == mark) or
                (board[4] == board[5] == board[6] == mark) or
                (board[7] == board[8] == board[9] == mark) or

                (board[1] == board[4] == board[7] == mark) or
                (board[2] == board[5] == board[8] == mark) or
                (board[3] == board[6] == board[9] == mark) or

                (board[1] == board[5] == board[9] == mark) or
                (board[7] == board[5] == board[3] == mark))

    def choose_first(self):
        """FOR WHOSE TURN IS FIRST"""
        flip = random.randint(0, 1)

        if flip == 0:
            return Player_1
        else:
            return Player_2

    def space_check(self, board, position):
        return self.board[position] == ' '

    def full_board_check(self, board):

        for i in range(1, 10):
            if self.space_check(board, i):
                return False
        # BOARD IS FULL IF WE RETURN TRUE
        return True

    def player_choice(self, board):

        position = 0
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.space_check(board, position):
            position = int(input('Choose a position: (1-9) : '))

        return position

    def replay(self):
        choice = input("Play again? Enter Yes or No :")
        return choice == 'Yes'


if __name__ == '__main__':
    print("Welcome to Tic TAC TOE")
    Player_1 = input("Enter Player 1 name : ")
    Player_2 = input("Enter player 2 name : ")
    logging.debug(f"Player 1: {Player_1}")
    logging.debug(f"Player 2: {Player_2}")

    while True:
        the_board = [" "] * 10
        c1 = GameBody(the_board)
        player1_marker, player2_marker = c1.player_input()
        turn = c1.choose_first()
        print(turn + ' will go first')

        play_game = input('Are you ready to play? \n Enter y/n :')
        if play_game == 'y':
            game_on = True
        else:
            game_on = False

        # GAME PLAY
        while game_on:
            if turn == Player_1:
                # Show the board
                c1.display_board(the_board)
                # Choose the position
                position = c1.player_choice(the_board)
                # Place the marker on the position
                c1.place_marker(the_board, player1_marker, position)
                # Check if they won
                if c1.win_check(the_board, player1_marker):
                    c1.display_board(the_board)
                    print(f'{Player_1} HAS WON!!!')
                    logging.debug(f'{Player_1} HAS WON!!!')
                    game_on = False
                # Or check if there is tie
                else:
                    if c1.full_board_check(the_board):
                        c1.display_board(the_board)
                        print("TIE GAME!")
                        logging.debug("TIE GAME!")
                        game_on = False
                    else:
                        turn = Player_2

                # No tie and no win? Then next player's turn
            else:
                # Show the board
                c1.display_board(the_board)
                # Choose the position
                position = c1.player_choice(the_board)
                # Place the marker on the position
                c1.place_marker(the_board, player2_marker, position)
                # Check if they won
                if c1.win_check(the_board, player2_marker):
                    c1.display_board(the_board)
                    print(f'{Player_2} HAS WON!!!')
                    logging.debug(f'{Player_2} HAS WON!!!')
                    game_on = False
                # Or check if there is tie
                else:
                    if c1.full_board_check(the_board):
                        c1.display_board(the_board)
                        print("TIE GAME!")
                        logging.debug("TIE GAME!")
                        game_on = False
                    else:
                        turn = Player_1

        if not c1.replay():
            break