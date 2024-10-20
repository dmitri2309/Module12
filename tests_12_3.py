import unittest
from module12_1 import *
from module12_2 import *


# class Runner:
#     def __init__(self, name, speed=5):
#         self.name = name
#         self.distance = 0
#         self.speed = speed
#
#     def run(self):
#         self.distance += self.speed * 2
#         return self.distance

#
#     def walk(self):
#         self.distance += self.speed
#         return self.distance
#
#     def __str__(self):
#         return self.name
#
#     def __eq__(self, other):
#         if isinstance(other, str):
#             return self.name == other
#         elif isinstance(other, Runner):
#             return self.name == other.name
#
#     def __repr__(self):
#         return self.name
#
#
# class Tournament:
#     def __init__(self, distance, *participants):
#         self.full_distance = distance
#         self.participants = list(participants)
#
#     def start(self):
#         finishers = {}
#         place = 1
#         while self.participants:
#             for participant in self.participants:
#                 participant.run()
#                 if participant.distance >= self.full_distance:
#                     finishers[place] = participant
#                     place += 1
#                     self.participants.remove(participant)
#         return finishers

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walking = Runner('Peter')
        for i in range(9):
            walking.walk()
        self.assertEqual(walking.walk(), 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        running = Runner('Peter')
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
    def test1_start(self):
        self.race = Tournament(5, self.run1, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[2]), "Nik")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test2_start(self):
        self.race = Tournament(5, self.run2, self.run3)
        res = self.race.start()
        TournamentTest.all_results.update(res)
        self.assertIs(str(TournamentTest.all_results[2]), "Nik")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test3_start(self):
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
