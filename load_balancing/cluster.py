from .server import Server


class Cluster:
    def __init__(self, umax, ttask, server_cost):
        self.umax = umax
        self.ttask = ttask
        self.server_cost = server_cost
        self.servers = []

    def server_count(self):
        return len(self.servers)

    def get_cost(self):
        return self.server_cost * self.server_count()

    def is_empty(self):
        return self.server_count() == 0

    def add_server(self):
        new_server = Server(self.umax, self.ttask)
        self.servers.append(new_server)
        return new_server

    def update(self):
        live_servers = []
        for server in self.servers:
            server.update()
            if not server.is_empty():
                live_servers.append(server)

        self.servers = live_servers

    def get_status(self):
        if self.is_empty():
            server_status = ['0']
        else:
            server_status = [str(server.user_count())
                             for server in self.servers]

        return server_status

# TODO test 0 connections
