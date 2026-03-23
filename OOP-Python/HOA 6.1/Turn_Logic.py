from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from random import randint
from Character import Character
from os import system
from time import sleep as wait

try:
    from pynput.keyboard import Key, Listener
except ImportError:
    print("Dependency missing!,\nplease install the pynput module")
    raise Exception("Import Error")


##########################################
#               BATTLE LOGIC
##########################################

def print_Hp():
    for char in Character.char_list:
        char_Hp = char.getHp()
        if char_Hp <= 0:#To avoid printing negative Hp
            char_Hp = 0
        print(f"{char.getUsername()}'s Hp : {char_Hp}")

def create_attack_menu(player_char):
    player_attacks = {
        "Basic Attack" : player_char.basicAttack
        }
    
    if isinstance(player_char,Swordsman):
        player_attacks['Slash Attack'] = player_char.slashAttack
    elif isinstance(player_char,Magician):
        player_attacks["Heal"] = player_char.heal
        player_attacks["Magic Attack"] = player_char.magicAttack
    elif isinstance(player_char,Archer):
        player_attacks["Ranged Attack"] = player_char.rangedAttack
        
    return player_attacks
    
def get_enemy_char(player_char):
    for char in Character.char_list:
        if char is not player_char:
            return char
    
def turn_menu(player_char):
    selected_move = 0
    attack_list = create_attack_menu(player_char)

    def print_turn_menu():
        system('clear')
        options = [' ' for _ in range(len(attack_list))]
        options[selected_move] = '*'
        
        print(f"{player_char.getUsername()}'s Turn")
        
        for i, attack in enumerate(attack_list):
            print("[" + options[i] + "]" + attack + '\t', end = "")

    def on_press(key):
        nonlocal selected_move

        if key == Key.left:
            selected_move = (selected_move - 1) % len(attack_list)
            print_turn_menu()

        elif key == Key.right:
            selected_move = (selected_move + 1) % len(attack_list)
            print_turn_menu()

        elif key == Key.enter:
            system('clear')
            return False  # stop listener

    print_turn_menu()

    with Listener(on_press=on_press) as listener:
        listener.join()

    attack_name = list(attack_list.keys())[selected_move]

    if attack_name == "Heal":
        attack_list[attack_name]()
    else:
        attack_list[attack_name](get_enemy_char(player_char))

    print_Hp()
    wait(3)
    
def any_char_dead(is_pve):#-1 for player died, 1 for area cleared 
    for char in Character.char_list:
        if char.getHp() <= 0:
            if is_pve:
                if char.is_a_player():
                    system('clear')
                    print("Player died")
                    wait(3)
                    return -1
                else:
                    system('clear')
                    print("Area cleared")
                    print(f"Current wins:{char.check_wins()}")
                    Character.char_list.pop()#remove monster from char list,assumes only player and monster
                    wait(3)
                    return 1
            else:
                system('clear')
                print(f"{char.getUsername()} Died")
                winner= get_enemy_char(char)
                winner.set_wins(winner.check_wins()+1)
                print(f"{winner.getUsername()} WINS! Wins:{winner.check_wins()}")
                wait(3)
                system('clear')
                return 1
    return 0

        
def monster_attack(monster):
    system('clear')
    attacks = (monster.basicAttack,monster.slashAttack,monster.magicAttack,monster.rangedAttack,monster.heal)
    rand_move = randint(0, 4)
    if rand_move == 4:
        attacks[rand_move]()
    else:
        attacks[rand_move](Character.player_list[0])
    print_Hp()
    wait(3)

def round_logic(is_pve):#different logics for pve and pvp
    dead_status = any_char_dead(is_pve)
    while not dead_status:
        char_on_turn = Character.char_list[randint(0,len(Character.char_list)-1)]
        if not char_on_turn.is_a_player() and is_pve:
            monster_attack(char_on_turn)
        else:
            turn_menu(char_on_turn)
        dead_status = any_char_dead(is_pve)
    return dead_status