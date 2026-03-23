from os import system
try:
    from pynput.keyboard import Key, Listener
except ImportError:
    print("Dependency missing!\n,please install the pynput module")


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
    print(f"{options[0]} Singleplayer\n {options[1]} Multiplayer")

def select_on_menu(key):
    global curr_choice_mm,selection_active
    if not selection_active:#"Press any key" screen
        selection_active = True
    elif key == Key.up:
        curr_choice_mm = (curr_choice_mm + 1) % 2
    elif key == Key.down:
        curr_choice_mm = (curr_choice_mm + 1) % 2
    elif key == Key.enter:
        return False
    change_mm(curr_choice_mm)