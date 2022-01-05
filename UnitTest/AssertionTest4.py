import unittest

class AssertionTest(unittest.TestCase):


    def TestName(self):
        list = ("python","selenium","java")
        #self.assertIn("python",list)
        self.assertNotIn("ruby",list)



if __name__ == "__main__":
    unittest.main()
