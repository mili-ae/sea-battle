import unittest

from game.utils.enums import ShipDirection, ShipType, SquareStatus
from game.grid import Grid


class GridTest(unittest.TestCase):
    
    def test_square_update(self):
        test_grid = Grid()
        grd = test_grid.get_grid()
        
        #Test forced placement on the grid and placement enums
        test_grid.update_square(5, 5, place=True, type=SquareStatus.OCCUPIED)
        grd = test_grid.get_grid()
        self.assertEqual(grd[5][5], SquareStatus.OCCUPIED.value)
        
        test_grid.update_square(1, 4, place=True, type=SquareStatus.DESTROYED)
        grd = test_grid.get_grid()
        self.assertEqual(grd[1][4], SquareStatus.DESTROYED.value)
        
        test_grid.update_square(4, 4, place=True, type=SquareStatus.MISS)
        grd = test_grid.get_grid()
        self.assertEqual(grd[4][4], SquareStatus.MISS.value)
        
        
    def test_ship_placement(self):
        test_grid = Grid()
        
        test_grid.put_ship_at(1, 1, ShipDirection.HORIZONTAL, ShipType.FOUR)
        grd = test_grid.get_grid()
        for i in range(1, 4):
            self.assertEqual(grd[i][1], SquareStatus.OCCUPIED)
            
        test_grid.put_ship_at(8, 1, ShipDirection.VERTICAL, ShipType.THREE)
        grd = test_grid.get_grid()
        for i in range(1, 3):
            self.assertEqual(grd[8][i], SquareStatus.OCCUPIED)
            
        test_grid.put_ship_at(9, 9, ShipDirection.VERTICAL, ShipType.ONE)
        grd = test_grid.get_grid()
        self.assertEqual(grd[9][9], SquareStatus.OCCUPIED)
        
        
if __name__ == "__main__":
    unittest.main()