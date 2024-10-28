import logging
from module12_4 import *
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_test.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            first = Runner('Вася', -5)
            for _ in range(10):
                first.walk()
            self.assertEqual(first.distance, 50, f"{first.name} должен пробежать 50, а пробежал {first.distance}")
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=exc)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            second = Runner(1, 5)
            for _ in range(10):
                second.run()
            self.assertEqual(second.distance, 100, f"{second.name} должен пробежать 50, а пробежал {second.distance}")
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=exc)
