import unittest
from world import World


class CostEfficiencyTest(unittest.TestCase):
    """Test the cost efficiency of the LoadBalancer."""

    def test_case_1(self):
        world = World(umax=4, ttask=5)
        world.run([1, 5, 2, 3, 2, 3])
        self.assertEqual(28, world.total_cost)
        # the better cost is actually 24

    def test_case_2(self):
        world = World(umax=4, ttask=5)
        world.run([3, 2, 3, 2, 5, 1])
        self.assertEqual(24, world.total_cost)

    def test_case_3(self):
        world = World(umax=4, ttask=3)
        world.run([3, 2, 3])
        self.assertEqual(8, world.total_cost)

    def test_case_4(self):
        world = World(umax=4, ttask=2)
        world.run([3, 2])
        self.assertEqual(5, world.total_cost)
        # the better cost is actually 4

    def test_case_5(self):
        world = World(umax=2, ttask=4)
        world.run([1, 3, 0, 1, 0, 1])
        self.assertEqual(15, world.total_cost)

    def test_case_6(self):
        world = World(umax=10, ttask=10)
        world.run([20, 25, 40, 100, 15, 12])
        self.assertEqual(223, world.total_cost)


if __name__ == '__main__':
    unittest.main()
