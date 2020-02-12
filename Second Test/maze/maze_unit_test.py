import unittest
from .find_maze_shortest_path import Maze


class TestMazeMethod(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def _get_test_data(self):
        return [
            (
                [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 1, 0]],
                "Right >> Right >> Right >> Right >> Right >> Down >> Down >> Down"
            ),
            (
                [[0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 2], [0, 0, 0, 1, 0, 0]],
                "Down >> Down >> Down >> Down >> Right >> Right >> Up >> Up >> Up >> Up >> Right >> Right >> Down >> Down >> Down >> Right"
            ),
            (
                [[0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 1, 2], [0, 0, 0, 1, 0, 0]],
                "Goal Not Found"
            ),
            (
                [[0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1], [0, 1, 2, 1, 0, 1], [0, 1, 0, 1, 1, 2], [0, 0, 0, 1, 0, 0]],
                "Down >> Right >> Right >> Down"
            )
        ]

    def test_success_maze(self):
        maze_data_list = self._get_test_data()

        for maze_info in maze_data_list:
            maze_data, expected_output = maze_info
            maze = Maze(maze_data)
            self.assertEqual(expected_output, maze.find_min_path())

    def test_failed_maze(self):
        maze_data = [
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 1, 2, 1, 0, 1],
            [0, 1, 0, 1, 0, 2],
            [0, 0, 0, 1, 0, 0]
        ]
        expected_output = "Down >> Right >> Right >> Down"
        unexpected_output_1 = "Down >> Down >> Down >> Down >> Right >> Right >> Up >> Up"
        unexpected_output_2 = "Down >> Right >> Right >> Up >> Right >> Right >> Down >> Down >> Down >> Right"
        maze = Maze(maze_data)
        self.assertEqual(expected_output, maze.find_min_path())
        self.assertNotEqual(unexpected_output_1, maze.find_min_path())
        self.assertNotEqual(unexpected_output_2, maze.find_min_path())


if __name__ == '__main__':
    unittest.main()
