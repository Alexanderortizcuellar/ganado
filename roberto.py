from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import os
import qdarkgraystyle
import sys
from ui_ganado import Ui_MainWindow
import ui_exportar
import ui_tracker
import ui_calendar_dialog
from pathlib import Path
from PyQt5 import QtWidgets


class DataModel(QAbstractTableModel):
    def __init__(self, data:list, headers:list):
        super().__init__()
        self._data = [[item for item in items] for items in data]
        self.headers = [header[0] for header in headers]

    def data(self, index: QModelIndex, role: int):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            print(index.row(), index.column(), "here!", self._data)
            value = self._data[index.row()][index.column()]
            return str(value)
        
    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 22
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if role==Qt.DisplayRole:
            if orientation==Qt.Horizontal:
                return self.headers[section]
            
    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable
    
    def setData(self, index: QModelIndex, value, role: int = ...) -> bool:
        if role == Qt.EditRole:
            self._data[index.row()][index.column()] = value
            con = sqlite3.connect(f"{os.getcwd()}/ganado.db")
            c = con.cursor()
            record = self.index(index.row(), 0)
            if record is not None:
                #c.execute(f"UPDATE ganado SET Numero=5 WHERE Numero={record}")
                con.commit()
            con.close()
            return True
        return False
    
    def removeRows(self, position, rows, QModelIndex):
        self.beginRemoveRows(QModelIndex, position, position+rows-1)
        for i in range(rows):
            del(self._data[position])
        self.endRemoveRows()
        self.layoutChanged.emit()
        return True


class CalendarDialog(QDialog, ui_calendar_dialog.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.calendar.selectionChanged.connect(self.set_date)
        self.buttonBox:QDialogButtonBox.rejected.connect(self.close)
    def set_date(self):
        date = self.calendar.selectedDate()
        self.date_entry.setDate(date)



class Tracker(QDialog, ui_tracker.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.buttons_dlg:QDialogButtonBox
        self.buttons_dlg.accepted.connect(self.insert_record)
        self.comprado.clicked.connect(self.procedencia_ui)
        self.criadero.clicked.connect(self.procedencia_ui)
        self.otro_procedencia.clicked.connect(self.procedencia_ui)
        self.vendida.clicked.connect(self.final_ui)
        self.muerta.clicked.connect(self.final_ui)
        self.marcar_vacunado_c_b_c1.clicked.connect(lambda x:self.marcar_res_vacunada(self.vacunas_ciclo1_c_b))
        self.marcar_vacunado_c_b_c2.clicked.connect(lambda x:self.marcar_res_vacunada(self.vacunas_ciclo2_c_b))
        self.marcar_vacunado_aftosa_c1.clicked.connect(lambda x:self.marcar_res_vacunada(self.vacunas_ciclo1_aftosa))
        self.marcar_vacunado_aftosa_c2.clicked.connect(lambda x:self.marcar_res_vacunada(self.vacunas_ciclo2_aftosa))

        self.desmarcar_vacunado_c_b_c1.clicked.connect(lambda x:self.desmarcar_res_vacunada(self.vacunas_ciclo1_c_b))
        self.desmarcar_vacunado_c_b_c2.clicked.connect(lambda x:self.desmarcar_res_vacunada(self.vacunas_ciclo2_c_b))
        self.desmarcar_vacunado_aftosa_c1.clicked.connect(lambda x:self.desmarcar_res_vacunada(self.vacunas_ciclo1_aftosa))
        self.desmarcar_vacunado_aftosa_c2.clicked.connect(lambda x:self.desmarcar_res_vacunada(self.vacunas_ciclo2_aftosa))
        
    def procedencia_ui(self):
        self.procedencia_uis:QStackedWidget
        if self.criadero.isChecked():
            self.procedencia_uis.setCurrentIndex(0)
        if self.comprado.isChecked():
            self.procedencia_uis.setCurrentIndex(1)
        if self.otro_procedencia.isChecked():
            self.procedencia_uis.setCurrentIndex(2)

    def final_ui(self):
        if self.vendida.isChecked():
            self.final_uis.setEnabled(True)
            self.final_uis.setCurrentIndex(1)
        if self.muerta.isChecked():
            self.final_uis.setEnabled(True)
            self.final_uis.setCurrentIndex(0)

    def calendar_dlg(self):
        dlg = CalendarDialog(self)
        dlg.exec_()

    def marcar_res_vacunada(self,l:QListWidget):
        dlg = CalendarDialog(self)
        dlg.exec_()
        date = dlg.calendar.selectedDate().toString("dd/MM/yyyy")
        l.addItem(date)

    def desmarcar_res_vacunada(self,l:QListWidget):
        row = l.currentRow()
        l.takeItem(row)


    def gather_data(self):
        numero = self.numero.value()
        fdn = "" if self.fdn.date().toString("dd/MM/yyyy")=="01/01/1800" else self.fdn.date().toString("dd/MM/yyyy")
        marca = self.marca.text()
        sexo = self.sexo.currentText()
        dueno = self.dueno.currentText()
        mama = self.mama.value()
        descripcion = self.descripcion.toPlainText()
        comprado = "Si" if self.comprado.isChecked() else "No"
        precio_compra = self.comprado_precio.value()
        vendedor = self.comprado_vendedor.text()
        Fecha_compra = "" if self.comprado_fecha.date().toString("dd/MM/yyyy") == "01/01/1800" else self.comprado_fecha.date().toString("dd/MM/yyyy")
        criadero = "Si" if self.criadero.isChecked() else "No"
        procedencia_otro = "Si" if self.otro_procedencia.isChecked() else "No"
        procedencia_otro_cual = self.cual_otro_procedencia.text()
        procedencia_otro_notas = self.notas_otro_procedencia.toPlainText()
        vendida = "Si" if self.vendida.isChecked() else "No"
        vendida_comprador = self.vendida_comprador.text()
        vendida_precio = self.vendida_precio.value()
        vendida_fecha = "" if self.vendida_fecha.date().toString("dd/MM/yyyy") == "01/01/1800" else self.vendida_fecha.date().toString("dd/MM/yyyy")
        muerta = "Si" if self.muerta.isChecked() else "No"
        muerta_causa = self.muerta_causa.text()
        muerta_fecha = "" if self.muerta_fecha.date().toString("dd/MM/yyyy") == "01/01/1800" else self.muerta_fecha.date().toString("dd/MM/yyyy")
        self.vacunas_ciclo1_c_b:QListWidget
        vacunas = {
            "vacunas_c_b_c1":self.retrieve_list_data(self.vacunas_ciclo1_c_b),
            "vacunas_c_b_c2":self.retrieve_list_data(self.vacunas_ciclo2_c_b),
            "vacunas_aftosa_c1":self.retrieve_list_data(self.vacunas_ciclo1_aftosa),
            "vacunas_aftosa_c2":self.retrieve_list_data(self.vacunas_ciclo2_aftosa),
        }
        datos = {
            "numero":numero,"fdn":fdn,"marca":marca,
            "sexo":sexo,"Dueño":dueno,"mama":mama,
            "descripcion":descripcion,"comprado":comprado,
            "precio-compra":precio_compra,"vendedor":vendedor,
            "fecha-compra":Fecha_compra,"criadero":criadero,
            "procedencia-otro":procedencia_otro,
            "procedencia-otro-cual":procedencia_otro_cual,
            "procedencia-otro-notas":procedencia_otro_notas,
            "vendida":vendida,"vendida-comprador":vendida_comprador,
            "vendida-precio":vendida_precio,"vendida-fecha":vendida_fecha,
            "muerta":muerta,"muerta-causa":muerta_causa,
            "muerta-fecha":muerta_fecha,
        }
        return datos,vacunas
        
    def retrieve_list_data(self,l:QListWidget):
        rows = l.count()
        values = []
        for row in range(rows):
            values.append(l.item(row).text())
        return values
    
    def insert_record(self):
        data,vacunas = self.gather_data()
        data = list(data.values())
        con = sqlite3.connect(f"{os.getcwd()}/ganado.db")
        cursor = con.cursor()
        query = """INSERT INTO ganado VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(query, data)
        self.parent.todos_table.setModel(None)
        cattle_data = list(cursor.execute("select * from ganado"))
        headers = cursor.description
        self.parent.model = DataModel(cattle_data, headers)
        self.parent.todos_table.setModel(self.parent.model)
        for key in vacunas.keys():
            for value in vacunas[key]:
                print([data[0],key,value])
                cursor.execute("INSERT INTO vacunas VALUES(?,?,?)", [data[0],key,value])
        con.commit()
        con.close()


class Exportar(QDialog, ui_exportar.Ui_Dialog):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        self.file_btn.clicked.connect(self.pick_file)
        self.formatlist:QListWidget
        self.uilist:QStackedWidget
        self.formatlist.itemClicked.connect(lambda x: self.uilist.setCurrentIndex(self.formatlist.indexFromItem(x).row()))
    def pick_file(self):
        file, ok = QFileDialog.getSaveFileName(self, "Escoja un archivo",None, "Excel (*.xlsx);;Todos (*.*)")
        if file:
            self.file_line.setText(file)




class Window(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(f"{os.getcwd()}/ganado.db")
        self.cur = self.con.cursor()
        self.cur.execute("select * from ganado")
        data = self.cur.fetchall()
        headers = self.cur.description
        self.model = DataModel(data, headers)
        self.todos_table.setModel(self.model)
        self.exportar_btn.clicked.connect(self.export)
        self.nuevo_btn.clicked.connect(self.add)
        self.remove_btn.clicked.connect(self.remove)
        styles = Path("styles/").iterdir()
        styles = [str(os.getcwd()/style.absolute()) for style in styles]
        self.styles_combo:QComboBox
        self.styles_combo.currentTextChanged.connect(lambda x:app.setStyleSheet(Path(x).open().read()))
        self.styles_combo.insertItems(1, styles)




    def export(self):
        dlg = Exportar()
        dlg.exec_()
    def add(self):
        dlg = Tracker(self)
        dlg.exec_()

    def remove(self):
        self.todos_table:QTableView
        index = self.todos_table.currentIndex()
        if index.row()==-1:
            return
        dlg = QMessageBox.question(self, "Eliminar registros","Estás a punto de eliminar un registro, Estás seguro?")
        if dlg == QMessageBox.Yes:
            self.model.removeRows(index.row(), 1, index)
            record = index.data()
            if record is None:
                return
            query = f"DELETE FROM ganado WHERE Numero={record}"
            self.cur.execute(query)
            self.con.commit()


    def edit(self):
        pass





app = QApplication(sys.argv)
window = Window()
window.show()
app.setStyleSheet(qdarkgraystyle.load_stylesheet())
app.exec_()


