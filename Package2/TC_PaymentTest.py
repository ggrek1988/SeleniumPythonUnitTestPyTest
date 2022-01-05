import unittest

class PeymentsTest(unittest.TestCase):

    def test_peymentiondollar(self):
        print("This is peyment in dollar test")
        self.assertTrue(True)

    def test_peymentionruppes(self):
        print("This is peyment in Ruppes test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
