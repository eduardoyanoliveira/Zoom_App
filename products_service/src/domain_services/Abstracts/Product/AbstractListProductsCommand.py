from abc import ABC, abstractmethod
from typing import List

from domain.entities.Product import Product


class AbstractListProductsCommand(ABC):
    @abstractmethod
    def execute(self) -> List[Product]:
        pass