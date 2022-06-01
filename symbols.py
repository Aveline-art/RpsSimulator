class Symbol():
    ROCK = "RO"
    PAPER = "PA"
    SCISSORS = "SC"

    def __init__(self, symbol: str, name: str) -> None:
        self.symbol = symbol
        self.name = name

    @staticmethod
    def wins_against() -> str:
        raise NotImplementedError

    @staticmethod
    def loses_to() -> str:
        raise NotImplementedError

    @classmethod
    def create_symbol(cls,
                      symbol: str,
                      name: str,
                      wins_against: str,
                      loses_to: str):
        new_symbol = cls(symbol, name)
        new_symbol.wins_against = lambda: wins_against
        new_symbol.loses_to = lambda: loses_to
        return new_symbol


Rock_Symbol = Symbol.create_symbol(
    Symbol.ROCK, 'Rock', Symbol.SCISSORS, Symbol.PAPER)
Paper_Symbol = Symbol.create_symbol(
    Symbol.PAPER, 'Paper', Symbol.ROCK, Symbol.SCISSORS)
Scissors_Symbol = Symbol.create_symbol(
    Symbol.SCISSORS, 'Scissors', Symbol.PAPER, Symbol.ROCK)
