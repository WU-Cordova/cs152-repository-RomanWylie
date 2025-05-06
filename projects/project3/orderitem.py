from dataclasses import dataclass



@dataclass
class Drink:
    drink_name : str
    drink_price : float
    def __hash__(self) -> int:
        return hash(self.drink_name) * hash(self.drink_price)

    def __str__(self) -> str:
        return f"{self.drink_name} : ${self.drink_price:.2f}"

class OrderItem:
    def __init__(self, drink:Drink):
        self._drink: Drink = drink
        self._customization: str = ""
    
    def _customize(self, input:str):
        self._customization = input
    
    def __str__(self) -> str:
        return f"{self._drink.drink_name} ({self._customization})"