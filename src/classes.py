from os import name, system
from random import choice, randint
from time import sleep
from simple_term_menu import TerminalMenu

# Player Class for inidividual human players

class Player():
    def __init__(self, name = "undefined", health = 200, body_type = "undefined", weapon = "undefined"):
        self.__name = name
        self.__health = health
        self.__body_type = body_type
        self.__weapon = weapon


    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_body_type(self):
        return self.__body_type

    def get_weapon(self):
        return self.__weapon    

    def set_name(self, name):
        self.__name = name

    def set_body_type(self, body_type):
        self.__body_type = body_type

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def damage(self, health):
        self.__health -= health

# Child Class of the Player Class for AI specifics

class ComputerPlayer(Player):

    # Random names for AI player
    bot_names = ["Terminator", "Annihilator", "Destroyer", "Crusher", "Nuts-n-Bolts", "Link",
    "Mechanicus", "Ripper", "Tank", "Shredder"]

    # Random Body type for AI player
    bot_body_type = ["Tracked", "Soft-Wheeled", "Hard-Wheeled"]

    # Random Arm weapon for AI player
    bot_weapon = ["Electrocutor", "Powersaw", "Flipper"]

    def __init__(self):
        self.__name = choice(ComputerPlayer.bot_names)
        self.__body_type = choice(ComputerPlayer.bot_body_type)
        self.__weapon = choice(ComputerPlayer.bot_weapon)
        self.__health = 200
        # Had to declare all parameters as body type and weapon were positional
        super().__init__(self.__name, self.__health, self.__body_type, self.__weapon)





class Game():
    # Initilizes a main player and second player (either human or computer)
    def __init__(self):
        self.player_one = ""
        self.player_two = ""
        self.attack_first_flag = False
        self.arena_effects_flag = False
        self.game_exit_flag = False
        # Dmg calculator sets of tuples for calculating damage
        self.strong_against_weapon = {
            ("Electrocutor", "Flipper"),
            ("Powersaw", "Electrocutor"),
            ("Flipper", "Powersaw")
        }
        self.weak_against_weapon = {
            ("Electrocutor", "Electrocutor"),
            ("Powersaw", "Powersaw"),
            ("Flipper", "Flipper")
        }

        self.strong_against_body = {
            ("Electrocutor", "Tracked"),
            ("Powersaw", "Soft-Wheeled"),
            ("Flipper", "Hard-Wheeled")
        }
        self.weak_against_body = {
            ("Electrocutor", "Soft-Wheeled"),
            ("Powersaw", "Hard-Wheeled"),
            ("Flipper", "Tracked")
        }

    # DO TIME PERMITTING
    def introduction(self):
        ### Add cool ASCII Picture
        ### Add ... initializing Battle Bots ... print message
        ### Add timer pause before menu opens
        pass

    # Method that clears the terminal throughout the game so players don't have to scroll
    def clear_terminal(self):
        system("cls" if name == "nt" else "clear")

    def game_mode(self):
        self.clear_terminal()
        options = ["Single Player", "Multi Player", "Exit Game"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        while menu_entry_index != 2:
            try:
                print(f"You have selected {options[menu_entry_index]}!\n")
                sleep(1)
                self.clear_terminal()
                if menu_entry_index == 0:
                    self.single_player()
                    self.game_exit_flag = False
                elif menu_entry_index == 1:
                    self.multi_player()
                    self.game_exit_flag = False
                self.clear_terminal()
                menu_entry_index = terminal_menu.show()
            except TypeError:
                print ("Please select an option")
                menu_entry_index = terminal_menu.show()
                continue
        print(f"You have selected {options[menu_entry_index]}!\n")

    # ERORR HANDLE (if escape pushed) TypeError: list indices must be integers or slices, not NoneType
    def single_player(self):
        # ERORR HANDLE INPUT HERE FOR INTS/FLOAT EMPTIES NONE TYPE ETC
        self.player_one = Player()
        player_one_name = input("What's you're Battle Robots Name ? ")
        self.player_one.set_name(player_one_name.capitalize())
        print(f"\n Welcome, {self.player_one.get_name()}")
        self.player_two = ComputerPlayer()
        print(f"\n You're Battling: {self.player_two.get_name()}!\n")
        print("...initializing...")
        sleep(4)
        self.clear_terminal()
        self.arena_effects()
        self.body_type_menu(self.player_one, self.player_two)

    def multi_player(self):
        # ERROR HANDLE IF BOTH PLAYERS HAVE SAME NAME
        self.player_one = Player()
        player_one_name = input("Player One: What's you're Battle Robots Name ? ")
        self.player_one.set_name(player_one_name.capitalize())
        self.clear_terminal()
        self.player_two = Player()
        player_two_name = input("Player Two: What's you're Battle Robots Name ? ")
        self.player_two.set_name(player_two_name.capitalize())
        self.clear_terminal()
        self.arena_effects()
        self.body_type_menu(self.player_one, self.player_two)        

    def body_type_menu(self, player_one, player_two):
        players = [player_one, player_two]
        exit_flag = False
        for char in players:
            if isinstance(char, ComputerPlayer):
                self.weapon_menu(player_one, player_two)
            else:
                print(f"{char.get_name()}: What Body-Type do you want ? \n")
                body_type_options = ["Tracked", "Soft-Wheeled", "Hard-Wheeled", "Main Menu"]
                terminal_menu = TerminalMenu(body_type_options)
                menu_entry_index = terminal_menu.show()
                while menu_entry_index != 3:
                    try:
                        print(f"You have selected {body_type_options[menu_entry_index]}!\n")
                        if menu_entry_index == 0:
                            char.set_body_type("Tracked")
                        elif menu_entry_index == 1:
                            char.set_body_type("Soft-Wheeled")
                        elif menu_entry_index == 2:
                            char.set_body_type("Hard-Wheeled")
                        sleep(2)
                        self.clear_terminal()
                        break
                    except TypeError:
                        print ("Please select an option")
                        menu_entry_index = terminal_menu.show()
                        continue
                if menu_entry_index == 3:
                    exit_flag = True
                    self.clear_terminal()
                    print(f"You have selected {body_type_options[menu_entry_index]}!\n")
                    sleep(1)
            if self.game_exit_flag:
                break
            if exit_flag:
                self.clear_terminal()
                break
        if exit_flag is False and self.game_exit_flag is not True:
            self.weapon_menu(player_one, player_two)
            # else:
            #         print(f"{self.player_two.get_name()}: Select what Body Type you want:\n")
            #     break




    def weapon_menu(self, player_one, player_two):
        players = [player_one, player_two]
        exit_flag = False
        for char in players:
            if isinstance(char, ComputerPlayer):
                self.bot_select()
            else:
                print(f"{char.get_name()}: What Weapon do you want to punish your opponent with!\n")
                weapon_options = ["Electrocutor", "Powersaw", "Flipper", "Main Menu"]
                terminal_menu = TerminalMenu(weapon_options)
                menu_entry_index = terminal_menu.show()
                while menu_entry_index != 3:
                    try:
                        print(f"You have selected {weapon_options[menu_entry_index]}!\n")
                        if menu_entry_index == 0:
                            char.set_weapon("Electrocutor")                       
                        elif menu_entry_index == 1:
                            char.set_weapon("Powersaw")
                        elif menu_entry_index == 2:
                            char.set_weapon("Flipper")
                        sleep(2)
                        self.clear_terminal()
                        break
                    except TypeError:
                        print ("Please select an option")
                        menu_entry_index = terminal_menu.show()
                        continue   
                if menu_entry_index == 3:
                    exit_flag = True
                    self.clear_terminal()
                    print(f"You have selected {weapon_options[menu_entry_index]}!\n")
                    sleep(1)
            if exit_flag:
                self.clear_terminal()
                self.game_exit_flag = True
                break
        if exit_flag is False:
            self.battle_load_screen()
            
        # print(f"You have selected {weapon_options[menu_entry_index]}!\n")

    def bot_select(self):
            print(f"{self.player_two.get_name()} is thinking....\n")
            sleep(2)
            print(f"{self.player_two.get_name()} has selected Body Type: {self.player_two.get_body_type()}\n")
            print(f"{self.player_two.get_name()} has selected Weapon: {self.player_two.get_weapon()}\n")
            print("...initializing...")
            sleep(4)
            self.clear_terminal()
    
    def battle_load_screen(self):
        print(f"Player One: {self.player_one.get_name()}, Health: {self.player_one.get_health()}, Weapon: {self.player_one.get_weapon()}, Body-Type: {self.player_one.get_body_type()}\n")
        print("VERSUS!\n")
        print(f"Player Two: {self.player_two.get_name()}, Health: {self.player_two.get_health()}, Weapon: {self.player_two.get_weapon()}, Body-Type: {self.player_two.get_body_type()}\n")
        print("...initializing...\n")
        sleep(4)
        self.clear_terminal()
        print("Roll for who attacks first!\n")
        player_one_roll = 0
        player_two_roll = 0
        while player_one_roll == player_two_roll:
            player_one_roll = randint(1, 6)
            print(f"{self.player_one.get_name()} rolls: {player_one_roll}\n")
            player_two_roll = randint(1, 6)
            print(f"{self.player_two.get_name()} rolls: {player_two_roll}\n")
            if player_one_roll == player_two_roll:
                print("Same number, roll again!\n")
                continue
            elif player_one_roll > player_two_roll:
                print(f"{self.player_one.get_name()} attacks first!\n")
                break
            elif player_two_roll > player_one_roll:
                print(f"{self.player_two.get_name()} attacks first!\n")
                self.attack_first_flag = True
                break
        print("...initializing...\n")
        sleep(5)
        self.clear_terminal()        
        # Flag variable called in game object that determines who goes first based on roll above
        # Battle method called in here
        if self.attack_first_flag:
            self.battle(self.player_two, self.player_one)
        elif self.attack_first_flag is False:
            self.battle(self.player_one, self.player_two)
        # self.player_two

    # Calculate damage for weapon attacking weapon
    def weap_weap_dmg(self, first, second):
        if (first, second) in self.strong_against_weapon:
            return 30
        elif (first, second) in self.weak_against_weapon:
            return 10
        else:
            return 20
    # Calculate damage for weapon attacking body
    def weap_body_dmg(self, first, second):
        if (first, second) in self.strong_against_body:
            return 30
        elif (first, second) in self.weak_against_body:
            return 10
        else:
            return 20

    def battle(self, first, second):
        # Declared menu variable here to prevent assignment errors later (required two menus one for bot and one for players)
        menu_entry_index = True
        bot_entry_index = True
        while self.player_one.get_health() > 0 and self.player_two.get_health() > 0:
            print(f"Player One: {self.player_one.get_name()}, Health: {self.player_one.get_health()}, Weapon: {self.player_one.get_weapon()}, Body-Type: {self.player_one.get_body_type()}\n")
            print(f"Player Two: {self.player_two.get_name()}, Health: {self.player_two.get_health()}, Weapon: {self.player_two.get_weapon()}, Body-Type: {self.player_two.get_body_type()}\n")
            # if isinstance(first, ComputerPlayer):
            #     self.bot_attack()
            print("Where do you want to attack your opponent, " f"{first.get_name()}!\n")
            # List of attack options for players (only 2 when declared weapons and body type)
            attack_options = [f"{second.get_name()} Weapon: {second.get_weapon()} ", f"{second.get_name()} Body: {second.get_body_type()} "]
            # Arena effects added here, arena options declared outside if statement so they can be used later in random attack statement
            arena_options = ["Powersaw", "Crushing Mallets", "Flame-Jets"]
            arena_choice = choice(arena_options)
            if self.arena_effects_flag:
                # Adds a 3rd attack option to list
                attack_options += [f"Attempt to push {second.get_name()} into {arena_choice}"]
            
            # Bot specific attack
            if isinstance(first, ComputerPlayer):
                bot_entry_index = choice(attack_options)
                sleep(2)
                print(f"{first.get_name()} is thinking....\n")
                sleep(3)
                if bot_entry_index == attack_options[0]:
                    print(f"{first.get_name()} has selected Weapon: {second.get_weapon()}\n")
                    sleep(3)
                elif bot_entry_index == attack_options[1]:
                    print(f"{first.get_name()} has selected Body Type: {second.get_body_type()}\n")
                    sleep(3)
                elif bot_entry_index == attack_options[2]:
                    print(f"{first.get_name()} attempts to push {second.get_name()} into {arena_choice}\n")
                    sleep(3)
            # Human player menu
            else:
                terminal_menu = TerminalMenu(attack_options)
                menu_entry_index = terminal_menu.show()
                print(f"You have selected {attack_options[menu_entry_index]}\n")
            # Damage calculator
            # Weapon always attacks
            # Dmg calculator for Weapon attacking Weapon
            if menu_entry_index == 0 or bot_entry_index == attack_options[0]:
                damage_taken = self.weap_weap_dmg(first.get_weapon(), second.get_weapon())
                second.damage(damage_taken)
            # Dmg calculator for Weapon attacking Body
            elif menu_entry_index == 1 or bot_entry_index == attack_options[1]:
                damage_taken = self.weap_body_dmg(first.get_weapon(), second.get_body_type())
                second.damage(damage_taken)
            #  Random Arena attack selected
            elif menu_entry_index == 2 or bot_entry_index == attack_options[2]:
                damage_taken = randint(0, 40)
                second.damage(damage_taken)
            print(f"{second.get_name()} takes {damage_taken} damage!\n")

            # Random Arena damage
            if self.arena_effects_flag:
                player_chance = [first, second]
                # random pick of players in game
                player_attacked = choice(player_chance)
                # random damage between 0 - 20
                rand_attack_dmg = randint(0, 20)
                random_chance = randint(0, 100)
                # 25% chance of player taking damage
                if random_chance < 25:
                    arena_choice = choice(arena_options)                    
                    print(f"{player_attacked.get_name()} has driven into the Arena's {arena_choice}!\n")
                    print(f"{player_attacked.get_name()} takes {rand_attack_dmg} damage! ouch...\n")
                    player_attacked.damage(rand_attack_dmg)
                    sleep(5)
            # menu_entry_index = terminal_menu.show()
            sleep(3)
            self.clear_terminal()
            first, second = second, first
        if self.player_one.get_health() > 0:
            print(f"\n{self.player_one.get_name()} Wins!")
        else:
            print(f"\n{self.player_two.get_name()} Wins!")
        sleep(3)
        self.game_exit_flag = True
        self.clear_terminal()

    def arena_effects(self):
        print("Do you want Arena Effects added to game ?\n")
        print(" Arena effects allow players to target their opponent with the Arena's Powersaw's, Crushing Mallets and Flame-Jets!\n")
        print(" Players may also randomly be hit by these effects in the Arena!\n")
        options = ["Yes", "No"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        self.clear_terminal()
        if menu_entry_index == 0:
            print(f"You have selected {options[menu_entry_index]}!\n")
            self.arena_effects_flag = True
        elif menu_entry_index == 1:
            print(f"You have selected {options[menu_entry_index]}!\n")
            self.arena_effects_flag = False
        self.clear_terminal()


# When a player wins it goes back to weapon select menu, maybe add a break statement after the call up there
# Add random change to randint environmental damage each turn to each player


# game =Game()
# game.game_mode()

# in the move function
