import unittest
from test import *

class TestDataStructures(unittest.TestCase):

    def test_count_items(self):
        self.assertEqual(count_items([1,2,3]),3)    

    def test_unique_items(self):
        self.assertEqual(unique_items([1,1,2,3]),{1,2,3})

    def test_get_keys(self):
        self.assertEqual(get_keys({"a":1,"b":2}),["a","b"])

    def test_get_values(self):
        self.assertEqual(get_values({"a":1,"b":2}),[1,2])


    def test_sort(self):
        self.assertEqual(sort_numbers([3,1,2]),[1,2,3])

    def test_filter_even(self):
        self.assertEqual(filter_even([1,2,3,4]),[2,4])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1,1,2,3]),[1,2,3])

    def test_sum(self):
        self.assertEqual(sum_numbers([1,2,3]),6)

    def test_factorial(self):
        self.assertEqual(factorial(4),24)

    def test_recursive_sum(self):
        self.assertEqual(recursive_sum(4),10)

    def test_format_name(self):
        self.assertEqual(format_name("Alice",20),"Name: Alice, Age: 20")

    def test_format_price(self):
        self.assertEqual(format_price("Apple",5),"Item: Apple costs $5")

if __name__ == "__main__":
    unittest.main()