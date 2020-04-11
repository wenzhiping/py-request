#coding:utf-8
import requests
import unittest
import os, sys
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parentdir)
from  db_fixture import test_data
class test(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/add_guest/'
    def tearDown(self):
        return self.result
    def test_add_guest_nomal(self):
        params = {'eid':1 ,
        'realname' :'jktest',
        'phone':111119,
        'email':'111119@mail.com'
         }
        r = requests.post(self.url,data=params)
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'add guest success')
if __name__ == '__main__':
    # test_data.init_data()
    unittest.main()

# url = 'http://127.0.0.1:8000/api/add_guest/'
# params = {'eid':1,
# 'realname' :'jktest',
# 'phone':111119,
# 'email':'111119@mail.com'
#  }
# r = requests.post(url,params).json()
# unittest.assertEqual(r['stayus'],200)
# print(type(r),r)
