import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest #niewwykonuje testu
    def test_search(self):
        print(str("This is seach test").upper())

    @unittest.skip("I an skipping this test method because it is not ready") #niewykonuje testu z informacją
    def test_advancedsearch(self):
        print(str("This is advancedsearch test").upper())

    @unittest.skipIf(1==1,"number are not equals")
    def test_prepaidcharge(self):
        print(str("This is prepaidcharge test").upper())

    def test_loginbygmail(self):
        print(str("This is login by email").upper())

    def test_loginbytwitter(self):
        print(str("This is login by twitter").upper())


if __name__ == "__main__":
    unittest.main()
