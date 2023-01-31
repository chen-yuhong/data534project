import unittest
from test_apra import TestAPRA


def my_suite():
    
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(unittest.makeSuite(TestAPRA))
    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
