from .grid import Grid


class Player:
    def __init__(self, name: str, player_grid: Grid, turn: bool = False) -> None:
        self.name = name
        self.player_grid = player_grid
        self.shooting_grid = Grid()
        self.turn = turn
        
        self.ships_placed = {
            "1"   :   0,
            "2"   :   0,
            "3"   :   0,
            "4"   :   0
        }
        self.total_ship_squares = 10
    
    
    def shoot(self, opponent):
        coord = input("Enter coordinates to shoot at (in 'x;y' format): ")
        coord = coord.split(";")
        
        target = self.shooting_grid.update_square(int(coord[0]), int(coord[1]))
        self.shooting_grid.draw_grid()
        
        if target == None:
            return self.shoot(opponent)
        elif target == "Miss!":
            print(target)
            self.turn = False
            opponent.turn = True
            return
        else:
            print(target)
            opponent.total_ship_squares -= 1
            return self.shoot(opponent)