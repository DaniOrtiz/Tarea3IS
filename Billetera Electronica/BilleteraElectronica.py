'''
Created on 4/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''
# -*- coding: utf-8 -*-

class BilleteraElectronica():

    def __init__(self, ID, nombres, apellidos, CI, PIN):
        self.ID = ID
        self.nombres = nombres
        self.apellidos = apellidos
        self.CI = CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.balance = 0
        
    def saldo (self):
        return(self.balance)
    
    def recargar(self, monto, fecha, identificador):
        if monto <= 0:
            raise Exception ("No se pueden recargar montos negativos") 
        else:
            recarga = (monto,fecha,identificador) 
            self.creditos.append(recarga)
            self.balance += monto 
    
    def consumir(self, monto, fecha, identificador, PIN):
        if self.PIN != PIN:
            raise Exception ("Pin Invalido")
        else: 
            if monto > self.balance:
                raise Exception ("Saldo Insuficiente") 
            else:
                consumo = (monto,fecha,identificador)
                self.debitos.append(consumo)
                self.balance -= monto
        
    