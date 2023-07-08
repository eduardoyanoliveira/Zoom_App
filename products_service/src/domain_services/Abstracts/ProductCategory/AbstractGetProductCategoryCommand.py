from abc import ABC, abstractmethod


class AbstractGetProductCategoryCommand(ABC):

    @abstractmethod
    def execute(self, category_id : int):
        pass