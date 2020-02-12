"""
Time and Space Complexity:
Time Complexity: O(MxN) ;where M = Number of Rows, N = Number of Columns
Space Complexity: O(MxN)
"""


class Maze:
    def __init__(self, maze, start_x=0, start_y=0, goal=2):
        """
        :variable maze: a MxN 2D matrix where values are 0(Empty place value/open to move), 1(Block value), 2(Goal value)
        :variable row: initial row number of starting point
        :variable col: initial column number of starting point
        :variable M: length of rows
        :variable N: length of column
        :variable position_vals: movement names for each empty point/state
        :variable positions: each movement point state
        :variable goal: goal to exit from maze (destination)
        :variable visited: check if state which is visited or not
        :variable queue: Movement queue
        :variable path: each prev state and current state with movement name list
        """
        self.maze = maze
        self.row = start_x
        self.col = start_y
        self.M = len(self.maze)
        self.N = len(self.maze[0])
        self.position_vals = ["Left", "Right", "Up", "Down"]
        self.positions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.goal = goal
        self.visited = {}
        self.queue = []
        self.path = []

    def __init_info(self):
        # initially assign all point as a not visited type
        self.visited = {(r, c): False for c in range(self.N) for r in range(self.M)}
        # empty queue
        self.queue = []
        # empty output path
        self.path = []

    def path_valid(self, row, col):
        """
        :params row: current row movement point
        :params col: current column movement point
        """
        # check a state which should take a move or not condition check if row & column are in between of maze then
        # check if the maze state is open to move or is a goal also check if this state previously visited or not
        # then return True if open to move or False
        return (0 <= row < self.M and 0 <= col < self.N) and (
                    self.maze[row][col] == 0 or self.maze[row][col] == self.goal) and not self.visited[(row, col)]

    def get_path(self):
        # from all movement return exact path of destination
        path_len = len(self.path) - 1
        parent = self.path[path_len][0]
        final_path = [self.path[path_len][2]]
        while path_len > 0:
            cur_path = self.path[path_len - 1]
            if parent == cur_path[1]:
                final_path.append(cur_path[2])
                parent = cur_path[0]
            path_len -= 1
        return ' >> '.join(final_path[::-1])

    def find_min_path(self, start_x=None, start_y=None):    # main function which find the shortest path in BFS ways
        self.__init_info()
        row = start_x if start_x else self.row
        col = start_y if start_y else self.col

        # check start state is valid
        if not self.path_valid(row, row):
            return "Path is not valid"

        # make started state as visited
        self.visited[(row, col)] = True
        # insert started state on a queue
        self.queue.append([row, col])
        found = False
        while self.queue and not found:
            row, col = self.queue.pop(0)
            for index, pos_val in enumerate(self.position_vals):
                position_x, position_y = self.positions[index]
                # make new position
                new_row = row + position_x
                new_col = col + position_y
                # check if new state is a valid path
                if self.path_valid(new_row, new_col):
                    # make new state as visited
                    self.visited[(new_row, new_col)] = True
                    # insert new state on a queue
                    self.queue.append([new_row, new_col])
                    # insert prev state and new state with movement name on path
                    self.path.append([(row, col), (new_row, new_col), pos_val])
                    # check new state is a goal
                    if self.maze[new_row][new_col] == self.goal:
                        found = True
                        break
        return self.get_path() if found else "Goal Not Found"


if __name__ == '__main__':
    maze = [
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 1, 2, 1, 0, 1],
        [0, 1, 0, 1, 1, 2],
        [0, 0, 0, 1, 0, 0]
    ]

    maze_obj = Maze(maze)
    # start from (0, 0) state
    print("Output from (0, 0): {}".format(maze_obj.find_min_path()))
    # start from (4,4) state
    print("Output from (4, 4): {}".format(maze_obj.find_min_path(start_x=4, start_y=4)))
