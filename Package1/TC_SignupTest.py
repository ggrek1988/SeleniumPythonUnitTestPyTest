import unittest

class SignupTest(unittest.TestCase):

    def test_signbyEmail(self):
        print("This is sign by email test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("This is sign by facebook test")
        self.assertTrue(True)

    def test_loginbyTwitter(self):
        print("This is sign by Twitter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
