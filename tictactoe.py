#!usr/bin/python3

import random 

class TicTacToe: 

    def __init__(self): 

        self.board = []
        self.players = ["player1", "player2"]
        for i in range(9): 
            self.board.append([i+1]) 


    def instructions(self): 

        print("""
                Tic Tac Toe Game 

                  Player 1 : O 
                  Player 2 : X 

    At first, one player is chosen at random to 
    go first. Player who places three in a row 
    (row, column, diagonal) first wins the game. 

                   Have Fun!

            """)
        self.choose_move()


    def display_board(self): 

        """
        function that prints out the board 
        """

        print("\t\t ", self.board[0], self.board[1], self.board[2])          #print the board 3 x 3
        print("\t\t ", self.board[3], self.board[4], self.board[5])
        print("\t\t ", self.board[6], self.board[7], self.board[8],"\n")


    def place_marker(self, player):

        """function to place O or X on to the display_board under the right conditions"""

        if player == "player1": 
            try: 
                pos = int(input("Player 1 move(O): ")) -1
                self.space_check(player, pos)
            except ValueError:                                      #if player inputs a value other than a number
                print("please enter a number between 1-9")
                self.place_marker(player)
            except IndexError: 
                print("please enter a number between 1-9")
                self.place_marker(player)
        elif player == "player2": 
            try: 
                pos = int(input("Player 2 move(X): ")) -1
                self.space_check(player, pos)
            except ValueError: 
                print("please enter a number between 1-9")
                self.place_marker(player)
            except IndexError: 
                print("please enter a number between 1-9")
                self.place_marker(player)
        self.display_board()


    def space_check(self, player, pos): 

        """check if it is valid place for player move. if valid, show board and check if won."""

        if str(self.board[pos]).strip().isalpha():                  #if a marker is already there
            print("You cannot mark there.")
            self.place_marker(player)
        else: 
            if player == "player1": 
                self.board[pos] = " O "
            elif player == "player2":
                self.board[pos] = " X "
            print()

        self.display_board()
        self.win_check(player)


    def win_check(self, player): 

        """
        checks for winner. if no winner, check for full board."""
        
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
            self.full_check(player, self.board)


    def full_check(self, player, board): 

        """check if the board is full. if not, continue"""

        for p in board: 
            if isinstance(p, list): 
                if player == "player1":
                    self.place_marker("player2")
                elif player == "player2":
                    self.place_marker("player1")
        else:
            self.replay()


    def replay(self): 

        """asks player if he or she wants to play again."""

        print("""
          Do you wish to play again? (Y/N)
            """)
        ans = input(">>> ")
        if ans.lower() == "y":                                          #accept both upper and lower inputs
            self.__init__()
            self.choose_move()
        elif ans.lower() == "n": 
            quit()


    def choose_move(self): 

        """using random module, choose who goes first"""

        first_move = random.choice(self.players)
        self.display_board()
        self.place_marker(first_move)


if __name__ == "__main__":
    game = TicTacToe()
    game.instructions()