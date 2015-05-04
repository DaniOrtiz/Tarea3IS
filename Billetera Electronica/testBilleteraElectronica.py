'''
Created on 4/5/2015

@author: Daniela Ortiz (10-10517)
         Maria Lourdes Garcia (10-10264)
'''
import unittest
from BilleteraElectronica import *
import BilleteraElectronica


class TestBilleteraElectronicaExists(unittest.TestCase):

    def testBilleteraElectronicaExists(self):
        BilleteraElectronica(111111111, Maria, Lopez, 9345678, 111111)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()