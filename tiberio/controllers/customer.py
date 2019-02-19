from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Slot

from views.ui_customer import Ui_Customer


class FormCustomer(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_Customer()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.treeWidget.itemDoubleClicked.connect(self.get_cliente)

    def get_cliente(self):
        self.parent.ui.txtRuc.setText('foo')
        self.parent.ui.lblProveedor.setText('bar')
        self.close()
