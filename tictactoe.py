#!usr/bin/python3

"""
Tic Tac Toe

PROGRAM NAME: tictactoe.py
VERSION: N/A
CREATOR: dukalee 
DATE: February 15, 2018
======================

A simple tic tac toe game for two players. 

instead of a 
  |  | 
--------
  |  | 
--------
  |  | 

like board,  this program displays the board in such fashion: 

[1] [2] [3] 
[4] [5] [6] 
[7] [8] [9] 

How to Play
======================

when the game starts, it is randomly chosen whether player1 or player2 goes first. 
if it is your turn, input the number of the position where you wish to place your mark. 
if a player wins or if there is a draw, it will prompt for a replay. 
"""

import random 

class TicTacToe: 

    def __init__(self): 

        self.board = []
        self.players = ["player1", "player2"]
        for i in range(9): 
            self.board.append([i+1]) 


    def display_board(self): 

        """
        function that prints out the board 
        """

        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])


    def place_marker(self, player):

        """
        function to place O or X on to the display_board
        """

        if player == "player1": 
            try: 
                pos = int(input("Player 1 move(O): ")) -1
                self.space_check(player, pos)
            except ValueError: 
                print("please enter a number between 1-9")
                self.place_marker(player)
        elif player == "player2": 
            try: 
                pos = int(input("Player 2 move(X): ")) -1
                self.space_check(player, pos)
            except ValueError: 
                print("please enter a number between 1-9")
                self.place_marker(player)

        self.display_board()


    def space_check(self, player, pos): 

        """
        check if it is valid place for player move. if valid, show board and check if won.
        """

        if str(self.board[pos]).strip().isalpha(): 
            print("You cannot mark there.")
            self.place_marker(player)

        else: 
            if player == "player1": 
                self.board[pos] = " O "
            elif player == "player2":
                self.board[pos] = " X "

        self.display_board()
        self.win_check(player)


    def win_check(self, player): 

        """
        checks for winner. if no winner, check for full board.
        """
        
        if (self.board[0] == self.board[1] == self.board[2] or
            self.board[3] == self.board[4] == self.board[5] or
            self.board[6] == self.board[7] == self.board[8] or 
            self.board[0] == self.board[3] == self.board[6] or
            self.board[1] == self.board[4] == self.board[7] or
            self.board[2] == self.board[5] == self.board[8] or
            self.board[0] == self.board[4] == self.board[8] or 
            self.board[2] == self.board[4] == self.board[6]):

            print(player + " win!")
            self.replay()

        else: 
            self.full_board_check(player, self.board)


    def full_board_check(self, player, board): 

        """
        checks if board is full. if not, continue
        """

        for p in board: 
            if isinstance(p, list): 
                if player == "player1":
                    self.place_marker("player2")
                elif player == "player2":
                    self.place_marker("player1")
        else:
            self.replay()


    def replay(self): 

        """
        asks player if he or she wants to play again.
        """

        print("Do you wish to play again?")
        ans = input(">>> ")
        if ans.lower() == "y": 
            self.__init__()
            self.choose_move()
        elif ans.lower() == "n": 
            quit()


    def choose_move(self): 

        """
        using random module, choose who goes first
        """

        first_move = random.choice(self.players)
        self.display_board()
        self.place_marker(first_move)


if __name__ == "__main__":
    game = TicTacToe()
    game.choose_move()