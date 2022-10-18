from .grid import Grid


class Player:
    def __init__(self, name: str, grid: Grid, turn: bool = False) -> None:
        self.name = name
        self.grid = grid
        self.turn = turn
        
        self.ships_placed = {
            "1"   :   0,
            "2"   :   0,
            "3"   :   0,
            "4"   :   0
        }
    
    
    def shoot_at(self, x: int, y: int):
        pass