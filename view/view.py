from contract.iview import IView
from contract.imodel import IModel
from contract.iactionperformer import IActionPerformer


class View(IView):
    # To be completed

    def setActionPerformer(self, actionPerformer: IActionPerformer) -> None:
        ...

    def setModel(self, model: IModel) -> None:
        ...

    def showMessage(self, message: str) -> None:
        ...

    def askProposal(self) -> int:
        ...
