from load_balancing import LoadBalancer, Cluster


class World:
    SERVER_COST = 1

    def __init__(self, umax, ttask, verbose=False):
        self.total_cost = 0
        self.load_balancer = LoadBalancer(
            Cluster(umax=umax, ttask=ttask, server_cost=self.SERVER_COST))
        self.verbose = verbose

    def is_empty(self):
        return self.load_balancer.cluster.is_empty()

    def update(self, new_conn=0):
        self.load_balancer.cluster.update()
        if new_conn:
            self.load_balancer.add_users(new_conn)
        self.total_cost += self.load_balancer.cluster.get_cost()
        server_status = self.load_balancer.cluster.get_status()

        if self.verbose:
            print(','.join(server_status))

        return server_status

    def run(self, connections):
        for connection in connections:
            self.update(connection)

        while not self.is_empty():
            self.update()

        if self.verbose:
            print('custo:', self.total_cost)
