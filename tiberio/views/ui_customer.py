# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer.ui',
# licensing of 'customer.ui' applies.
#
# Created: Fri Feb 15 11:20:14 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Customer(object):
    def setupUi(self, Customer):
        Customer.setObjectName("Customer")
        Customer.resize(369, 260)
        self.treeWidget = QtWidgets.QTreeWidget(Customer)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 351, 241))
        self.treeWidget.setIndentation(0)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        self.retranslateUi(Customer)
        QtCore.QMetaObject.connectSlotsByName(Customer)

    def retranslateUi(self, Customer):
        Customer.setWindowTitle(QtWidgets.QApplication.translate("Customer", "Cliente", None, -1))
        self.treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("Customer", "RUC", None, -1))
        self.treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("Customer", "RAZON SOCIAL", None, -1))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("Customer", "10444948430", None, -1))
        self.treeWidget.topLevelItem(0).setText(1, QtWidgets.QApplication.translate("Customer", "CORPORACION ZEVALLOS", None, -1))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

