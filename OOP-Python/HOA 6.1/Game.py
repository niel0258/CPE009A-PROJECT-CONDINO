from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Character import Character
from Novice import Novice
from Boss import Boss
from os import system
from Turn_Logic import *

try:
    from pynput.keyboard import Key, Listener
except ImportError:
    print("Dependency missing!,\nplease install the pynput module")
    raise Exception("Import Error")
    
##########################################
#           MISCELLANOUS
#########################################

def change_role(character):
    selected_char = 0
    roles = [Swordsman,Archer,Magician]
    num_roles = len(roles)
    def print_choices():
        system('clear')
        print(f"{character.getUsername()}, Select Role:")
        options = [' ' for _ in range(num_roles)]
        options[selected_char] = '>'
        print(f"[{options[0]}] Swordsman\n[{options[1]}] Archer\n[{options[2]}] Magician")
        
    def select_choices(key):
        nonlocal selected_char
        if key == Key.up:
            selected_char = (selected_char - 1) % num_roles
        elif key == Key.down:
            selected_char = (selected_char + 1) % num_roles
        elif key == Key.enter:
            return False
        print_choices()
    
    print_choices()
    
    with Listener(on_press=select_choices) as listener:
        listener.join()
        
    current_wins = character.check_wins()
    Character.char_list.remove(character)
    
    if character in Character.player_list:
        Character.player_list.remove(character)
        
    character = roles[selected_char](character.getUsername())
    character.set_wins(current_wins)
    return character

def set_to_maxHp(character):
    character.setHp(100 + character.getVit())
    
def createMonster():
    return Boss("Monster")

#########################################
#               GAME MODE
#########################################

#NOTE: ADD A "PLAY AGAIN" LOGIC

def pve():
    system("clear")
    player = Novice(input("Input username: "))
    player.be_player()
    
    system('clear')
    createMonster()
    game_status = round_logic(True)
    while game_status != -1:
        if game_status == 1:
            player.set_wins(player.check_wins() + 1)
            set_to_maxHp(player)
            if player.check_wins() == 2:
                system('clear')
                player = change_role(player)
                player.be_player()
        createMonster()
        game_status = round_logic(True)

    
def pvp():
    system('clear')
    player_1 = Novice(input("Input name for Player 1: "))
    player_2 = Novice(input("Input name for Player 2: "))
    
    change_role(player_1).be_player()
    change_role(player_2).be_player()
    
    game_status = round_logic(False)
    while game_status != -1:
        if game_status == 1:
            for player in Character.player_list:
                set_to_maxHp(player)
        game_status = round_logic(False)
    
#################################################
#              MAIN MENU 
#################################################
def main_menu():
    curr_choice_mm = 0
    selection_active = False
    
    def print_mm(first_press):
        system("clear")
        print("Medieval Chaos:Oblivion")
        
        if first_press:
            print("Press any key to continue")
        else:
            print("Select Mode")
        
    def change_mm(selected):
        print_mm(False)
        options = [' ',' ']
        options[selected] = '>'
        print(f"{options[0]} Singleplayer\n {options[1]} Player vs Player")

    def select_on_menu(key):
        nonlocal curr_choice_mm,selection_active
        if not selection_active:#"Press any key" screen
            selection_active = True
        elif key == Key.up:
            curr_choice_mm = (curr_choice_mm - 1) % 2
        elif key == Key.down:
            curr_choice_mm = (curr_choice_mm + 1) % 2
        elif key == Key.enter:
            return False
        change_mm(curr_choice_mm)

    print_mm(True)
    
    with Listener(on_press=select_on_menu) as listener:
        listener.join()
        
    if curr_choice_mm == 0:
        pve()
    else:
        pvp()

main_menu()