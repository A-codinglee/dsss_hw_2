import unittest
from math_quiz import Random_Int, Random_Op, Calculator


class TestMathGame(unittest.TestCase):

    def test_Random_Int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_Int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Random_Op(self):
        # TODO
        for _ in range(1000):
            rand_op = Random_Op()
            self.assertTrue(rand_op == '+' or rand_op == '-' or rand_op == '*')

    def test_Calculator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 15, '*', '10 * 15', 150),
                (-7, 21, '-', '-7 - 21', -28),
                (0, -10, '+', '0 + -10', -10),
                (-1, 2, '*', '-1 * 2', -2)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                actual_problem, actual_answer = Calculator(num1, num2, operator)
                self.assertEqual(actual_problem, expected_problem)
                self.assertEqual(actual_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
