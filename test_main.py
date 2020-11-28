import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_func_exists(self) :
        self.assertTrue( "quadratic" in globals(), "No function called quadratic has been defined" )
        
    def test_func_return(self) :
        xv = np.linspace(-10,10,500)
        myarr = quadratic( xv,1, 1, 1 )
        self.assertTrue( len(myarr)==500, "The quadratic function should return an np.array that has the same length as the input xvals input np array" )
        
    def test_func_works(self) :
        xv = np.linspace(-10,10,500)
        for i in range(5) :
            a, b, c = np.random.randint(-10,10), np.random.randint(-10,10), np.random.randint(-10,10)
            quad = quadratic( xv, a, b, c )
            for j in range(len(quad)) : 
                yv = a*xv[j]*xv[j] + b*xv[j] + c
                self.assertTrue( np.abs(yv-quad[j])<1e-7, "The quadratic function does not seem to calculate the quadratic correctly" )
