from typing import Tuple
from game import grid, player, ship
import os

from game.utils.enums import ShipDirection, ShipType


class Main:
    def __init__(self) -> None:
        self.ships_limit = {
            "1"   :   4,
            "2"   :   3,
            "3"   :   2,
            "4"   :   1
        }
 
    def start_game(self) -> None:
        os.system("clear")
        
        # Create grids for each player
        player_one_field = grid.Grid()
        player_two_field = grid.Grid()
        
        #Create players
        player_name = input("Enter Player 1 name: ")
        player_one = player.Player(player_name, player_one_field, True)
        player_name = input("Enter Player 2 name: ")
        player_two = player.Player(player_name, player_two_field)
        
        os.system("clear")
        print("Before we begin, you need to place your ships.")
        self.start_placing_ships(player_one)
        self.start_placing_ships(player_two)  
        
    def start_placing_ships(self, player: player.Player):
        pgrid = player.grid        
        
        print("Ships are placed in format of 'x;y;t;d' where X and Y are the coordinates, T - type of the ship in int(1-4) and D - direction(h,v)")
        print(f"\n\nPlayer {player.name}, place your ships!")
        while player.ships_placed != self.ships_limit:
            print(pgrid.draw_grid())
            pinput = input()
            
            data = self.check_and_format_input(pinput)
            check = data[0]
            pinput = data[1]
            while check == True:
                if self.ships_limit[str(pinput[2])] == player.ships_placed[str(pinput[2])]:
                    print(f"You already reached limit of {pinput[2]}-square ships")
                    break
                
                pgrid.put_ship_at(int(pinput[0]) - 1, int(pinput[1]) - 1, ShipDirection(pinput[3]), ShipType(int(pinput[2])))
                player.ships_placed[str(pinput[2])] += 1
                os.system("clear")
                print("Ships are placed in format of 'x;y;t;d' where X and Y are the coordinates, T - type of the ship in int(1-4) and D - direction(h,v)")
                break
        
    def check_and_format_input(self, pinput: str) -> Tuple[bool, list[str]]:
        pinput = pinput.split(";")
        allowed_dir = ["h", "v"]
        
        if int(pinput[0]) > 10 or int(pinput[1]) > 10 or int(pinput[0]) < 1 or int(pinput[1]) < 1:
            return (False, [])
        
        if int(pinput[2]) < 1 or int(pinput[2]) > 4:
            return (False, [])
        
        if pinput[3] not in allowed_dir:
            return (False, [])
        
        return (True, pinput)
            
    def loop(self):
        pass
        

    

if __name__ == "__main__":
    game_process = Main().start_game()