import unittest
import module12_1
from module12_2 import *


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walking = module12_1.Runner('Peter')
        for i in range(9):
            walking.walk()
        self.assertEqual(walking.walk(), 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        running = module12_1.Runner('Peter')
        for i in range(9):
            running.run()
        self.assertEqual(running.run(), 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challange(self):
        walking = Runner('Peter')
        running = Runner('Peter')
        for i in range(9):
            walking.walk()
            running.run()
        self.assertNotEqual((walking.walk(), running.run()), 100)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = Runner("Usain", speed=10)
        self.run2 = Runner("Andry", speed=9)
        self.run3 = Runner("Nik", speed=3)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_start1(self):
        self.race = Tournament(5, self.run1, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[2]), "Nik")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_start2(self):
        self.race = Tournament(5, self.run2, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[2]), "Nik")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_start3(self):
        self.race = Tournament(5, self.run1, self.run2, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[3]), "Nik")

    def tearDown(self):
        print(TournamentTest.all_results)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)


if __name__ == '__main__':
    unittest.main()
