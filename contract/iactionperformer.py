from abc import ABC, abstractmethod


class IActionPerformer(ABC):
    @abstractmethod
    def performProposeNumber(self, num: int) -> None:
        ...
