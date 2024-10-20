import logging
from module12_4 import *
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            walking = Runner('Peter')
            for i in range(9):
                walking.walk()
            self.assertEqual(walking.walk(), 50)
        except:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            running = Runner('Peter')
            for i in range(9):
                running.run()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(running.run(), 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challange(self):
        walking = Runner('Peter')
        running = Runner('Peter')
        for i in range(9):
            walking.walk()
            running.run()
        self.assertNotEqual((walking.walk(), running.run()), 100)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_test.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
