import unittest
from game.grid import Grid

from game.player import Player
from game.utils.enums import ShipDirection, ShipType

class PlayerTest(unittest.TestCase):
    
    def test_shooting(self):
        player1_grid = Grid()
        player2_grid = Grid()
        
        player1 = Player("1", player1_grid, True)
        player2 = Player("2", player2_grid)
        
        player1.player_grid.put_ship_at(5, 5, ShipDirection.VERTICAL, ShipType.FOUR)
        player2.player_grid.put_ship_at(5, 5, ShipDirection.VERTICAL, ShipType.FOUR)
        
        player1.shoot(player2)
        
        # Check if shot missed (ENTER '1;1')
        self.assertFalse(player1.turn)
        self.assertTrue(player2.turn)
        
        player2.shoot(player1)
        
        # Check if shot hit (ENTER 5;5 - 5;9)
        self.assertEqual(9, player1.total_ship_squares)
        
        result = player2.shoot(player1)
        
        # Check hit of the same tile several times
        self.assertIsNone(result)
    
    
if __name__ == "__main__":
    unittest.main()