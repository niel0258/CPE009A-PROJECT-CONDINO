from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician

def printHp(char):
    print(f"{char.getUsername()} HP: {char.getHp()}")

Character1 = Swordsman("Royce")
Character2 = Magician("Archie")
printHp(Character1)
printHp(Character2)
Character1.slashAttack(Character2)
Character1.basicAttack(Character2)
printHp(Character1)
printHp(Character2)
Character2.heal()
Character2.magicAttack(Character1)
#Character2.slashAttack(Character1)#changed magicAttack to slashAttack
printHp(Character1)
printHp(Character2)