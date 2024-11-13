import unittest

import runner_and_tournament


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        walk = runner_and_tournament.Runner('Walker')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    @skip_if_frozen
    def test_run(self):
        run = runner_and_tournament.Runner('Runner')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        walk2 = runner_and_tournament.Runner('Walker_2')
        run2 = runner_and_tournament.Runner('Runner_2')
        for i in range(10):
            walk2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walk2.distance)


if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.run_1 = runner_and_tournament.Runner('Усейн', 10)
        self.run_2 = runner_and_tournament.Runner('Андрей', 9)
        self.run_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            results = {}
            for place, runner in result.items():
                results[place] = runner.name
            print(results)

    @skip_if_frozen
    def test_run_1(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.run_1, self.run_3)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @skip_if_frozen
    def test_run_2(self):
        self.tournament_2 = runner_and_tournament.Tournament(90, self.run_2, self.run_3)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @skip_if_frozen
    def test_run_3(self):
        self.tournament_3 = runner_and_tournament.Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()
