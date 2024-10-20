import unittest
import tests_12_3


run_test = unittest.TestSuite()

run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_test)
