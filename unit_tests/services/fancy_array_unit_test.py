from services.fancy_array import FancyArray
import unittest

class TestFancyArray(unittest.TestCase):
    def test_first_array(self):
        # Arrange
        arr = [3, 0, 2, 8, 6, 1, 9, 5, 4, 7]
        fancy_array = FancyArray(arr)

        # Act
        lesser_than = fancy_array.is_less_than(arr[1], arr[2])
        greater_than = fancy_array.is_greater_than(arr[7], arr[6])
        smallest = fancy_array.find_smallest_number()
        smallest_position = fancy_array.find_smallest_number_and_position()
        largest = fancy_array.find_largest_number()
        largest_position = fancy_array.find_largest_number_and_position()
        sort_once = fancy_array.sort_one_pass_asc()

        # Assert
        self.assertEqual(lesser_than, True)
        self.assertEqual(greater_than, False)
        self.assertEqual(smallest, 0)
        self.assertEqual(smallest_position, (1, 0))
        self.assertEqual(largest, 9)
        self.assertEqual(largest_position, (6, 9))
        self.assertEqual(sort_once, [0, 2, 3, 6, 1, 8, 5, 4, 7, 9])
    
    def test_second_array(self):
        # Arrange
        arr = [8, 3, 4, 2]
        fancy_array = FancyArray(arr)

        # Act
        smallest = fancy_array.find_smallest_number_and_position()

        # Assert
        self.assertEqual(smallest, (3, 2))
    
    def test_third_array(self):
        # Arrange
        arr = [7, 4, 6, 5]
        fancy_array = FancyArray(arr)

        # Act
        sorting = fancy_array.sort_one_pass_desc()

        # Assert
        self.assertEqual(sorting, [7, 6, 5, 4])
    
    def test_fourth_array(self):
        # Arrange
        arr = [6, 5, 8, 7]
        fancy_array = FancyArray(arr)

        # Act
        sort_asc = fancy_array.sort_one_pass_asc()

        # Assert
        self.assertEqual(sort_asc, [5, 6, 7, 8])
    
    def test_fifth_array(self):
        # Arrange
        arr = [9, 0, 8, 1]
        fancy_array = FancyArray(arr)

        # Act
        sort_desc = fancy_array.sort_one_pass_desc()

        # Assert
        self.assertEqual(sort_desc, [9, 8, 1, 0])
    
    def test_sixth_array(self):
        # Arrange
        arr = [5, 7, 6, 3]
        fancy_array = FancyArray(arr)

        # Act
        asc_sort = fancy_array.sort_asc()

        # Assert
        self.assertEqual(asc_sort, [3, 5, 6, 7])
    
    def test_seventh_array(self):
        # Arrange
        arr = [5, 7, 6, 3]
        fancy_array = FancyArray(arr)

        # Act
        asc_desc = fancy_array.sort_desc()

        # Assert
        self.assertEqual(asc_desc, [7, 6, 5, 3])
    
    def test_eighth_array(self):
        # Arrange
        arr = [3, 0, 2, 8, 6, 1, 9, 5, 4, 7]
        fancy_array = FancyArray(arr)

        # Act
        fancy_array.swap(3, 5)

        # Assert
        self.assertEqual(arr, [3, 0, 2, 1, 6, 8, 9, 5, 4, 7])

    def test_find_my_magic_number(self):
        # Arrange
        arr = [3, 0, 8, 6, 1, 9, 5, 4, 7, 2]
        fancy_array = FancyArray(arr)
        my_magic_number_expected = 8
        is_my_magic_number = lambda x : x % 3 == 2

        # Act
        my_magic_number = fancy_array.find_magic_number(is_my_magic_number)
        #my_magic_number = fancy_array.find_magic_number(self.whatever)

        # Assert
        self.assertEqual(my_magic_number, my_magic_number_expected)

    def whatever(self, x) :
        return x % 3 == 2

unittest.main()