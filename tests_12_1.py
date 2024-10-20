from module12_1 import *
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walking = Runner('Peter')
        for i in range(9):
            walking.walk()
        self.assertEqual(walking.walk(), 50)

    def test_run(self):
        running = Runner('Peter')
        for i in range(9):
            running.run()
        self.assertEqual(running.run(), 100)

    def test_challange(self):
        walking = Runner('Peter')
        running = Runner('Peter')
        for i in range(9):
            walking.walk()
            running.run()
        self.assertNotEqual((walking.walk(), running.run()), 100)


if __name__ == '__main__':
    unittest.main()
