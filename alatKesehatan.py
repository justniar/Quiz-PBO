from db import DBConnection as mydb

class alatKesehatan:
    def __init__(self):
        self.__idalkes= None
        self.__kode_alkes= None
        self.__nama_alkes= None
        self.__harga= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "Kode Alat Kesehatan:" + self.__idalkes + "\n" + "Nama Alat Kesehatan:" + self.__nama_alkes + "\n" + "Harga:" + self.__harga
        else:
            return self.__info

    @property
    def id(self):
        return self.__idalkes
    
    @property
    def kode_alkes(self):
        return self.__kode_alkes

    @kode_alkes.setter
    def kode_alkes(self, value):
        self.__kode_alkes = value
    
    @property
    def nama_alkes(self):
        return self.__nama_alkes

    @nama_alkes.setter
    def nama_alkes(self, value):
        self.__nama_alkes = value
    
    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, value):
        self.__harga = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_alkes,self.__nama_alkes,self.__harga)
        sql="INSERT INTO alatkesehatan (kode_alkes,nama_alkes,harga) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_alkes,self.__nama_alkes,self.__harga,id)
        sql="UPDATE alatkesehatan SET kode_alkes=%s, nama_alkes=%s, harga=%s, WHERE idalkes=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateBykodealkes(self, kode_alkes):
        self.conn = mydb()
        val = (self.__kode_alkes,self.__nama_alkes,self.__harga, kode_alkes)
        sql="UPDATE alatkesehatan SET kode_alkes=%s, nama_alkes=%s, harga=%s, WHERE kode_alkes=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM alatkesehatan WHERE idalkes='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteBykodealkes(self, kode_alkes):
        self.conn = mydb()
        sql="DELETE FROM alatkesehatan WHERE kode_alkes='" + str(kode_alkes) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM alatkesehatan WHERE idalkes='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_alkes = self.result[1]                   
        self.__nama_alkes = self.result[2]                   
        self.__harga = str(self.result[3])                                    
        self.conn.disconnect
        return self.result
        
    def getBykodealkes(self, kode_alkes):
        a=str(kode_alkes)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM alatkesehatan WHERE kode_alkes='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_alkes = self.result[1]                   
            self.__nama_alkes = self.result[2]                   
            self.__harga = str(self.result[3])                                    
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_alkes = ''                  
            self.__nama_alkes = ''                  
            self.__harga = ''                                 
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM alatkesehatan"
        self.result = self.conn.findAll(sql)
        return self.result
