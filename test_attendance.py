import unittest
from attendance import Attendance

class TestWaysToAttendClasses(unittest.TestCase):
    def test_should_return_number_of_ways_to_attend_classes_over_5_days(self):
        no_of_academic_days = 5
        expected_no_of_ways = 29
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_attend_classes(), expected_no_of_ways)
        
    def test_should_return_number_of_ways_to_attend_classes_over_10_days(self):
        no_of_academic_days = 10
        expected_no_of_ways = 773
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_attend_classes(), expected_no_of_ways)

class TestWaysToMissLastDay(unittest.TestCase):
    def test_should_return_number_of_ways_to_miss_last_day_of_classes_for_5_days(self):
        no_of_academic_days = 5
        expected_no_of_ways = 14
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_miss_last_day(), expected_no_of_ways)
    
    def test_should_return_number_of_ways_to_miss_last_day_of_classes_for_10_days(self):
        no_of_academic_days = 10
        expected_no_of_ways = 372
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.ways_to_miss_last_day(), expected_no_of_ways)

class TestProbabilityToMissGradCeremony(unittest.TestCase):        
    def test_should_return_probability_to_miss_grad_ceremony_in_string_format_for_5_days(self):
        no_of_academic_days = 5
        expected_probability = "14/29"
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.probability_to_miss_grad_ceremony(), expected_probability)
        
    def test_should_return_probability_to_miss_grad_ceremony_in_string_format_for_10_days(self):
        no_of_academic_days = 10
        expected_probability = "372/773"
        at = Attendance(no_of_academic_days)
        self.assertEqual(at.probability_to_miss_grad_ceremony(), expected_probability)
        