class Hand():
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


Rock_Hand = Hand.create_symbol(
    Hand.ROCK, 'Rock', Hand.SCISSORS, Hand.PAPER)
Paper_Hand = Hand.create_symbol(
    Hand.PAPER, 'Paper', Hand.ROCK, Hand.SCISSORS)
Scissors_Hand = Hand.create_symbol(
    Hand.SCISSORS, 'Scissors', Hand.PAPER, Hand.ROCK)
