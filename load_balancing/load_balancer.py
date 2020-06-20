class LoadBalancer:
    """Load balancer for user connection distribution.

    Args:
        cluster: The Cluster this LoadBalancer will use to add new servers and
            distribute connections.
    """

    def __init__(self, cluster):
        self.cluster = cluster

    @property
    def total_capacity(self):
        """Return the total user capacity in the availble servers."""
        total_capacity = 0
        for server in self.cluster.servers:
            total_capacity += server.get_capacity()
        return total_capacity

    def _add_to_server(self, server, n):
        """Add n users to a given server.

        The maximum number of users possible will be added to the server, it is
            not guaranted that all the n can be added.

        Args:
            server: The Server to add the users to.
            n: The number of users to add.

        Returns:
            The number of users that were added to the server.
        """
        capacity = server.get_capacity()
        connected_users = 0
        if capacity:
            connected_users = min(capacity, n)
            server.add_users(connected_users)

        return connected_users

    def add_users(self, n):
        """Add n users to the cluster managed by this LoadBalancer.

        Args:
            n: The number of users to add.
        """
        if n <= 0:
            return

        # filter available servers
        available_servers = [
            server for server in self.cluster.servers if server.get_capacity()]

        # TODO keep servers sorted
        # get servers sorted by time to live
        sorted_servers = sorted(
            available_servers, key=lambda server: server.ttl)

        total_capacity = self.total_capacity
        index = 0
        while total_capacity > 0 and n > 0:
            curr_server = sorted_servers[index]
            # Add users to older server if possible to use all its capacity,
            #   else add to older ones.
            # This makes possible to finish older servers earlier in some
            # cases.
            if ((n >= curr_server.get_capacity()) or
                    index == len(sorted_servers) - 1):
                connected_users = self._add_to_server(curr_server, n)
                n -= connected_users
                total_capacity -= connected_users

            index = (index + 1) % len(sorted_servers)

        # need more servers
        while n > 0:
            new_server = self.cluster.add_server()
            connected_users = self._add_to_server(new_server, n)
            n -= connected_users
