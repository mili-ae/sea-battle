from tabulate import tabulate
from .utils.enums import ShipDirection, ShipType, SquareStatus


class Grid:
    '''
    Module for working with game grid.
    '''
    def __init__(self) -> None:
        self.__x = 10
        self.__y = 10
        self.__grid = list()
        
        for i in range(self.__y):
            self.__grid.append([SquareStatus.NONE] * self.__x)
            
    
    def put_ship_at(self, x: int, y: int, direction: ShipDirection, ship: ShipType):
        '''
        This method is used for placing ships onto the grid
        '''
        ship_length = ship.value
        
        while ship_length != 0:
            try:
                if direction == ShipDirection.HORIZONTAL:
                    self.create_ship_square_at(x, y)
                    x += 1
                else:
                    self.create_ship_square_at(x, y)
                    y += 1
            except IndexError:
                pass
                
            ship_length -= 1

    def create_ship_square_at(self, x: int, y: int) -> None:
        '''
        Creates ship square on the grid
        '''
        self.__grid[x][y] = SquareStatus.OCCUPIED
    
    def update_square(self, x: int, y: int, delete: bool = False) -> str:
        '''
        Updates the status of squares on grid
        '''
        square = self.__grid[x][y]
        
        if delete:
            square = SquareStatus.NONE.value
            return
        
        if square == SquareStatus.DESTROYED or square == SquareStatus.MISS:
            return None
        elif square == SquareStatus.NONE.value:
            square = SquareStatus.MISS
            return "Miss!"
        else:
            square = SquareStatus.DESTROYED
            return "Hit!!"

    def draw_grid(self):
        data = list()
        
        for i in range(10):
            copy = self.__grid[:]
            data.append(copy[i])
            for j in range(10):
                try:
                    data[i][j] = data[i][j].value
                except:
                    pass   
        
        print(tabulate(data, tablefmt="grid"))
