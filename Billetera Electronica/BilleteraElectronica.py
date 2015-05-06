'''
Created on 4/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''
class BilleteraElectronica(object):

    def __init__(self, nombres, apellidos, CI, PIN):
        self.nombres = nombres
        self.apellidos = apellidos
        self.CI = CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.saldo = 0
        
    def recargas(self, monto, fecha, identificador):
        recarga = (monto,fecha,identificador) 
        self.creditos.append(recarga)
        self.saldo += monto
        
    def consumos(self, monto, fecha, identificador):
        if monto > self.saldo:
            raise Exception("saldo insuficiente")
        else: 
            consumo = (monto,fecha,identificador)
            self.debitos.append(consumo)
            self.saldo -= monto
        
        
    def saldo(self,recargas):
    #   self.balance = balance
    
    def recargar(self):
    
    def consumir(self):