import unittest
import tests_12_2
import tests_12_1

run_test = unittest.TestSuite()

run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_test)
