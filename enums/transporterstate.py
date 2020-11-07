from enum import Enum

class TransporterState(Enum):
    EMPTY = 0
    PICKUP = 1 # SHIPMENT HAS YET TO BE PICKED UP
    TRANSPORTING = 2