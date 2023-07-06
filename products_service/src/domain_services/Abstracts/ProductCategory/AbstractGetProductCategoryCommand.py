from abc import ABC, abstractmethod
from typing import int


class AbstractGetProductCategoryCommand(ABC):

    @abstractmethod
    def execute(self, category_id : int):
        pass