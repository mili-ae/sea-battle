from enum import Enum

class ShipType(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

class ShipDirection(Enum):
    HORIZONTAL = 'h'
    VERTICAL = 'v'
    
class SquareStatus(Enum):
    NONE = ' '
    OCCUPIED = 'S'
    DESTROYED = 'D'
    MISS = '0'