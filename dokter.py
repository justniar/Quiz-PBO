from db import DBConnection as mydb

class Dokter:
    def __init__(self):
        self.__iddokter= None
        self.__nik= None
        self.__nama= None
        self.__jk= None
        self.__spesialis= None
        self.__tarif=None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "NIK:" + self.__nik + "\n" + "Nama:" + self.__nama + "\n" + "Jenis Kelamin" + self.__jk + "\n" + "Spesialis:" + self.__spesialis + "\n" + "Tarif:" + self.__tarif
        else:
            return self.__info

    @property
    def id(self):
        return self.__iddokter
    
    @property
    def nik(self):
        return self.__nik

    @nik.setter
    def nik(self, value):
        self.__nik = value
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value
    
    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value
    
    @property
    def spesialis(self):
        return self.__spesialis

    @spesialis.setter
    def spesialis(self, value):
        self.__spesialis = value
    
    @property
    def tarif(self):
        return self.__tarif

    @tarif.setter
    def tarif(self, value):
        self.__tarif = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__nik,self.__nama,self.__jk,self.__spesialis,self.__tarif)
        sql="INSERT INTO dokter (nik,nama,jk,spesialis,tarif) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__nik,self.__nama,self.__jk,self.__spesialis,self.__tarif, id)
        sql="UPDATE dokter SET nik=%s, nama=%s, jk=%s, spesialis=%s, tarif=%s WHERE iddokter=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateBynik(self, nik):
        self.conn = mydb()
        val = (self.__nik,self.__nama,self.__jk,self.__spesialis,self.__tarif, nik)
        sql="UPDATE dokter SET nik=%s, nama=%s, jk=%s, spesialis=%s, tarif=%s WHERE nik=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM dokter WHERE iddokter='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteBynik(self, nik):
        self.conn = mydb()
        sql="DELETE FROM dokter WHERE nik='" + str(nik) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM dokter WHERE iddokter='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nik = self.result[1]                   
        self.__nama = self.result[2]                   
        self.__jk = str(self.result[3])                   
        self.__spesialis = self.result[4]    
        self.__tarif = str(self.result[5])               
        self.conn.disconnect
        return self.result
        
    def getBynik(self, nik):
        a=str(nik)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM dokter WHERE nik='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nik = self.result[1]                   
            self.__nama = self.result[2]                   
            self.__jk = str(self.result[3])                   
            self.__spesialis = self.result[4]    
            self.__tarif = str(self.result[5])                 
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nik = ''                  
            self.__nama = ''                  
            self.__jk = ''                  
            self.__spesialis = '' 
            self.__tarif = ''                  
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dokter"
        self.result = self.conn.findAll(sql)
        return self.result

