class Attendance():
    def __init__(self, no_of_academic_days):
        self.no_of_academic_days = no_of_academic_days
        self.cache = {}
        
    def _number_of_ways(self, days_to_fill, consecutive_leaves_consumed):
        if (days_to_fill,consecutive_leaves_consumed) in self.cache:
            return self.cache[(days_to_fill,consecutive_leaves_consumed)]
        if consecutive_leaves_consumed == 4:
            self.cache[(days_to_fill,consecutive_leaves_consumed)] = 0
            return 0
        if days_to_fill == 0:
            self.cache[(days_to_fill,consecutive_leaves_consumed)] = 1
            return 1
        res = self._number_of_ways(days_to_fill-1,0) + self._number_of_ways(days_to_fill-1,consecutive_leaves_consumed+1)
        self.cache[(days_to_fill, consecutive_leaves_consumed)] = res
        return res
    
    def ways_to_attend_classes(self):
        days_to_fill = self.no_of_academic_days
        consecutive_leaves_consumed = 0
        return self._number_of_ways(days_to_fill, consecutive_leaves_consumed)
    
    def ways_to_miss_last_day(self):
        days_to_fill = self.no_of_academic_days -1
        consecutive_leaves_consumed = 1
        return self._number_of_ways(days_to_fill, consecutive_leaves_consumed)