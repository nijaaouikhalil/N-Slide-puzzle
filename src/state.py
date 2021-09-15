from math import sqrt


class State:

    # Constructor - Take in tuple and generate list of nodes for initial state
    def __init__(self, state):
        self.initial_state = state
        self.dimension = int(sqrt(len(state) + 1))
        self.total_nodes = (len(state))
        self.goal = list(range(1, self.total_nodes + 1))

    # To String override (prints a state)
    def __str__(self):
        s = ""
        for i in range(len(self.initial_state)):
            if i % self.dimension == 0 and i != 0:
                s += "\n"
            s += str(self.initial_state[i]) + "\t"
        return s

    # Returns list of possible moves given a node
    def get_moves(self, node):
        # any given tile can only move by 1 or n
        possible_moves = [1, -1, self.dimension, -self.dimension]
        valid_moves = []

        # iterate over possible moves and determine which ones are valid given current node position
        for move in possible_moves:
            if 0 <= node + move < self.total_nodes:
                if move == 1 and node in range(self.dimension - 1, self.total_nodes, self.dimension):
                    continue
                if move == -1 and node in range(0, self.total_nodes, self.dimension):
                    continue
                valid_moves.append(move)
        return valid_moves

    # Returns list of possible states
    def expand(self, state):
        # retrieve all possible moves for each node
        possible_states = []
        for position in range(self.total_nodes):
            possible_moves = self.get_moves(position)
            for move in possible_moves:
                new_state = state[:]
                (new_state[position + move], new_state[position]) = (new_state[position], new_state[position + move])
                possible_states.append(new_state)
        return possible_states
