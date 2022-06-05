from msilib.schema import Error
from growth.cell import Cell, CellType
import preset
import random


class Culture():
    distribution = preset.DISTRIBUTION

    def __init__(self, distribution: dict[CellType, list[CellType]]) -> None:
        self.distribution = distribution

    def create_cell(self, cell_type=None):
        if cell_type not in self.distribution.keys():
            raise Error
        if cell_type:
            return Cell(cell_type, self.distribution[cell_type])
        else:
            random_type = random.choice([self.distribution.keys()])
            return Cell(random_type, self.distribution[random_type])
