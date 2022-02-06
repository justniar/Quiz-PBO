import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from dokter import Dokter # Class Dokter dari dokter.py

qtcreator_file  = "dokter.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowDokter(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtNIK.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox spesialis
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            dk = Dokter()

            # Get all 
            result = dk.getAllData()

            self.gridDokter.setHorizontalHeaderLabels(['ID', 'NIK', 'Nama', 'Jenis Kelamin', 'Spesialis', 'Tarif'])
            self.gridDokter.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridDokter.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridDokter.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            nik=self.txtNIK.text()           
            dk = Dokter()
            # search process
            result = dk.getBynik(nik)           
            a = dk.affected
            if(a!=0):
                self.txtNIK.setText(dk.nik.strip())
                self.txtNama.setText(dk.nama.strip())
                jk = dk.jk.strip()
                if jk == "L":
                    self.optLaki.setChecked(True)
                else:
                    self.optPerempuan.setChecked(True)
                self.cboSpesialis.setCurrentText(dk.spesialis.strip())
                self.txtTarif.setText(dk.tarif.strip())
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
                
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNIK.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self):
        try:
            dk = Dokter()
            nik=self.txtNIK.text()
            nama=self.txtNama.text()
            jk = ""
            if self.optLaki.isChecked():
                jk= "L"
            if self.optPerempuan.isChecked():
                jk= "P"
                
            spesialis=self.cboSpesialis.currentText()
            tarif=self.txtTarif.text()
            if(self.edit_mode==False):   
                dk.nik = nik
                dk.nama = nama
                dk.jk = jk
                dk.spesialis = spesialis
                dk.tarif = tarif
                a = dk.simpan()
                
                if(a>0):
                    self.messagebox("SUKSES", "Data Dokter Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Dokter Gagal Tersimpan")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
                
            elif(self.edit_mode==True):
                dk.nik = nik
                dk.nama = nama
                dk.jk = jk
                dk.spesialis = spesialis
                dk.tarif = tarif
                a = dk.updateBynik(nik)
                
                if(a>0):
                    self.messagebox("SUKSES", "Data Dokter Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Dokter Gagal Diperbarui")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            dk= Dokter()
            nik=self.txtNIK.text()
                       
            if(self.edit_mode==True):
                a = dk.deleteBynik(nik)
                if(a>0):
                    self.messagebox("SUKSES", "Data Dokter Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Dokter Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtNIK.setText("")
        self.txtNama.setText("")
        
        self.cboSpesialis.setCurrentText("")
        self.txtTarif.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowDokter()
    window.show()
    window.select_data()
    sys.exit(app.exec_())