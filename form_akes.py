import sys
from PyQt5 import QtWidgets, uic
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from alatKesehatan import alatKesehatan # Class Mahasiswa dari mahasiswa.py

qtcreator_file  = "alatkesehatan.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowAlatkesehatan(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtKodeAlkes.returnPressed.connect(self.search_data) 
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")
        self.select_data()

    def select_data(self):
        try:
            alkes = alatKesehatan()

            # Get all 
            result = alkes.getAllData()

            self.gridAlkes.setHorizontalHeaderLabels(['ID Alkes', 'Kode Alat Kesehatan', 'Nama Alat', 'Harga'])
            self.gridAlkes.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridAlkes.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridAlkes.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode_alkes=self.txtKodeAlkes.text()           
            alkes = alatKesehatan()
            # search process
            result = alkes.getBykodealkes(kode_alkes)           
            a = alkes.affected
            if(a!=0):
                self.txtKodeAlkes.setText(alkes.kode_alkes.strip())
                self.txtNamaAlkes.setText(alkes.nama_alkes.strip())
                self.txtHargaAlkes.setText(alkes.harga.strip())
                self.btnSimpan.setText("Update")
                self.edit_mode=True
                self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
                self.btnHapus.setStyleSheet("background-color : red")
                
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtKodeAlkes.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self):
        try:
            alkes = alatKesehatan()
            kode_alkes=self.txtKodeAlkes.text()
            nama_alkes=self.txtNamaAlkes.text()
            harga=self.txtHargaAlkes.text()
                
            if(self.edit_mode==False):   
                alkes.kode_alkes = kode_alkes
                alkes.nama_alkes = nama_alkes
                alkes.harga = harga
                a = alkes.simpan()
                
                if(a>0):
                    self.messagebox("SUKSES", "Data Alat Kesehatan Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Alat Kesehatan Gagal Tersimpan")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
                
            elif(self.edit_mode==True):
                alkes.kode_alkes = kode_alkes
                alkes.nama_alkes = nama_alkes
                alkes.harga = harga
                a = alkes.updateBykodealkes(kode_alkes)
                
                if(a>0):
                    self.messagebox("SUKSES", "Data Alat Kesehatan Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Alat Kesehatan Gagal Diperbarui")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def delete_data(self):
        try:
            alkes= alatKesehatan()
            kode_alkes=self.txtKodeAlkes.text()
                       
            if(self.edit_mode==True):
                a = alkes.deleteBykodealkes(kode_alkes)
                if(a>0):
                    self.messagebox("SUKSES", "Data Alat Kesehatan Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Alat Kesehatan Gagal Dihapus")
                
                self.clear_entry() # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def clear_entry(self):
        self.txtKodeAlkes.setText("")
        self.txtNamaAlkes.setText("")
        self.txtHargaAlkes.setText("")
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
    window = WindowAlatkesehatan()
    window.show()
    window.select_data()
    sys.exit(app.exec_())