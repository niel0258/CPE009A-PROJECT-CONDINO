from Character import Character

class Novice(Character):
    def basicAttack(self,character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Attack! -{self.getDamage()}")
    

#character1 = Novice("Niel")
#print(character1.getUsername())
#print(character1.getHp())

#The Novice class inherits the attributes and methods of the superclass (Character) which lets it access all the methods
#and attributes of the original class