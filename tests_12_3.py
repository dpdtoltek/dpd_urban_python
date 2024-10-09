import runner
import runner_and_tournament as rat
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        self.name = runner.Runner('Ben')
        for i in range(10):
            self.name.walk()
        self.assertEqual(self.name.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        self.name = runner.Runner('John')
        for i in range(10):
            self.name.run()
        self.assertEqual(self.name.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        self.name1 = runner.Runner('Eva')
        self.name2 = runner.Runner('Mary')
        for i in range(10):
            self.name1.run()
            self.name2.walk()
        self.assertNotEqual(self.name1.distance, self.name2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        all_res = [cls.all_results.get(result) for result in cls.all_results]
        for i in all_res:
            for key, value in i.items():
                i[key] = value.name
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start1(self):
        self.tournament1 = rat.Tournament(90, self.runner1, self.runner3)
        result1 = self.tournament1.start()
        TournamentTest.all_results['test_start1'] = result1
        last = result1[max(result1)]
        self.assertTrue(last == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start2(self):
        self.tournament2 = rat.Tournament(90, self.runner2, self.runner3)
        result2 = self.tournament2.start()
        TournamentTest.all_results['test_start2'] = result2
        last = result2[max(result2)]
        self.assertTrue(last == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start3(self):
        self.tournament3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        result3 = self.tournament3.start()
        TournamentTest.all_results['test_start3'] = result3
        last = result3[max(result3)]
        self.assertTrue(last == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start4(self):
        self.tournament4 = rat.Tournament(6,  self.runner3, self.runner2, self.runner1)
        result4 = self.tournament4.start()
        TournamentTest.all_results['test_start4'] = result4
        last = result4[max(result4)]
        self.assertTrue(last == 'Ник', 'Последний не Ник.')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start5(self):
        self.tournament5 = rat.Tournament(18,  self.runner2, self.runner1)
        result5 = self.tournament5.start()
        TournamentTest.all_results['test_start5'] = result5
        last = result5[max(result5)]
        self.assertTrue(last == 'Андрей', 'Последний не Андрей.')


if __name__ == '__main__':
    RunnerTest()
    TournamentTest()
