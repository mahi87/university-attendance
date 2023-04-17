import unittest
from attendance import Attendance

class TestAttendance(unittest.TestCase):
    def test_1_should_return_number_of_ways_to_attend_classes_over_n_days(self):
        no_of_academic_days = 5
        expected_no_of_ways = 29
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_attend_classes(), expected_no_of_ways)
        
    def test_2_should_return_number_of_ways_to_attend_classes_over_n_days(self):
        no_of_academic_days = 10
        expected_no_of_ways = 773
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_attend_classes(), expected_no_of_ways)
    
    def test_1_should_return_number_of_ways_to_miss_last_day_of_classes(self):
        no_of_academic_days = 5
        expected_no_of_ways = 14
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_miss_last_day(), expected_no_of_ways)
    
    def test_2_should_return_number_of_ways_to_miss_last_day_of_classes(self):
        no_of_academic_days = 10
        expected_no_of_ways = 372
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_miss_last_day(), expected_no_of_ways)