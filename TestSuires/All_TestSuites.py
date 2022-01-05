import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest


from Package2.TC_PaymentreturnTest import PeymentsReturnTest
from Package2.TC_PaymentTest import  PeymentsTest

#Get all tests from LoginTest,SignupTest,PeymentsReturnTest,PeymentsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PeymentsReturnTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PeymentsTest)

#Create test  suites
senityTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner().run(senityTestSuite)