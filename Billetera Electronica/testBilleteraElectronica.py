'''
Created on 4/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''
# -*- coding: utf-8 -*-

import unittest
from BilleteraElectronica import *
import datetime

class TestBilleteraElectronica(unittest.TestCase):

    ###########################################################################
    #                               Casos TDD                                 #
    ###########################################################################
    
    # Caso para verificar que existe la clase Billetera Electronica
    
    def TestBilleteraElectronicaExist(self):
        BilleteraElectronica()
    
    # Caso para verificar que existe el constructor de la clase Billetera 
    # Electronica
        
    def TestConstructBEExist(self):
        BilleteraElectronica("AfJ556tY", "Nelson", "Gonzalez", 19994187, 123456)
    
    # Caso para verificar que existe el metodo saldo
    
    def TestSaldoExists(self):
        Billetera = BilleteraElectronica("76rYU0PL", "Manuel", "Pacheco", 21345227, 987654)
        Billetera.saldo()
        
    # Caso para verificar que existe la estructura creditos y el metodo recargar
    
    def TestRecargarExists(self):
        Billetera = BilleteraElectronica("356TgHJ1", "Maria", "Peres", 5617234, 187423)
        Fecha = datetime(2015, 4, 23, 8, 5)
        Billetera.recargar(12000, Fecha, "981yHJ32")
    
    # Caso para verificar que existe la estructura debitos y el metodo consumir
    
    def TestConsumirExists(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        Fecha = datetime (2009, 8, 30, 3, 25)
        Billetera.consumir(5000, Fecha, "HOk234t1", 663312)
        
    # Caso para verificar que la recarga se haga efectivamente 
       
    def TestRecargaCorrect(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        Fecha = datetime (2009, 8, 30, 3, 25)
        Billetera.recargar(5000, Fecha, "HOk234t1")
        self.assertEqual(Billetera.saldo(), 5000, "Saldo Incorrecto")
    
    # Caso para verificar que el consumo se haga efectivamente
        
    def TestConsumirCorrect(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        Fecha = datetime (2009, 8, 30, 3, 25)
        Billetera.recargar(5000, Fecha, "HOk234t1")
        SaldoAnterior = Billetera.saldo()
        Billetera.consumir(500, Fecha, "HOk234t1", 663312)
        self.assertEqual(Billetera.saldo(), SaldoAnterior - 500, "Saldo Incorrecto")
        
    # Caso nombres y apellidos en castellano
    
    #def TestNamesInCatilian(self):
    #    BilleteraElectronica("fj459gjd", "�����'�����", "������-�����", 12345678, 123456)
    
    # Caso para verificar que se calcula el saldo correctamente
    
    def TestSaldoCorrect(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        self.assertEqual(Billetera.saldo(), 0)
           
    ###########################################################################
    #               Casos Fronteras, Esquinas y Malicia                       #
    ###########################################################################
    
    def TestRecargaNegative(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        Fecha = datetime (2009, 8, 30, 3, 25)
        self.assertRaises(Exception, Billetera.recargar, -5000, Fecha, "HOk234t1" )
        
    def TestConsumoInvalid(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        Fecha = datetime (2009, 8, 30, 3, 25)
        Billetera.recargar(100, Fecha, "HOk234t1")
        self.assertRaises(Exception, Billetera.consumir, 500, Fecha, "HOk234t1", 663312)
        
    def TestPINInvalid(self):
        Billetera = BilleteraElectronica("24Saa90j" , "Luis", "Garcia", 8226134, 663312)
        Fecha = datetime (2009, 8, 30, 3, 25)
        Billetera.recargar(100, Fecha, "HOk234t1")
        self.assertRaises(Exception, Billetera.consumir, 500, Fecha, "HOk234t1", 663312)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()