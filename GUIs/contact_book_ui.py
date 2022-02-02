# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Designs\contact_book_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.combo_box_group_name = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_box_group_name.setObjectName("combo_box_group_name")
        self.gridLayout.addWidget(self.combo_box_group_name, 1, 0, 1, 1)
        self.line_edit_search = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.line_edit_search.setFont(font)
        self.line_edit_search.setObjectName("line_edit_search")
        self.gridLayout.addWidget(self.line_edit_search, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 89, 781, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_widget_contact_list = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_widget_contact_list.setObjectName("table_widget_contact_list")
        self.table_widget_contact_list.setColumnCount(0)
        self.table_widget_contact_list.setRowCount(0)
        self.verticalLayout.addWidget(self.table_widget_contact_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_add_contact_book = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add_contact_book.setObjectName("btn_add_contact_book")
        self.horizontalLayout_2.addWidget(self.btn_add_contact_book)
        self.btn_edit_contact_book = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_edit_contact_book.setObjectName("btn_edit_contact_book")
        self.horizontalLayout_2.addWidget(self.btn_edit_contact_book)
        self.btn_show_info_contact_book = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_show_info_contact_book.setObjectName("btn_show_info_contact_book")
        self.horizontalLayout_2.addWidget(self.btn_show_info_contact_book)
        self.btn_delete_contact_book = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_delete_contact_book.setObjectName("btn_delete_contact_book")
        self.horizontalLayout_2.addWidget(self.btn_delete_contact_book)
        self.btn_refresh_contact_book = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_refresh_contact_book.setObjectName("btn_refresh_contact_book")
        self.horizontalLayout_2.addWidget(self.btn_refresh_contact_book)
        self.btn_group_name_control = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_group_name_control.setObjectName("btn_group_name_control")
        self.horizontalLayout_2.addWidget(self.btn_group_name_control)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "search"))
        self.btn_add_contact_book.setText(_translate("MainWindow", "Add"))
        self.btn_edit_contact_book.setText(_translate("MainWindow", "Edit"))
        self.btn_show_info_contact_book.setText(_translate("MainWindow", "Show Info"))
        self.btn_delete_contact_book.setText(_translate("MainWindow", "Delete"))
        self.btn_refresh_contact_book.setText(_translate("MainWindow", "Refresh"))
        self.btn_group_name_control.setText(_translate("MainWindow", "Panle Group Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
