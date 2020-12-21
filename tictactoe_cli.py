import random

class Play_Game():
    def __init__(self):
        self.play = True

    def main(self):
        pass

    def check_winner_1(self, player):
        for i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for number in i:
                if board.board1[number] != player:
                    result = False
            if result == True:
                return True
        return False
    
    def check_winner_2(self, player):
        for i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for number in i:
                if board.board2[number] != player:
                    result = False
            if result == True:
                return True
        return False
    
    def check_winner_3(self, player):
        for i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for number in i:
                if board.board3[number] != player:
                    result = False
            if result == True:
                return True
        return False
    
    def check_tie_1(self):
        if " " not in board.board1:
            return True
        else:
            return False
    
    def check_tie_2(self):
        if "-" not in board.board2:
            return True
        else:
            return False
    
    def check_tie_3(self):
        if "?" not in board.board3:
            return True
        else:
            return False

# Pilihan Map
class Board():
    game_still_going = True

    def __init__(self):
        self.board1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.board2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.board3 = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]
    
    def display1(self):
        print(" ")
        print("| {} | {} | {} |         | 1 | 2 | 3 |".format(self.board1[0], self.board1[1], self.board1[2]))
        print("| {} | {} | {} |         | 4 | 5 | 6 |".format(self.board1[3], self.board1[4], self.board1[5]))
        print("| {} | {} | {} |         | 7 | 8 | 9 |".format(self.board1[6], self.board1[7], self.board1[8]))
        print(" ")
    
    def display2(self):
        print(" ")
        print("| {} | {} | {} |         | 1 | 2 | 3 |".format(self.board2[0], self.board2[1], self.board2[2]))
        print("| {} | {} | {} |         | 4 | 5 | 6 |".format(self.board2[3], self.board2[4], self.board2[5]))
        print("| {} | {} | {} |         | 7 | 8 | 9 |".format(self.board2[6], self.board2[7], self.board2[8]))
        print(" ")
    
    def display3(self):
        print(" ")
        print("| {} | {} | {} |         | 1 | 2 | 3 |".format(self.board3[0], self.board3[1], self.board3[2]))
        print("| {} | {} | {} |         | 4 | 5 | 6 |".format(self.board3[3], self.board3[4], self.board3[5]))
        print("| {} | {} | {} |         | 7 | 8 | 9 |".format(self.board3[6], self.board3[7], self.board3[8]))
        print(" ")
    
    def board_reset_1(self):
        self.board1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def board_reset_2(self):
        self.board2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    
    def board_reset_3(self):
        self.board3 = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]
    
    def update1(self, number, player):
        if self.board1[number-1] == " ":
            self.board1[number-1] = player

    def update2(self, number, player):
        if self.board2[number-1] == "-":
            self.board2[number-1] = player
    
    def update3(self, number, player):
        if self.board3[number-1] == "?":
            self.board3[number-1] = player
    
    def choose_map(self):
        if p == "1":
            board.display1()
        elif p == "2":
            board.display2()
        elif p == "3":
            board.display3()
    
    def update_map_x(self):
        if p == "1":
            board.update1(x_choice, "X")
        elif p == "2":
            board.update2(x_choice, "X")
        elif p == "3":
            board.update3(x_choice, "X")
    
    def update_map_o(self):
        if p == "1":
            board.update1(o_choice, "O")
        elif p == "2":
            board.update2(o_choice, "O")
        elif p == "3":
            board.update3(o_choice, "O")

# Pilihan Character
class Character():
    def __init__(self):
        self.character = ["X", "O"]
    
    def select_character1(self):
        print("Player 1 as",self.character[0])
        print("AI as",self.character[1])
    
    def select_character2(self):
        print("Player 1 as",self.character[1])
        print("AI as",self.character[0])
    
    def select_character3(self):
        print("Player 1 as",self.character[0])
        print("Player 2 as",self.character[1])
    
    def select_character4(self):
        print("Player 1 as",self.character[1])
        print("Player 2 as",self.character[0])

# Memilih mode: vs ai dan vs player
class Mode():
    def __init__(self):
        self.mode = ["Vs AI", "Vs Player"]
    
    def ai(self):
        print(self.mode[0])
    
    def player(self):
        print(self.mode[1])

# Keluar dari game
class Exit_Game():
    def exit(self):
        print("Exit Game")

play = Play_Game()
board = Board()
character = Character()
mode = Mode()
ext = Exit_Game()

p = input("Choose one: \n 1. Board 1 ( ) \n 2. Board 2 ( - ) \n 3. Board 3 ( ? ) \n > ")

while True:
    board.choose_map()

    x_choice = int(input("X) Choose 1-9 > "))
    while " " not in board.board1[x_choice-1] or "-" not in board.board2[x_choice-1] or "?" not in board.board3[x_choice-1]:
        print("Wrong Step")
        x_choice = int(input("X) Choose 1-9 > "))

    board.update_map_x()

    board.choose_map()

    if p == "1":
        if play.check_winner_1("X"):
            print("X WIN!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_1()
                continue
            else:
                print("Game Over")
                break
        elif play.check_tie_1():
            print("There is no winner!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_1()
                continue
            else:
                print("Game Over")
                break
    elif p == "2":
        if play.check_winner_2("X"):
            print("X WIN!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_2()
                continue
            else:
                print("Game Over")
                break
        elif play.check_tie_2():
            print("There is no winner!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_1()
                continue
            else:
                print("Game Over")
                break
    elif p == "3":
        if play.check_winner_3("X"):
            print("X WIN!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_3()
                continue
            else:
                print("Game Over")
                break
        elif play.check_tie_3():
            print("There is no winner!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_1()
                continue
            else:
                print("Game Over")
                break

    o_choice = int(input("O) Choose 1-9 > "))
    while " " not in board.board1[o_choice-1] or "-" not in board.board2[o_choice-1] or "?" not in board.board3[o_choice-1]:
        print("Wrong Step")
        o_choice = int(input("o) Choose 1-9 > "))

    board.update_map_o()

    if p == "1":
        if play.check_winner_1("O"):
            board.choose_map()
            print("O WIN!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_1()
                continue
            else:
                print("Game Over")
                break
    elif p == "2":
        if play.check_winner_2("O"):
            board.choose_map()
            print("O WIN!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_2()
                continue
            else:
                print("Game Over")
                break
    elif p == "3":
        if play.check_winner_3("O"):
            board.choose_map()
            print("O WIN!!!")
            a = input("Do you want to play again? Y/N > ")
            if a.lower() == "y":
                board.board_reset_3()
                continue
            else:
                print("Game Over")
                break
