import unittest
from module12_2 import *


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    # @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.run1 = Runner("Usain", speed=10)
        self.run2 = Runner("Andry", speed=9)
        self.run3 = Runner("Nik", speed=3)

    def test_start1(self):
        self.race = Tournament(90, self.run1, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[2]), "Nik")

    def test_start2(self):
        self.race = Tournament(90, self.run2, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[2]), "Nik")

    def test_start3(self):
        self.race = Tournament(90, self.run1, self.run2, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[3]), "Nik")

    def tearDown(self):
        for key, value in TournamentTest.all_results.items():
            print(key, value)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)


if __name__ == '__main__':
    unittest.main()
