from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

def printHp(char):
    print(f"{char.getUsername()} HP: {char.getHp()}")

Character1 = Swordsman("Royce")
Character2 = Boss("Archie")
printHp(Character1)
printHp(Character2)
Character1.slashAttack(Character2)
Character1.basicAttack(Character2)
printHp(Character1)
printHp(Character2)
Character2.heal()
Character2.basicAttack(Character1)
Character2.rangedAttack(Character1)
Character2.slashAttack(Character1)
Character2.magicAttack(Character1)
printHp(Character1)
printHp(Character2)