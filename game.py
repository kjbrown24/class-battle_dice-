import random
from charactertype import CharacterType

class Game:
    """Manages the Dice Battle game logic ."""
    
    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        self. __player1 = player1
        

        pass  #TODO: Implement die roll )1-6) and apply scaled attack power to defender





















# Instantiating an Enum member
mycharactertype = CharacterType.WARRIOR
# Accessing name and value
print(mycharactertype) # Output : CharacterType.WARRIOR
print (mycharactertype.name ) # Output : ”WARRIOR”
print (mycharactertype.value) # Output : ”Warrior”
