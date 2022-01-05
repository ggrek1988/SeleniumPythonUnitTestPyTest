import unittest
#setup - wykonywana przed kazdą fukcją test case
#teardown - wykonywana jest po pozytywnym zakonczeniu kazdego test casea
#setUpClass - wywoływana raz przed wykonaniem wszystkich testów
#teraDownClass - wywoływana raz po wykonaniu wszystkich testów
#setUpModule() - wywołana jest przed kazdą classą i test case
#tearDownModule() - wywołana jest po zakonczeniu kazdej klasy i test case

def setUpModule():
    print("setUpModule()")

def tearDownModule():
    print("tearDownModule()")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        print("This in login TEST")

    @classmethod
    def tearDown(self) -> None:
        print("This is logout TEST")

    @classmethod
    def setUpClass(cls) -> None:
        print("Open Application")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Close Application")

    def test_search(self):
        print(str("This is seach test").upper())


    def test_advancedsearch(self):
        print(str("This is advancedsearch test").upper())


if __name__ == "__main__":
    unittest.main()
