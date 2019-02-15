from PySide2.QtWidgets import QDialog, QTreeWidgetItem
from PySide2.QtCore import Slot, Qt

from views.customer import FormCustomer
from ui.ui_invoice import Ui_Invoice


class FormInvoice(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Invoice()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.treeProductos.setAlternatingRowColors(True)

        self.set_col_width_tree_widget()

        self.ui.btnCancelar.clicked.connect(self.close)
        self.ui.btnAgregarProd.clicked.connect(self.agregar_producto)
        self.ui.txtRuc.returnPressed.connect(self.buscar_cliente)

    def set_col_width_tree_widget(self):
        self.ui.treeProductos.setColumnWidth(0, 60)
        self.ui.treeProductos.setColumnWidth(1, 150)
        self.ui.treeProductos.setColumnWidth(2, 70)
        self.ui.treeProductos.setColumnWidth(3, 80)

    @Slot()
    def agregar_producto(self):
        print('add prod')
        f = QTreeWidgetItem(self.ui.treeProductos, [
            self.ui.txtCantidad.text(),
            self.ui.txtProducto.text(),
            self.ui.txtPrecio.text(),
        ])
        f.setTextAlignment(0, Qt.AlignRight)
        f.setTextAlignment(1, Qt.AlignLeft)
        f.setTextAlignment(2, Qt.AlignRight)
        f.setTextAlignment(3, Qt.AlignRight)
        #QTreeWidgetItem(self.ui.treeProductos, ['1', 'IMPRESORA KYOCERA', '500.00', '500.00'])

    @Slot()
    def buscar_cliente(self):
        print('search')
        ui_cliente = FormCustomer(self)
        ui_cliente.exec_()

