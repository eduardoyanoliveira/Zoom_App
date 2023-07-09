from abc import ABC, abstractmethod


class AbstractListProductCategoryCommand(ABC):

    @abstractmethod
    def execute(self):
        pass