import unittest
from load_balancing import LoadBalancer, Cluster


class LoadBalancerTest(unittest.TestCase):
    """Test the LoadBalancer class methods."""

    def setUp(self):
        self.lb = LoadBalancer(Cluster(
            umax=1, ttask=1, server_cost=1))

    def test_total_capacity_method(self):
        server_max_capacity = 5
        self.lb.cluster.umax = server_max_capacity

        # initial capacity should be zero
        self.assertEqual(0, self.lb.total_capacity)

        # adding a new server the capacity should be the max capacity of the
        #   server
        self.lb.cluster.add_server()
        self.assertEqual(server_max_capacity, self.lb.total_capacity)

        self.lb.cluster.add_server()
        self.lb.cluster.add_server()
        self.assertEqual(3*server_max_capacity, self.lb.total_capacity)

        # removing servers should lower capacity
        del self.lb.cluster.servers[0]
        self.assertEqual(2*server_max_capacity, self.lb.total_capacity)

        # adding users to server should lower its capacity (if no new servers
        #   are created)
        self.lb.add_users(7)
        self.assertEqual(2*server_max_capacity-7, self.lb.total_capacity)

    def test_add_users_method(self):
        with self.subTest('Test zero users added'):
            self.lb.add_users(0)
            # no servers should be created
            self.assertTrue(self.lb.cluster.is_empty())

        with self.subTest('Test negative number of users added'):
            self.lb.add_users(-10)
            # nothing should happen
            self.assertTrue(self.lb.cluster.is_empty())
