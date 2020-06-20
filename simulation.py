from world import World


class Simulation:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def run(self, output_filename):
        with open(self.input_filename, 'r') as input_file, \
                open(output_filename, 'w') as output_file:
            ttask = int(input_file.readline())
            umax = int(input_file.readline())
            world = World(umax=umax, ttask=ttask, verbose=True)

            # user adding phase
            for line in input_file:
                server_status = world.update(int(line.strip()))
                output_file.write(','.join(server_status) + '\n')

            # user disconnecting phase
            while not world.is_empty():
                server_status = world.update()
                output_file.write(','.join(server_status) + '\n')

            # write total cost
            output_file.write(str(world.total_cost) + '\n')


if __name__ == '__main__':
    Simulation(input_filename='test.txt').run(output_filename='out.txt')
