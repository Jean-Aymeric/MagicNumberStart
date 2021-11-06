from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def compareToMagicNumber(self, num: int) -> int:
        ...

    @abstractmethod
    def getProposalCount(self) -> int:
        ...

    @abstractmethod
    def getMaxNumberOfProposals(self) -> int:
        ...
