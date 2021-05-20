import unittest
from main import Knuth_Morris_Pratt_algorithm


class testMain(unittest.TestCase):
    def setUp(self):
        self.first_test_basic_text = "The thirty-three thieves thought that they thrilled the throne throughout Thursday"
        self.first_test_the_required_set = "Monday"
        self.second_test_basic_text = "Peter Piper Picked a Peck of Pickled Peppers"
        self.second_test_the_required_set = "Pickled"
        self.third_test_basic_text = "Интервьюер интервента интервьюировал"
        self.third_test_the_required_set = "интервьюир"
        self.first_result = "The required set not found"
        self.second_result = "The required set found"
        self.third_result = "The required set found"

    def test_first(self):
        self.assertEqual(Knuth_Morris_Pratt_algorithm(self.first_test_the_required_set, self.first_test_basic_text), self.first_result)

    def test_second(self):
        self.assertEqual(Knuth_Morris_Pratt_algorithm(self.second_test_the_required_set, self.second_test_basic_text), self.second_result)

    def test_third(self):
        self.assertEqual(Knuth_Morris_Pratt_algorithm(self.third_test_the_required_set, self.third_test_basic_text), self.third_result)

if __name__ == '__main__':
    unittest.main()
