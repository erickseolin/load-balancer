from .user_connection import UserConnection


class Server:
    def __init__(self, umax, ttask):
        self.umax = umax
        self.ttask = ttask
        self.connections = []
        self.ttl = 0

    def user_count(self):
        user_count = 0
        for conn in self.connections:
            user_count += conn.user_count
        return user_count

    def is_empty(self):
        return self.user_count() == 0

    def get_capacity(self):
        return self.umax - self.user_count()

    def add_users(self, n):
        self.connections.append(UserConnection(self.ttask, n))
        # server time to live os reseted
        self.ttl = self.ttask

    def update(self):
        live_connections = []
        for user in self.connections:
            user.ttl -= 1

            # remove finished connections
            if user.ttl > 0:
                live_connections.append(user)

        # update server time to live
        self.ttl -= 1
        self.connections = live_connections
