from contract.imodel import IModel
from contract.iview import IView
from contract.iactionperformer import IActionPerformer


class Controller(IActionPerformer):
    # To be completed

    def setView(self, view: IView) -> None:
        ...

    def setModel(self, model: IModel) -> None:
        ...

    def start(self) -> None:
        ...

    def performProposeNumber(self, num: int) -> None:
        ...
