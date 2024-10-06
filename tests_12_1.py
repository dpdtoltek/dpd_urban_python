import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.name = runner.Runner('Ben')
        for i in range(10):
            self.name.walk()
        self.assertEqual(self.name.distance, 50)

    def test_run(self):
        self.name = runner.Runner('John')
        for i in range(10):
            self.name.run()
        self.assertEqual(self.name.distance, 100)

    def test_challenge(self):
        self.name1 = runner.Runner('Eva')
        self.name2 = runner.Runner('Mary')
        for i in range(10):
            self.name1.run()
        for j in range(10):
            self.name2.walk()
        # self.distance1 = (self.name1.run() for i in range(10))
        # self.distance2 = (self.name2.walk() for i in range(10))
        self.assertNotEqual(self.name1.distance, self.name2.distance)


if __name__ == '__main__':
    RunnerTest()
