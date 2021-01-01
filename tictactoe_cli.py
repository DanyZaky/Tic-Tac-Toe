import random
import sqlite3
from datetime import datetime

class Data_Base():
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.sql = None
    
    def create_database(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.sql = "CREATE TABLE IF NOT EXISTS data (ID INTEGER PRIMARY KEY AUTOINCREMENT, Username VARCHAR(50) NOT NULL, Your_Character VARCHAR(50) NOT NULL, Mode VARCHAR(50) NOT NULL, History VARCHAR(50) NOT NULL, DateTime VARCHAR(50) NOT NULL)"
        self.cursor.execute(self.sql)
    
    def insert_win(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        date_time = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        self.sql = "INSERT INTO data (Username, Your_Character, Mode, History, DateTime) Values ('%s', '%s', '%s', '%s', '%s')"
        
        if character.select_character == "1" and mode.select_mode == "1":
            self.sql = self.sql % (menu.username, character.character[0], mode.mode[0], play.win, date_time)
        elif character.select_character == "1" and mode.select_mode == "2":
            self.sql = self.sql % (menu.username, character.character[0], mode.mode[1], play.win, date_time)
        elif character.select_character == "2" and mode.select_mode == "1":
            self.sql = self.sql % (menu.username, character.character[1], mode.mode[0], play.win, date_time)
        elif character.select_character == "2" and mode.select_mode == "2":
            self.sql = self.sql % (menu.username, character.character[1], mode.mode[1], play.win, date_time)    
        
        self.cursor.execute(self.sql)
        self.connection.commit()
    
    def insert_lose(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        date_time = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        self.sql = "INSERT INTO data (Username, Your_Character, Mode, History, DateTime) Values ('%s', '%s', '%s', '%s', '%s')"
        
        if character.select_character == "1" and mode.select_mode == "1":
            self.sql = self.sql % (menu.username, character.character[0], mode.mode[0], play.lose, date_time)
        elif character.select_character == "1" and mode.select_mode == "2":
            self.sql = self.sql % (menu.username, character.character[0], mode.mode[1], play.lose, date_time)
        elif character.select_character == "2" and mode.select_mode == "1":
            self.sql = self.sql % (menu.username, character.character[1], mode.mode[0], play.lose, date_time)
        elif character.select_character == "2" and mode.select_mode == "2":
            self.sql = self.sql % (menu.username, character.character[1], mode.mode[1], play.lose, date_time)    
        
        self.cursor.execute(self.sql)
        self.connection.commit()

    def insert_tie(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        date_time = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
        self.sql = "INSERT INTO data (Username, Your_Character, Mode, History, DateTime) Values ('%s', '%s', '%s', '%s', '%s')"
        
        if character.select_character == "1" and mode.select_mode == "1":
            self.sql = self.sql % (menu.username, character.character[0], mode.mode[0], play.tie, date_time)
        elif character.select_character == "1" and mode.select_mode == "2":
            self.sql = self.sql % (menu.username, character.character[0], mode.mode[1], play.tie, date_time)
        elif character.select_character == "2" and mode.select_mode == "1":
            self.sql = self.sql % (menu.username, character.character[1], mode.mode[0], play.tie, date_time)
        elif character.select_character == "2" and mode.select_mode == "2":
            self.sql = self.sql % (menu.username, character.character[1], mode.mode[1], play.tie, date_time)    
        
        self.cursor.execute(self.sql)
        self.connection.commit()
    
    def check_history(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.sql = "SELECT * FROM data"
        self.cursor.execute(self.sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

class Main_Menu():
    game_still_going = True
    def __init__(self):
        self.playgame = True
        self.select_chara = True
        self.select_map = True
        self.select_mode = True
        self.exit = True
        self.username = None

    def welcome(self):
        print("----------WELCOME TO TIC-TAC-TOE CLI GAME----------")
        print(" ")
        print("----------I HOPE YOU WILL ENJOY THIS GAME----------")
        print(" ")
    
    def login(self):
        print("Please input your username")
        self.username = input("Username: ")

class Play_Game(Main_Menu):
    def __init__(self):
        self.play = True
        self.x_choice = None
        self.o_choice = None
        self.player_1_win = "Player 1 WIN!!!"
        self.player_2_win = "Player 2 WIN!!!"
        self.ai_win = "AI WIN!!!"
        self.tie = "There is no winner!!!"
        self.win = "You Win"
        self.lose = "You Lose"

    def main(self):
        db.create_database()
        menu.welcome()
        while True:
            select = input("----------Main Menu---------- \n 1. Play Game \n 2. History \n 3. Exit Game \n > ")
            if select == "1":
                menu.login()
                while True:
                    main = input("----------Select Menu---------- \n 1. Select Board \n 2. Select Character \n 3. Select Mode \n 4. Start Game \n > ")
                    while main:
                        if main == "1":
                            board.select_board = input("Choose Your Board \n 1. Board 1 ( ) \n 2. Board 2 ( - ) \n 3. Board 3 ( ? ) \n > ")
                            
                            if board.select_board == "1":
                                print("You Choose")
                                board.display1()
                            elif board.select_board == "2":
                                print("You Choose")
                                board.display2()
                            elif board.select_board == "3":
                                print("You Choose")
                                board.display3()
                                
                            main = input("Select Menu \n 1. Select Board \n 2. Select Character \n 3. Select Mode \n 4. Start Game \n > ")
                        
                        elif main == "2":
                            character.select_character = input("Choose Your Character \n 1. X \n 2. O \n > ")
                            
                            if character.select_character == "1":
                                print("You are X")
                            elif character.select_character == "2":
                                print("You are O")

                            main = input("Select Menu \n 1. Select Board \n 2. Select Character \n 3. Select Mode \n 4. Start Game \n > ")
                        
                        elif main == "3":
                            mode.select_mode = input("Choose Mode \n 1. Vs AI \n 2. Vs Player \n > ")
                            
                            if mode.select_mode == "1":
                                mode.vs_ai()
                            if mode.select_mode == "2":
                                mode.vs_player()

                            main = input("Select Menu \n 1. Select Board \n 2. Select Character \n 3. Select Mode \n 4. Start Game \n > ")
                        
                        elif main == "4":
                            while Main_Menu.game_still_going == True:
                                board.choose_map()

                                character.choose_chara_x() 

                                board.update_map_x()

                                board.choose_map()

                                if board.select_board == "1":
                                    if play.check_winner("X"):
                                        if character.select_character == "1" and mode.select_mode == "1" or mode.select_mode == "2":
                                            print(self.player_1_win)
                                            db.insert_win()
                                        elif character.select_character == "2" and mode.select_mode == "1":
                                            print(self.ai_win)
                                            db.insert_lose()
                                        elif character.select_character == "2" and mode.select_mode == "2":
                                            print(self.player_2_win)
                                            db.insert_lose()    
                                        
                                        a = input("Do you want to play again? Y/N > ")
                                        
                                        if a.lower() == "y":
                                            board.board_reset_1()
                                            board.choose_map()
                                            character.choose_chara_x()   
                                            board.update_map_x()
                                            board.choose_map()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                                    
                                    elif play.check_tie():
                                        print(self.tie)
                                        db.insert_tie()
                                        a = input("Do you want to play again? Y/N > ")
                                        if a.lower() == "y":
                                            board.board_reset_1()
                                            board.choose_map()
                                            character.choose_chara_x()   
                                            board.update_map_x()
                                            board.choose_map()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                                
                                elif board.select_board == "2":
                                    if play.check_winner("X"):
                                        if character.select_character == "1" and mode.select_mode == "1" or mode.select_mode == "2":
                                            print(self.player_1_win)
                                            db.insert_win()
                                        elif character.select_character == "2" and mode.select_mode == "1":
                                            print(self.ai_win)
                                            db.insert_lose()
                                        elif character.select_character == "2" and mode.select_mode == "2":
                                            print(self.player_2_win)
                                            db.insert_lose()
                                        
                                        a = input("Do you want to play again? Y/N > ")
                                        
                                        if a.lower() == "y":
                                            board.board_reset_2()
                                            board.choose_map()
                                            character.choose_chara_x()   
                                            board.update_map_x()
                                            board.choose_map()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                                    
                                    elif play.check_tie():
                                        print(self.tie)
                                        db.insert_lose()
                                        a = input("Do you want to play again? Y/N > ")
                                        if a.lower() == "y":
                                            board.board_reset_2()
                                            board.choose_map()
                                            character.choose_chara_x()   
                                            board.update_map_x()
                                            board.choose_map()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                                
                                elif board.select_board == "3":
                                    if play.check_winner("X"):
                                        if character.select_character == "1" and mode.select_mode == "1" or mode.select_mode == "2":
                                            print(self.player_1_win)
                                            db.insert_win()
                                        elif character.select_character == "2" and mode.select_mode == "1":
                                            print(self.ai_win)
                                            db.insert_lose()
                                        elif character.select_character == "2" and mode.select_mode == "2":
                                            print(self.player_2_win)
                                            db.insert_lose()
                                        
                                        a = input("Do you want to play again? Y/N > ")
                                        
                                        if a.lower() == "y":
                                            board.board_reset_3()
                                            board.choose_map()
                                            character.choose_chara_x()   
                                            board.update_map_x()
                                            board.choose_map()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                                    
                                    elif play.check_tie():
                                        print(self.tie)
                                        db.insert_tie()
                                        a = input("Do you want to play again? Y/N > ")
                                        if a.lower() == "y":
                                            board.board_reset_3()
                                            board.choose_map()
                                            character.choose_chara_x()   
                                            board.update_map_x()
                                            board.choose_map()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False

                                character.choose_chara_o()

                                board.update_map_o()

                                if board.select_board == "1":
                                    if play.check_winner("O"):
                                        board.choose_map()
                                        if character.select_character == "1" and mode.select_mode == "1":
                                            print(self.ai_win)
                                            db.insert_lose()
                                        elif character.select_character == "1" and mode.select_mode == "2":
                                            print(self.player_2_win)
                                            db.insert_lose()
                                        elif character.select_character == "2" and mode.select_mode == "1" or mode.select_mode == "2":
                                            print(self.player_1_win)
                                            db.insert_win()
                                        
                                        a = input("Do you want to play again? Y/N > ")
                                        
                                        if a.lower() == "y":
                                            board.board_reset_1()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                                
                                elif board.select_board == "2":
                                    if play.check_winner("O"):
                                        board.choose_map()
                                        if character.select_character == "1" and mode.select_mode == "1":
                                            print(self.ai_win)
                                            db.insert_lose()
                                        elif character.select_character == "1" and mode.select_mode == "2":
                                            print(self.player_2_win)
                                            db.insert_lose()
                                        elif character.select_character == "2" and mode.select_mode == "1" or mode.select_mode == "2":
                                            print(self.player_1_win)
                                            db.insert_win()
                                        
                                        a = input("Do you want to play again? Y/N > ")
                                        
                                        if a.lower() == "y":
                                            board.board_reset_2()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                                
                                elif board.select_board == "3":
                                    if play.check_winner("O"):
                                        board.choose_map()
                                        if character.select_character == "1" and mode.select_mode == "1":
                                            print(self.ai_win)
                                            db.insert_lose()
                                        elif character.select_character == "1" and mode.select_mode == "2":
                                            print(self.player_2_win)
                                            db.insert_lose()
                                        elif character.select_character == "2" and mode.select_mode == "1" or mode.select_mode == "2":
                                            print(self.player_1_win)
                                            db.insert_win()
                                        
                                        a = input("Do you want to play again? Y/N > ")
                                        
                                        if a.lower() == "y":
                                            board.board_reset_3()
                                        else:
                                            print("Game Over")
                                            ext.exit_game()
                                            return False
                        else:
                            print("Wrong Move")
                            main = input("Select Menu \n 1. Select Board \n 2. Select Character \n 3. Select Mode \n 4. Start Game \n > ")
                return False

            elif select == "2":
                print(" ")
                print("----------History----------")
                db.check_history()    
                print(" ")
                        
            else:
                ext.exit_game()
                return False
        
        return False

    def check_winner(self, player):
        for i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            result = True
            for number in i:
                if board.board1[number] != player and board.board2[number] != player and board.board3[number] != player:
                    result = False
            if result == True:
                return True
        return False
    
    def check_tie(self):
        if " " not in board.board1 or "-" not in board.board2 or "?" not in board.board3:
            return True
        else:
            return False

# Pilihan Map
class Board(Main_Menu):
    def __init__(self):
        self.board1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.board2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.board3 = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]
        self.select_board = "1"
    
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
        if self.select_board == "1":
            board.display1()
        elif self.select_board == "2":
            board.display2()
        elif self.select_board == "3":
            board.display3()
    
    def update_map_x(self):
        if self.select_board == "1":
            board.update1(play.x_choice, "X")
        elif self.select_board == "2":
            board.update2(play.x_choice, "X")
        elif self.select_board == "3":
            board.update3(play.x_choice, "X")
    
    def update_map_o(self):
        if self.select_board == "1":
            board.update1(play.o_choice, "O")
        elif self.select_board == "2":
            board.update2(play.o_choice, "O")
        elif self.select_board == "3":
            board.update3(play.o_choice, "O")

# Pilihan Character
class Character(Main_Menu):
    def __init__(self):
        self.character = ["X", "O"]
        self.select_character = "1"
    
    def choose_chara_x(self):
        if self.select_character == "1" and mode.select_mode == "1" or mode.select_mode == "2":
            play.x_choice = int(input("Player 1 as X) Choose 1-9 > "))
            while " " not in board.board1[play.x_choice-1] or "-" not in board.board2[play.x_choice-1] or "?" not in board.board3[play.x_choice-1]:
                print("Wrong Step")
                play.x_choice = int(input("Player 1 as X) Choose 1-9 > "))
        elif self.select_character == "2" and mode.select_mode == "1":
            print("AI as X) Choose 1-9 > ")
            play.x_choice = random.randint(1,9)
            while " " not in board.board1[play.x_choice-1] or "-" not in board.board2[play.x_choice-1] or "?" not in board.board3[play.x_choice-1]:
                print("Wrong Step")
                print("AI as X) Choose 1-9 > ")
                play.x_choice = random.randint(1,9)
        elif self.select_character == "2" and mode.select_mode == "2":
            play.x_choice = int(input("Player 2 as X) Choose 1-9 > "))
            while " " not in board.board1[play.x_choice-1] or "-" not in board.board2[play.x_choice-1] or "?" not in board.board3[play.x_choice-1]:
                print("Wrong Step")
                play.x_choice = int(input("Player 2 as X) Choose 1-9 > "))
    
    def choose_chara_o(self):
        if self.select_character == "1" and mode.select_mode == "1":
            print("AI as O) Choose 1-9 > ")
            play.o_choice = random.randint(1,9)
            while " " not in board.board1[play.o_choice-1] or "-" not in board.board2[play.o_choice-1] or "?" not in board.board3[play.o_choice-1]:
                print("Wrong Step")
                print("AI as O) Choose 1-9 > ")
                play.o_choice = random.randint(1,9)
        elif self.select_character == "1" and mode.select_mode == "2":
            play.o_choice = int(input("Player 2 as O) Choose 1-9 > "))
            while " " not in board.board1[play.o_choice-1] or "-" not in board.board2[play.o_choice-1] or "?" not in board.board3[play.o_choice-1]:
                print("Wrong Step")
                play.o_choice = int(input("Player 2 as O) Choose 1-9 > "))
        elif self.select_character == "2" and mode.select_mode == "1" or mode.select_mode == "2":
            play.o_choice = int(input("Player 1 as O) Choose 1-9 > "))
            while " " not in board.board1[play.o_choice-1] or "-" not in board.board2[play.o_choice-1] or "?" not in board.board3[play.o_choice-1]:
                print("Wrong Step")
                play.o_choice = int(input("Player 1 as O) Choose 1-9 > "))

# Memilih mode: vs ai dan vs player
class Mode(Main_Menu):
    def __init__(self):
        self.mode = ["Vs AI", "Vs Player"]
        self.select_mode = "1"
    
    def vs_ai(self):
        print("You Choose Vs AI Mode")
    
    def vs_player(self):
        print("You Choose Vs Player Mode")

# Keluar dari game
class Exit_Game(Main_Menu):
    def exit_game(self):
        print("----------THANK YOU FOR PLAYING THIS GAME----------")

db = Data_Base()
menu = Main_Menu()
play = Play_Game()
board = Board()
character = Character()
mode = Mode()
ext = Exit_Game()

if __name__ == "__main__":
    play.main()
    