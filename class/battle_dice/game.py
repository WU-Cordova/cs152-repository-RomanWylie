import random
from character import Character

class Game:
    def __init__(self, player1: Character, player2: Character) -> None:
        """ Constructor for the Game class. Sets the players to instance variables.
        Args:   
            player1 (Character): The first player.
            player2 (Character): The second player.
        """
        self.p1 = player1
        self.p2 = player2


    def attack(self, attacker: Character, defender: Character) -> None:
        """ Attacks the defender. Algorithm: 
            1. Roll a random number between 1 and 6 for the attack.
            2. Subtract the attack value from the defender's health.
            3. If the defender's health is less than or equal to 0, they are defeated.
            4. Print the result of the attack.
        Args:
            attacker (Character): The attacker.
            defender (Character): The defender. 
        """
        roll = random.randint(1,6)
        damage = attacker.attack_power*roll // 2
        defender.health -= damage
        print(f"{defender.name} takes {damage} damage!")
            
            
            


    def start_battle(self) -> None:
        """ Starts the battle between the two players. Algorithm: 
            1. While both players are alive, do the following:
                1.1. Player 1 attacks Player 2.
                1.2. If Player 2 is defeated, break the loop.
                1.3. Player 2 attacks Player 1.
                1.4. If Player 1 is defeated, break the loop.
            2. Print the result of the battle.
        """
        while self.p1.health > 0 and self.p2.health > 0:
            self.attack(self.p1, self.p2)
            if self.p2.health <= 0:
                loser = self.p2.name
                winner=self.p1.name
                break
            self.attack(self.p2, self.p1)
            if self.p1.health <= 0:
                loser = self.p1.name
                winner = self.p2.name
                break
        print(f"{loser} has been defeated!")
        print(f"{winner} is victorious!")
        return

                
