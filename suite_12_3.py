import unittest
import runner_test
import tournament_test

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tournament_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
