# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invoice.ui',
# licensing of 'invoice.ui' applies.
#
# Created: Fri Feb 15 11:50:23 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Invoice(object):
    def setupUi(self, Invoice):
        Invoice.setObjectName("Invoice")
        Invoice.resize(401, 409)
        self.label = QtWidgets.QLabel(Invoice)
        self.label.setGeometry(QtCore.QRect(20, 24, 47, 13))
        self.label.setObjectName("label")
        self.txtFecha = QtWidgets.QLineEdit(Invoice)
        self.txtFecha.setGeometry(QtCore.QRect(70, 20, 81, 20))
        self.txtFecha.setText("")
        self.txtFecha.setObjectName("txtFecha")
        self.txtDoc = QtWidgets.QLineEdit(Invoice)
        self.txtDoc.setGeometry(QtCore.QRect(260, 20, 121, 20))
        self.txtDoc.setObjectName("txtDoc")
        self.label_2 = QtWidgets.QLabel(Invoice)
        self.label_2.setGeometry(QtCore.QRect(190, 24, 58, 13))
        self.label_2.setObjectName("label_2")
        self.txtRuc = QtWidgets.QLineEdit(Invoice)
        self.txtRuc.setGeometry(QtCore.QRect(70, 50, 81, 20))
        self.txtRuc.setObjectName("txtRuc")
        self.label_3 = QtWidgets.QLabel(Invoice)
        self.label_3.setGeometry(QtCore.QRect(20, 54, 25, 13))
        self.label_3.setObjectName("label_3")
        self.lblProveedor = QtWidgets.QLabel(Invoice)
        self.lblProveedor.setGeometry(QtCore.QRect(190, 54, 33, 13))
        self.lblProveedor.setObjectName("lblProveedor")
        self.treeProductos = QtWidgets.QTreeWidget(Invoice)
        self.treeProductos.setGeometry(QtCore.QRect(10, 170, 381, 181))
        self.treeProductos.setMinimumSize(QtCore.QSize(0, 0))
        self.treeProductos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeProductos.setBaseSize(QtCore.QSize(-19238, 0))
        self.treeProductos.setIndentation(0)
        self.treeProductos.setColumnCount(4)
        self.treeProductos.setObjectName("treeProductos")
        self.groupBox = QtWidgets.QGroupBox(Invoice)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 381, 81))
        self.groupBox.setObjectName("groupBox")
        self.txtCantidad = QtWidgets.QLineEdit(self.groupBox)
        self.txtCantidad.setGeometry(QtCore.QRect(60, 20, 81, 20))
        self.txtCantidad.setText("")
        self.txtCantidad.setObjectName("txtCantidad")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 24, 47, 13))
        self.label_4.setObjectName("label_4")
        self.txtProducto = QtWidgets.QLineEdit(self.groupBox)
        self.txtProducto.setGeometry(QtCore.QRect(250, 20, 121, 20))
        self.txtProducto.setText("")
        self.txtProducto.setObjectName("txtProducto")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(180, 20, 47, 13))
        self.label_5.setObjectName("label_5")
        self.txtPrecio = QtWidgets.QLineEdit(self.groupBox)
        self.txtPrecio.setGeometry(QtCore.QRect(60, 50, 81, 20))
        self.txtPrecio.setText("")
        self.txtPrecio.setObjectName("txtPrecio")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 54, 47, 13))
        self.label_6.setObjectName("label_6")
        self.btnAgregarProd = QtWidgets.QPushButton(self.groupBox)
        self.btnAgregarProd.setGeometry(QtCore.QRect(300, 50, 75, 23))
        self.btnAgregarProd.setObjectName("btnAgregarProd")
        self.btnGuardar = QtWidgets.QPushButton(Invoice)
        self.btnGuardar.setGeometry(QtCore.QRect(80, 370, 75, 23))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnCancelar = QtWidgets.QPushButton(Invoice)
        self.btnCancelar.setGeometry(QtCore.QRect(240, 370, 75, 23))
        self.btnCancelar.setObjectName("btnCancelar")

        self.retranslateUi(Invoice)
        QtCore.QMetaObject.connectSlotsByName(Invoice)

    def retranslateUi(self, Invoice):
        Invoice.setWindowTitle(QtWidgets.QApplication.translate("Invoice", "Factura", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Invoice", "Fecha:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Invoice", "Documento:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Invoice", "RUC:", None, -1))
        self.lblProveedor.setText(QtWidgets.QApplication.translate("Invoice", "-", None, -1))
        self.treeProductos.headerItem().setText(0, QtWidgets.QApplication.translate("Invoice", "Cantidad", None, -1))
        self.treeProductos.headerItem().setText(1, QtWidgets.QApplication.translate("Invoice", "Producto", None, -1))
        self.treeProductos.headerItem().setText(2, QtWidgets.QApplication.translate("Invoice", "P. Unitario", None, -1))
        self.treeProductos.headerItem().setText(3, QtWidgets.QApplication.translate("Invoice", "Total", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Invoice", "Producto", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Invoice", "Cantidad:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Invoice", "Producto:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Invoice", "Precio:", None, -1))
        self.btnAgregarProd.setText(QtWidgets.QApplication.translate("Invoice", "Agregar", None, -1))
        self.btnGuardar.setText(QtWidgets.QApplication.translate("Invoice", "Guardar", None, -1))
        self.btnCancelar.setText(QtWidgets.QApplication.translate("Invoice", "Cancelar", None, -1))

