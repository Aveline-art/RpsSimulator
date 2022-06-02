from hands import Rock, Paper, Scissors


class RPS():

    def __init__(self) -> None:
        self.rock = Rock()
        self.paper = Paper()
        self.scissors = Scissors()
        self.rock.add_opposing_group(self.paper)
        self.paper.add_opposing_group(self.scissors)
        self.scissors.add_opposing_group(self.rock)

    @property
    def all_sprites(self):
        sprites = self.rock.group.sprites() + self.paper.group.sprites() + \
            self.scissors.group.sprites()
        return sprites

    def create(self, num: int = 1):
        for i in range(num):
            self.rock.group.add(self.rock.create())
            self.paper.group.add(self.paper.create())
            self.scissors.group.add(self.scissors.create())
