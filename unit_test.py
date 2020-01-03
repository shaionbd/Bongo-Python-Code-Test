import unittest

import test1
import test2
import test3


class TestTask1Method(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_depth_of_test1(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 2,
                "key4": {
                    "key5": 4,
                    "key6": 4,
                    "key7":{
                        "key8": 5
                    }
                },
            "key9": 2
            }
        }
        depth_data = test1.depth(data, 1, [])
        sort_data = sorted(depth_data, key=lambda data: data[1])
        expected_data = [('key1', 1), ('key2', 1), ('key3', 2), ('key4', 2), ('key9', 2), ('key5', 3), ('key6', 3), ('key7', 3), ('key8', 4)]
        self.assertEqual(expected_data, sort_data)

    def test_depth_of_test2(self):
        person_a = test2.Person("User", "1", None)
        person_b = test2.Person("User", "2", person_a)
        person_c = test2.Person("User", "3", person_b)
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                },
                "key6": person_c
            },
        }
        depth_data = test2.depth(data, 1, [])
        sort_data = sorted(depth_data, key=lambda data: data[1])
        expected_data = [('key1', 1), ('key2', 1), ('key3', 2), ('key4', 2), ('key6', 2), ('key5', 3), ('user', 3), ('first_name', 3), ('last_name', 3), ('father', 3), ('first_name', 4), ('last_name', 4), ('father', 4), ('first_name', 4), ('last_name', 4), ('father', 4), ('first_name', 5), ('last_name', 5), ('father', 5), ('first_name', 5), ('last_name', 5), ('father', 5)]
        self.assertEqual(expected_data, sort_data)

    def test_lca(self):
        node1 = test3.Node(1)
        node2 = test3.Node(2, node1)
        node3 = test3.Node(3, node1)
        node4 = test3.Node(4, node2)
        node5 = test3.Node(5, node2)
        node6 = test3.Node(6, node3)
        node7 = test3.Node(7, node3)
        node8 = test3.Node(8, node4)
        node9 = test3.Node(9, node4)
        node10 = test3.Node(10, node6)

        for i in range(5):
            lst = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10]
            expexted_output = [1, 1, 1, 4, 1]
            ancestor = test3.lca(lst[i], lst[i+5])
            self.assertEqual(expexted_output[i], ancestor.value)

if __name__ == '__main__':
    unittest.main()