import logging
import module12_4
import unittest

# logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_test.log", encoding="UTF-8",
#                         format="%(asctime)s | %(levelname)s | %(message)s")

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO, filemode="a", filename="runner_test.log", encoding="UTF-8",
#                         format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        #first = Runner('Вася', -5)
        first = module12_4.Runner('Вася', -5)
        try:
            #first = module12_4.Runner('Вася', -5)
            for i in range(10):
                first.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(first.distance, 50)
        except:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        #second = Runner(1, 5)
        second = module12_4.Runner(1, 5)
        try:
            #second = module12_4.Runner(1, 5)
            #running = Runner('Peter')
            for i in range(10):
                second.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(second.distance, 100)
        except:
            logging.warning("Неверный тип данных для объекта Runner")

    # @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    # def test_challange(self):
    #     walking = Runner('Peter')
    #     running = Runner('Peter')
    #     for i in range(9):
    #         walking.walk()
    #         running.run()
    #     self.assertNotEqual((walking.walk(), running.run()), 100)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="a", filename="runner_test.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()
