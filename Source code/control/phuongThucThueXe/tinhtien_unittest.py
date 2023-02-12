# Python code to demonstrate working of unittest 
import unittest
from Goi24h import Goi24h
import datetime
import pandas as pd
from BinhThuong import BinhThuong
class TestStringMethods(unittest.TestCase):
    """Sample test case"""

    # Setting up for the test
    def setUp(self):
        pass

    # Cleaning up after the test
    def tearDown(self):
        pass
    def test_Goi24h(self):
        # bat buoc phai doc nhu the nay, ko duoc sua, neu ko chay loi, ko hieu thi hoi Phong
        data = pd.read_csv('data_unittest_Goi24h.csv').values
        #print(data)
        count_test = data.shape[0]
        #print( "count : " ,  count_test)
        for x in range(count_test) :
            #print(data[x][ 1 : ] )
            year, month, day, hour, minute, year_end, month_end, day_end, hour_end, minute_end,k, cost = data[x][ 1 : ]
            self.assertEqual(
                Goi24h().tinhTien(datetime.datetime(year, month, day, hour, minute), datetime.datetime(year_end, month_end, day_end, hour_end, minute_end), k),
                cost)
    def test_goiBinhthuong(self):
        # bat buoc phai doc nhu the nay, ko duoc sua, neu ko chay loi, ko hieu thi hoi Phong
        data = pd.read_csv('data_unittest_Binhthuong.csv').values
        #print(data)
        count_test = data.shape[0]
        #print( "count : " ,  count_test)
        for x in range(count_test) :
            #print(data[x][ 1 : ] )
            year, month, day, hour, minute, year_end, month_end, day_end, hour_end, minute_end,k, cost = data[x][ 1 : ]
            self.assertEqual(
                BinhThuong().tinhTien(datetime.datetime(year, month, day, hour, minute), datetime.datetime(year_end, month_end, day_end, hour_end, minute_end), k),
                cost)
if __name__ == '__main__':
    TestStringMethods().test_Goi24h()
    TestStringMethods().test_goiBinhthuong() 