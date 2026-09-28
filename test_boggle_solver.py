"""
Chase Medy
003107993

Black-box unit tests for boggle_solver.Boggle.
"""

import unittest
import sys

sys.path.append("/home/codio/workspace/")

from boggle_solver import Boggle


def _run(grid, dictionary):
    game = Boggle(grid, dictionary)
    return sorted(w.upper() for w in game.getSolution())


def _expected(words):
    return sorted(w.upper() for w in words)


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        expected = ["abc", "abdhi", "cfi", "dea"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Normal_case_4x4(self):
        grid = [
            ["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["I", "J", "K", "L"],
            ["M", "N", "O", "P"],
        ]
        dictionary = ["abcd", "efg", "fjk", "mnop", "abfe", "xyz"]
        expected = ["abcd", "efg", "fjk", "mnop", "abfe"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Normal_case_5x5(self):
        grid = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O"],
            ["P", "Q", "R", "S", "T"],
            ["U", "V", "W", "X", "Y"],
        ]
        dictionary = ["abc", "ghi", "mno", "pqr", "vwx", "abgf", "zzz"]
        expected = ["abc", "ghi", "mno", "pqr", "vwx", "abgf"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Normal_case_6x6(self):
        grid = [
            ["A", "B", "C", "D", "E", "F"],
            ["G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X"],
            ["Y", "Z", "A", "B", "C", "D"],
            ["E", "F", "G", "H", "I", "J"],
        ]
        dictionary = ["abc", "ghi", "opq", "stu", "yza", "efg", "efghij"]
        expected = ["abc", "ghi", "opq", "stu", "yza", "efg", "efghij"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Normal_case_7x7(self):
        grid = [
            ["A", "B", "C", "D", "E", "F", "G"],
            ["H", "I", "J", "K", "L", "M", "N"],
            ["O", "P", "Q", "R", "S", "T", "U"],
            ["V", "W", "X", "Y", "Z", "A", "B"],
            ["C", "D", "E", "F", "G", "H", "I"],
            ["J", "K", "L", "M", "N", "O", "P"],
            ["Q", "R", "S", "T", "U", "V", "W"],
        ]
        dictionary = ["abc", "hij", "opq", "vwx", "stu", "notfound"]
        expected = ["abc", "hij", "opq", "vwx", "stu"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Large_dictionary_10x10(self):
        grid = [
            ["C", "A", "T", "S", "D", "O", "G", "B", "I", "R"],
            ["H", "E", "L", "P", "F", "I", "S", "H", "M", "D"],
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
            ["U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"],
            ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N"],
            ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"],
            ["Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"],
            ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"],
        ]
        real_words = ["cats", "dog", "fish", "help"]
        noise = [f"zzz{i:03d}" for i in range(200)]
        dictionary = real_words + noise
        self.assertEqual(_expected(real_words), _run(grid, dictionary))

    def test_Rectangular_grid_3x5(self):
        grid = [
            ["A", "B", "C", "D", "E"],
            ["F", "G", "H", "I", "J"],
            ["K", "L", "M", "N", "O"],
        ]
        dictionary = ["abc", "fgh", "klm", "afk"]
        expected = ["abc", "fgh", "klm", "afk"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Rectangular_grid_4x2(self):
        grid = [["A", "B"], ["C", "D"], ["E", "F"], ["G", "H"]]
        dictionary = ["abd", "ace", "cef", "gh"]
        expected = ["abd", "ace", "cef"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))


class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        self.assertEqual(_expected([]), _run(grid, dictionary))

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        self.assertEqual(_expected([]), _run(grid, dictionary))

    def test_Empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        self.assertEqual(_expected([]), _run(grid, []))

    def test_No_matching_words(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["xyz", "hello", "zebra"]
        self.assertEqual(_expected([]), _run(grid, dictionary))

    def test_Words_shorter_than_3_ignored(self):
        grid = [["C", "A"], ["B", "T"]]
        dictionary = ["ab", "ac", "cab", "cat"]
        expected = ["cab", "cat"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Case_insensitive_matching(self):
        grid = [["c", "a"], ["b", "t"]]
        dictionary = ["CAT", "BAT"]
        expected = ["cat", "bat"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Invalid_grid_not_a_list(self):
        self.assertEqual(_expected([]), _run("not a list", ["abc"]))

    def test_Invalid_grid_numeric_cell(self):
        grid = [["A", "B"], ["C", "1"]]
        self.assertEqual(_expected([]), _run(grid, ["abc"]))

    def test_Invalid_grid_non_string_cell(self):
        grid = [["A", "B"], ["C", 5]]
        self.assertEqual(_expected([]), _run(grid, ["abc"]))

    def test_Invalid_dictionary_not_a_list(self):
        grid = [["A", "B"], ["C", "D"]]
        self.assertEqual(_expected([]), _run(grid, "abc"))

    def test_Ragged_grid_rows(self):
        grid = [["A", "B", "C"], ["D", "E"]]
        self.assertEqual(_expected([]), _run(grid, ["abc", "de"]))

    def test_Grid_row_not_a_list(self):
        grid = [["A", "B"], "CD"]
        self.assertEqual(_expected([]), _run(grid, ["abc"]))


class TestSuite_Complete_Coverage(unittest.TestCase):

    def test_Diagonal_traversal(self):
        grid = [["A", "X", "Y"], ["Z", "B", "W"], ["V", "U", "C"]]
        self.assertEqual(_expected(["abc"]), _run(grid, ["abc"]))

    def test_No_cell_reuse_within_word(self):
        grid = [["A", "B"], ["C", "D"]]
        self.assertEqual(_expected([]), _run(grid, ["aba", "abcda"]))

    def test_Duplicate_letters_allow_different_cells(self):
        grid = [["A", "B"], ["A", "C"]]
        dictionary = ["aba", "aca", "abc"]
        expected = ["aba", "aca", "abc"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Word_uses_snake_path(self):
        grid = [["A", "B"], ["D", "C"]]
        self.assertEqual(_expected(["abcd"]), _run(grid, ["abcd"]))

    def test_Overlapping_prefixes(self):
        grid = [
            ["C", "A", "T"],
            ["A", "R", "S"],
            ["B", "E", "D"],
        ]
        dictionary = ["cat", "cats", "car", "cars", "care"]
        expected = ["cat", "cats", "car", "cars", "care"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Long_word_wraps_full_grid(self):
        grid = [
            ["A", "B", "C", "D"],
            ["H", "G", "F", "E"],
            ["I", "J", "K", "L"],
            ["P", "O", "N", "M"],
        ]
        self.assertEqual(
            _expected(["abcdefghijklmnop"]),
            _run(grid, ["abcdefghijklmnop"]),
        )

    def test_Duplicate_words_in_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        self.assertEqual(_expected(["abc"]), _run(grid, ["abc", "abc", "abc"]))

    def test_Same_word_multiple_grid_paths_counted_once(self):
        grid = [["A", "A"], ["B", "B"]]
        self.assertEqual(_expected(["abb", "aab"]), _run(grid, ["abb", "aab"]))


class TestSuite_Qu_and_St(unittest.TestCase):

    def test_Qu_tile_basic(self):
        grid = [
            ["Qu", "A", "B"],
            ["C", "D", "E"],
            ["F", "G", "H"],
        ]
        self.assertEqual(_expected(["qua", "quad"]), _run(grid, ["qua", "quad"]))

    def test_St_tile_basic(self):
        grid = [
            ["St", "A", "R"],
            ["B", "C", "D"],
            ["E", "F", "G"],
        ]
        self.assertEqual(_expected(["star", "stab"]), _run(grid, ["star", "stab"]))

    def test_Ie_tile_basic(self):
        grid = [
            ["P", "Ie", "R"],
            ["A", "B", "C"],
            ["D", "E", "F"],
        ]
        self.assertEqual(_expected(["pie", "pier"]), _run(grid, ["pie", "pier"]))

    def test_Qu_tile_in_larger_word(self):
        grid = [
            ["Qu", "A", "R"],
            ["I", "T", "Z"],
            ["E", "N", "B"],
        ]
        dictionary = ["quart", "quartz", "quit"]
        expected = ["quart", "quartz", "quit"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Multiple_special_tiles_in_one_grid(self):
        grid = [
            ["Qu", "A", "St"],
            ["I", "P", "O"],
            ["T", "R", "Ie"],
        ]
        dictionary = ["quip", "stop", "pier", "quit"]
        expected = ["quip", "stop", "pier", "quit"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))

    def test_Qu_tile_word_of_exact_length_3(self):
        grid = [["Qu", "E"], ["Y", "T"]]
        self.assertEqual(_expected(["que"]), _run(grid, ["que", "qu"]))

    def test_Special_tile_present_but_word_uses_normal_letters(self):
        grid = [
            ["Qu", "A", "T"],
            ["R", "I", "B"],
            ["S", "M", "C"],
        ]
        dictionary = ["tab", "rib", "air"]
        expected = ["tab", "rib", "air"]
        self.assertEqual(_expected(expected), _run(grid, dictionary))


if __name__ == '__main__':
    unittest.main()