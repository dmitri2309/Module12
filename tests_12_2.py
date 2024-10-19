import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

    def __repr__(self):
        return self.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers
# runner1 = Runner("Usain", speed=10)
# runner2 = Runner("Andry", speed=9)
# runner3 = Runner("Nik", speed=3)


# race = Tournament(5, runner1, runner2, runner3)
# print(race.start())

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        runner1 = Runner("Usain", speed=10)
        runner2 = Runner("Andry", speed=9)
        runner3 = Runner("Nik", speed=3)

    # def test_start(self):
    #     race = Tournament(5, runner1, runner2, runner3)
    #     race.start()
    #     all_results = race.start

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    def test_start(self):
        race = Tournament(5, runner1, runner2, runner3)
        race.start()
        all_results = race.start