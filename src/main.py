from algorithms import DepthFirstSearch, IterativeDeepening, HammingDistance, ManhattanDistance
from utils import TimeAnalyzer, import_input, timeout


# Function to take tuple input and convert it into a list
def tuple_to_list(tup):
    puzzle_list = []
    for t in tup:
        puzzle_list.extend(list(t))
    return puzzle_list


def depth_first_search(input_filename, output_filename, timeout_seconds):
    output_path = "../results/"
    output_filename = output_filename + ".txt"
    f = open(output_path+output_filename, "w+")
    f.truncate(0)

    total_puzzles = 0
    sum_duration = 0
    sum_length = 0
    sum_cost = 0
    sum_no_solution = 0

    for index, puzzle in enumerate(import_input(input_filename)):
        total_puzzles += 1

        time_tracker = TimeAnalyzer()
        dfs = DepthFirstSearch(tuple_to_list(puzzle))
        time_tracker.start_timer()
        found = False
        with timeout(timeout_seconds):
            found = dfs.search()
        time_tracker.end_timer()
        f.write("------Puzzle " + str(index + 1) + "------" + "\n")
        if found:
            f.write("Solution found \n")

            sum_duration += time_tracker.get_duration()
            f.write("Time to solve: " + str(time_tracker.get_duration()) + " seconds \n")

            sum_length += dfs.solution_path
            f.write("Length of dfs: " + str(dfs.solution_path) + "\n")

            sum_cost += dfs.cost_path
            f.write("Cost of solution: " + str(dfs.cost_path) + "\n")

            optimality = (dfs.solution_path/dfs.cost_path)*100
            f.write("Optimality of solution: " + str(f"{optimality:.2f}") + "% " + "\n\n")
        else:
            sum_no_solution += 1
            f.write("No solution found \n")
            f.write("Time elapsed: " + str(time_tracker.get_duration()) + " seconds \n\n")

    if total_puzzles == sum_no_solution:
        average_execution_time = 0
        average_length = 0
        average_cost = 0
        average_no_solution = 100
    else:
        average_execution_time = sum_duration / (total_puzzles - sum_no_solution)
        average_length = sum_length / (total_puzzles - sum_no_solution)
        average_cost = sum_cost / (total_puzzles - sum_no_solution)
        average_no_solution = (sum_no_solution / total_puzzles) * 100

    f.write("\n ------Analysis------" + "\n")
    f.write("Total solution length: " + str(sum_length) + "\n")
    f.write("Average solution length: " + str(f"{average_length:.2f}") + "\n")
    f.write("Total solution cost: " + str(sum_cost) + "\n")
    f.write("Average solution cost: " + str(f"{average_cost:.2f}") + "\n")
    f.write("Average execution time: " + f"{average_execution_time:.2f}" + " seconds \n")
    f.write("Total no solution: " + str(sum_no_solution) + "\n")
    f.write("Average no solution: " + str(f"{average_no_solution:.2f}") + "% \n")


def iterative_deep(input_filename, output_filename, timeout_seconds):
    max_depth = 7
    output_path = "../results/"
    output_filename = output_filename + ".txt"
    f = open(output_path+output_filename, "w+")
    f.truncate(0)

    total_puzzles = 0
    sum_duration = 0
    sum_length = 0
    sum_cost = 0
    sum_no_solution = 0

    for index, puzzle in enumerate(import_input(input_filename)):
        total_puzzles += 1

        time_tracker = TimeAnalyzer()
        iterative_deepening = IterativeDeepening(tuple_to_list(puzzle), max_depth)
        time_tracker.start_timer()
        found = False
        with timeout(timeout_seconds):
            found = iterative_deepening.search()
        time_tracker.end_timer()
        f.write("------Puzzle " + str(index + 1) + "------" + "\n")
        if found:
            f.write("Solution found with max depth of: " + str(max_depth) + "\n")

            sum_duration += time_tracker.get_duration()
            f.write("Time to solve: " + str(time_tracker.get_duration()) + " seconds \n")

            sum_length += iterative_deepening.solution_path
            f.write("Length of iterative deepening: " + str(iterative_deepening.solution_path) + "\n")

            sum_cost += iterative_deepening.cost_path
            f.write("Cost of solution: " + str(iterative_deepening.cost_path) + "\n")

            optimality = (iterative_deepening.solution_path/iterative_deepening.cost_path)*100
            f.write("Optimality of solution: " + str(f"{optimality:.2f}") + "% " + "\n\n")
        else:
            sum_no_solution += 1
            f.write("No solution found with max depth of: " + str(max_depth) + "\n")
            f.write("Time elapsed: " + str(time_tracker.get_duration()) + " seconds \n\n")

    if total_puzzles == sum_no_solution:
        average_execution_time = 0
        average_length = 0
        average_cost = 0
        average_no_solution = 100
    else:
        average_execution_time = sum_duration / (total_puzzles - sum_no_solution)
        average_length = sum_length / (total_puzzles - sum_no_solution)
        average_cost = sum_cost / (total_puzzles - sum_no_solution)
        average_no_solution = (sum_no_solution / total_puzzles) * 100

    f.write("\n ------Analysis------" + "\n")
    f.write("Total solution length: " + str(sum_length) + "\n")
    f.write("Average solution length: " + str(f"{average_length:.2f}") + "\n")
    f.write("Total solution cost: " + str(sum_cost) + "\n")
    f.write("Average solution cost: " + str(f"{average_cost:.2f}") + "\n")
    f.write("Average execution time: " + f"{average_execution_time:.2f}" + " seconds \n")
    f.write("Total no solution: " + str(sum_no_solution) + "\n")
    f.write("Average no solution: " + str(f"{average_no_solution:.2f}") + "% \n")


def hamming_dist(input_filename, output_filename, timeout_seconds):
    output_path = "../results/"
    output_filename = output_filename + ".txt"
    f = open(output_path+output_filename, "w+")
    f.truncate(0)

    total_puzzles = 0
    sum_duration = 0
    sum_length = 0
    sum_cost = 0
    sum_no_solution = 0

    for index, puzzle in enumerate(import_input(input_filename)):
        total_puzzles += 1

        time_tracker = TimeAnalyzer()
        ham = HammingDistance(tuple_to_list(puzzle))
        time_tracker.start_timer()
        found = False
        with timeout(timeout_seconds):
            found = ham.search()
        time_tracker.end_timer()
        f.write("------Puzzle " + str(index + 1) + "------" + "\n")
        if found:
            f.write("Solution found \n")

            sum_duration += time_tracker.get_duration()
            f.write("Time to solve: " + str(time_tracker.get_duration()) + " seconds \n")

            sum_length += ham.solution_path
            f.write("Length of hamming distance: " + str(ham.solution_path) + "\n")

            sum_cost += ham.cost_path
            f.write("Cost of solution: " + str(ham.cost_path) + "\n")

            optimality = (ham.solution_path / ham.cost_path) * 100
            f.write("Optimality of solution: " + str(f"{optimality:.2f}") + "% " + "\n\n")
        else:
            sum_no_solution += 1
            f.write("No solution found \n")
            f.write("Time elapsed: " + str(time_tracker.get_duration()) + " seconds \n\n")

    if total_puzzles == sum_no_solution:
        average_execution_time = 0
        average_length = 0
        average_cost = 0
        average_no_solution = 100
    else:
        average_execution_time = sum_duration / (total_puzzles - sum_no_solution)
        average_length = sum_length / (total_puzzles - sum_no_solution)
        average_cost = sum_cost / (total_puzzles - sum_no_solution)
        average_no_solution = (sum_no_solution / total_puzzles) * 100

    f.write("\n ------Analysis------" + "\n")
    f.write("Total solution length: " + str(sum_length) + "\n")
    f.write("Average solution length: " + str(f"{average_length:.2f}") + "\n")
    f.write("Total solution cost: " + str(sum_cost) + "\n")
    f.write("Average solution cost: " + str(f"{average_cost:.2f}") + "\n")
    f.write("Average execution time: " + f"{average_execution_time:.2f}" + " seconds \n")
    f.write("Total no solution: " + str(sum_no_solution) + "\n")
    f.write("Average no solution: " + str(f"{average_no_solution:.2f}") + "% \n")


def manhattan_dist(input_filename, output_filename, timeout_seconds):
    output_path = "../results/"
    output_filename = output_filename + ".txt"
    f = open(output_path+output_filename, "w+")
    f.truncate(0)

    total_puzzles = 0
    sum_duration = 0
    sum_length = 0
    sum_cost = 0
    sum_no_solution = 0

    for index, puzzle in enumerate(import_input(input_filename)):
        total_puzzles += 1

        time_tracker = TimeAnalyzer()
        man = ManhattanDistance(tuple_to_list(puzzle))
        time_tracker.start_timer()
        found = False
        with timeout(timeout_seconds):
            found = man.search()
        time_tracker.end_timer()
        f.write("------Puzzle " + str(index + 1) + "------" + "\n")
        if found:
            f.write("Solution found \n")

            sum_duration += time_tracker.get_duration()
            f.write("Time to solve: " + str(time_tracker.get_duration()) + " seconds \n")

            sum_length += man.solution_path
            f.write("Length of manhattan distance: " + str(man.solution_path) + "\n")

            sum_cost += man.cost_path
            f.write("Cost of solution: " + str(man.cost_path) + "\n")

            optimality = (man.solution_path / man.cost_path) * 100
            f.write("Optimality of solution: " + str(f"{optimality:.2f}") + "% " + "\n\n")
        else:
            sum_no_solution += 1
            f.write("No solution found \n")
            f.write("Time elapsed: " + str(time_tracker.get_duration()) + " seconds \n\n")

    if total_puzzles == sum_no_solution:
        average_execution_time = 0
        average_length = 0
        average_cost = 0
        average_no_solution = 100
    else:
        average_execution_time = sum_duration / (total_puzzles - sum_no_solution)
        average_length = sum_length / (total_puzzles - sum_no_solution)
        average_cost = sum_cost / (total_puzzles - sum_no_solution)
        average_no_solution = (sum_no_solution / total_puzzles) * 100

    f.write("\n ------Analysis------" + "\n")
    f.write("Total solution length: " + str(sum_length) + "\n")
    f.write("Average solution length: " + str(f"{average_length:.2f}") + "\n")
    f.write("Total solution cost: " + str(sum_cost) + "\n")
    f.write("Average solution cost: " + str(f"{average_cost:.2f}") + "\n")
    f.write("Average execution time: " + f"{average_execution_time:.2f}" + " seconds \n")
    f.write("Total no solution: " + str(sum_no_solution) + "\n")
    f.write("Average no solution: " + str(f"{average_no_solution:.2f}") + "% \n")


if __name__ == '__main__':
    # Parameters: input_filename, output_filename, timeout_seconds
    depth_first_search("input_tuples_3x3", "results_dfs", 60)
    iterative_deep("input_tuples_3x3", "results_id", 60)
    hamming_dist("input_tuples_3x3", "results_ham", 60)
    manhattan_dist("input_tuples_3x3", "results_man", 60)
