# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\FAMILIA ROJAS YANES\Desktop\programas\ganado\ganado.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1021, 829)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.todos_table = QtWidgets.QTableView(self.frame_2)
        self.todos_table.setObjectName("todos_table")
        self.verticalLayout_2.addWidget(self.todos_table)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setMinimumSize(QtCore.QSize(117, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nuevo_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nuevo_btn.setFont(font)
        self.nuevo_btn.setObjectName("nuevo_btn")
        self.verticalLayout_3.addWidget(self.nuevo_btn)
        self.remove_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.verticalLayout_3.addWidget(self.remove_btn)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.exportar_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exportar_btn.setFont(font)
        self.exportar_btn.setObjectName("exportar_btn")
        self.verticalLayout_3.addWidget(self.exportar_btn)
        self.styles_combo = QtWidgets.QComboBox(self.frame)
        self.styles_combo.setObjectName("styles_combo")
        self.verticalLayout_3.addWidget(self.styles_combo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_4.addWidget(self.tableView_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableView_3 = QtWidgets.QTableView(self.tab_3)
        self.tableView_3.setObjectName("tableView_3")
        self.verticalLayout_5.addWidget(self.tableView_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableView_4 = QtWidgets.QTableView(self.tab_4)
        self.tableView_4.setObjectName("tableView_4")
        self.verticalLayout_6.addWidget(self.tableView_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 26))
        self.menubar.setObjectName("menubar")
        self.menu_Archivo = QtWidgets.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        self.menu_Editar = QtWidgets.QMenu(self.menubar)
        self.menu_Editar.setObjectName("menu_Editar")
        self.menu_Vista = QtWidgets.QMenu(self.menubar)
        self.menu_Vista.setObjectName("menu_Vista")
        self.menu_Acerca = QtWidgets.QMenu(self.menubar)
        self.menu_Acerca.setObjectName("menu_Acerca")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Buscar = QtWidgets.QAction(MainWindow)
        self.action_Buscar.setObjectName("action_Buscar")
        self.action_apariencia = QtWidgets.QAction(MainWindow)
        self.action_apariencia.setObjectName("action_apariencia")
        self.action_Acerca = QtWidgets.QAction(MainWindow)
        self.action_Acerca.setObjectName("action_Acerca")
        self.action_Editar = QtWidgets.QAction(MainWindow)
        self.action_Editar.setObjectName("action_Editar")
        self.action_Eliminar = QtWidgets.QAction(MainWindow)
        self.action_Eliminar.setObjectName("action_Eliminar")
        self.action_Salir = QtWidgets.QAction(MainWindow)
        self.action_Salir.setObjectName("action_Salir")
        self.action_Nuevo = QtWidgets.QAction(MainWindow)
        self.action_Nuevo.setObjectName("action_Nuevo")
        self.menu_Archivo.addAction(self.action_Nuevo)
        self.menu_Archivo.addAction(self.action_Editar)
        self.menu_Archivo.addAction(self.action_Eliminar)
        self.menu_Archivo.addAction(self.action_Salir)
        self.menu_Editar.addAction(self.action_Buscar)
        self.menu_Vista.addAction(self.action_apariencia)
        self.menu_Acerca.addAction(self.action_Acerca)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menu_Editar.menuAction())
        self.menubar.addAction(self.menu_Vista.menuAction())
        self.menubar.addAction(self.menu_Acerca.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ganado"))
        self.nuevo_btn.setText(_translate("MainWindow", "Nuevo"))
        self.remove_btn.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_3.setText(_translate("MainWindow", "Editar"))
        self.exportar_btn.setText(_translate("MainWindow", "Exportar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Todos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vendidos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Muertos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "comprados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Vacunas"))
        self.menu_Archivo.setTitle(_translate("MainWindow", "&Archivo"))
        self.menu_Editar.setTitle(_translate("MainWindow", "&Editar"))
        self.menu_Vista.setTitle(_translate("MainWindow", "&Vista"))
        self.menu_Acerca.setTitle(_translate("MainWindow", "&Ayuda"))
        self.action_Buscar.setText(_translate("MainWindow", "&Buscar"))
        self.action_apariencia.setText(_translate("MainWindow", "&apariencia"))
        self.action_Acerca.setText(_translate("MainWindow", "&Acerca"))
        self.action_Editar.setText(_translate("MainWindow", "&Editar"))
        self.action_Eliminar.setText(_translate("MainWindow", "&Eliminar"))
        self.action_Salir.setText(_translate("MainWindow", "&Salir"))
        self.action_Salir.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_Nuevo.setText(_translate("MainWindow", "&Nuevo"))
