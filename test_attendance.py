import unittest
from attendance import Attendance

class TestAttendance(unittest.TestCase):
    def test_should_return_number_of_ways_to_attend_classes_over_n_days(self):
        no_of_academic_days = 5
        expected_no_of_ways = 29
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_attend_classes(), expected_no_of_ways)
        
    
    