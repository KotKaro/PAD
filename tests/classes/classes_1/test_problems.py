import unittest

from classes.classes_1.problems import check_range, unique_list, volume_of_sphere, bool_range, num_fact


class MyTestCase(unittest.TestCase):
    def test_check_range_values_are_in_range_returns_expected_string(self):
        # Act
        result = check_range(34, 9, 228)

        # Assert
        self.assertEqual(result, "34  jest miedzy 9 a 228")

    def test_check_range_values_are_not_in_range_returns_expected_string(self):
        # Act
        result = check_range(7, 2, 5)

        # Assert
        self.assertEqual(result, "7 NIE jest miedzy 2 a 5")

    def test_bool_range_values_are_in_range_returns_true(self):
        # Act
        result = bool_range(34, 9, 228)

        # Assert
        self.assertEqual(result, True)

    def test_bool_range_values_are_not_in_range_returns_false(self):
        # Act
        result = bool_range(7, 2, 5)

        # Assert
        self.assertEqual(result, False)

    def test_unique_list_returns_only_unique_values_in_list(self):
        # Act
        result = unique_list([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])

        # Assert
        self.assertEqual(result, [1, 2, 3, 4])

    def test_volume_of_sphere_for_radius_2_returns12dot56(self):
        # Act
        result = volume_of_sphere(2)

        # Assert
        self.assertEqual(result, 12.56)

    def test_volume_of_sphere_for_radius_3_returns28dot26(self):
        # Act
        result = volume_of_sphere(3)

        # Assert
        self.assertEqual(result, 28.26)

    def test_num_fact_for_5_returns_factorial_equal_to_120(self):
        # Act
        result = num_fact(5)

        # Assert
        self.assertEqual(result, 120)

    def test_num_fact_for_10_returns_factorial_equal_to_3628800(self):
        # Act
        result = num_fact(10)

        # Assert
        self.assertEqual(result, 3628800)


if __name__ == '__main__':
    unittest.main()
