from state import State
from scipy.spatial.distance import hamming


# Depth First Search Class
class DepthFirstSearch:

    # Constructor
    def __init__(self, puzzle):
        self.state = State(puzzle)
        self.solution_path = 0
        self.cost_path = 0
        self.explored = []

    # Search function
    def search(self):
        # initialize a stack to hold our nodes
        stack = [self.state.initial_state]

        # while stack exists, keep investigating new nodes
        while stack:
            node = stack.pop()

            print(node)

            # if goal state reached, return true
            if node == self.state.goal:
                print("Solved by DFS! Final State: " + str(node))
                return True

            self.solution_path += 1

            # if node isn't goal state, expand node and add unexplored nodes to stack
            for state in self.state.expand(node):
                self.cost_path += 1
                if state not in self.explored:
                    stack.append(state)
                    self.explored.append(state)
        return False


# Iterative Deepening Class
class IterativeDeepening:

    # Constructor
    def __init__(self, puzzle, max_depth):
        self.state = State(puzzle)
        self.solution_path = 0
        self.cost_path = 0
        self.max_depth = max_depth

    # Utility function to recursively perform a depth-limited search of a node
    def depth_limited_search(self, node, max_depth):

        print(node)

        # if node is goal, return true
        if node == self.state.goal:
            print("Solved by Iterative Deepening! Final State: " + str(node))
            return True

        # if max depth is reached, we stop checking new nodes
        if max_depth <= 0:
            return False

        self.solution_path += 1

        # finally, we expand the current node and recursively call this function (with depth decremented by 1)
        for state in self.state.expand(node):
            self.cost_path += 1
            if self.depth_limited_search(state, max_depth - 1):
                return True
        return False

    # Search function
    def search(self):
        # for loop to go through each level of the given maximum depth (i.e. 1 ... max_depth)
        for i in range(self.max_depth):
            # call depth limited search on a node, return true if goal is reached
            if self.depth_limited_search(self.state.initial_state, i):
                return True
        return False


# Hamming Distance Class: A* Search with Heuristic H1
class HammingDistance:

    # Constructor
    def __init__(self, puzzle):
        self.state = State(puzzle)
        self.explored = []
        self.hamming_distance = []
        self.solution_path = 0
        self.cost_path = 0

    # Uses hamming() function to return hamming distance between goal and current node
    def get_hamming_distance(self, node):
        return hamming(node, self.state.goal) * len(node)

    # Search function
    def search(self):
        # initialize a stack to hold our nodes
        stack = [self.state.initial_state]

        while stack:
            # sort the stack by hamming distance (lowest to the top)
            stack = sorted(stack, key=lambda x: self.get_hamming_distance(x), reverse=True)

            # pop the node with lowest hamming, add it to explored
            node = stack.pop()
            self.explored.append(node)
            print(node)

            # if node is goal, return true
            if node == self.state.goal:
                print("Solved by Hamming! Final State: " + str(node))
                return True

            self.solution_path += 1

            # else, we expand the node and keep searching
            for state in self.state.expand(node):
                self.cost_path += 1
                if state not in self.explored:
                    stack.append(state)
                    self.explored.append(node)
        return False


# Manhattan Distance Class: A* search with Heuristic H2
class ManhattanDistance:

    # Constructor
    def __init__(self, puzzle):
        self.state = State(puzzle)
        self.explored = []
        self.solution_path = 0
        self.cost_path = 0

    # Utility function to compute manhattan distance between goal state and current node
    def get_manhattan_distance(self, node):
        distance = 0
        for position in node:
            goal_distance = abs(self.state.goal.index(position) - node.index(position))
            (up, down) = (goal_distance // self.state.dimension, goal_distance % self.state.dimension)
            distance += up + down
        return distance

    # Search function
    def search(self):
        # initialize stack with initial state
        stack = [self.state.initial_state]

        # search while stack exists
        while stack:
            # sort the stack by lowest Manhattan Distance
            stack = sorted(stack, key=lambda x: self.get_manhattan_distance(x), reverse=True)

            # pop the node with the lowest Manhattan Distance, add to explored nodes
            node = stack.pop()
            self.explored.append(node)
            print(node)

            # if goal is reached, we return true
            if node == self.state.goal:
                print("Solved by Manhattan! Final State: " + str(node))
                return True

            self.solution_path += 1

            # else, we keep searching and expand the node
            for state in self.state.expand(node):
                self.cost_path += 1
                if state not in self.explored:
                    stack.append(state)
                    self.explored.append(node)
        return False
