class Symbol():
    ROCK = "RO"
    PAPER = "PA"
    SCISSORS = "SC"

    def __init__(self, symbol) -> None:
        self.symbol = symbol
    
    def loses_to():
        raise NotImplementedError

class Rock_Symbol(Symbol):
    def __init__(self) -> None:
        super().__init__(self.ROCK)
    
    def loses_to():
        return Paper_Symbol()

class Paper_Symbol(Symbol):
    def __init__(self) -> None:
        super().__init__(self.PAPER)
    
    def loses_to():
        return Scissors_Symbol()
        
class Scissors_Symbol(Symbol):
    def __init__(self) -> None:
        super().__init__(self.SCISSORS)
    
    def loses_to():
        return Rock_Symbol()

