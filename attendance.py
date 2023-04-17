MAX_CONSECUTIVE_LEAVES_ALLOWED = 4


class Attendance:
    def _is_not_valid(self, no_of_academic_days):
        return no_of_academic_days < 1

    def __init__(self, no_of_academic_days):
        if self._is_not_valid(no_of_academic_days):
            raise ValueError("Invalid Input")
        self.no_of_academic_days = no_of_academic_days
        self.cache = {}

    def _number_of_ways(self, days_to_fill, consecutive_leaves_consumed):
        if (days_to_fill, consecutive_leaves_consumed) in self.cache:
            return self.cache[(days_to_fill, consecutive_leaves_consumed)]

        if consecutive_leaves_consumed == MAX_CONSECUTIVE_LEAVES_ALLOWED:
            self.cache[(days_to_fill, consecutive_leaves_consumed)] = 0
            return 0

        if days_to_fill == 0:
            self.cache[(days_to_fill, consecutive_leaves_consumed)] = 1
            return 1

        res = self._number_of_ways(days_to_fill - 1, 0) + self._number_of_ways(
            days_to_fill - 1, consecutive_leaves_consumed + 1
        )
        self.cache[(days_to_fill, consecutive_leaves_consumed)] = res
        return res

    def ways_to_attend_classes(self):
        days_to_fill = self.no_of_academic_days
        consecutive_leaves_consumed = 0
        return self._number_of_ways(days_to_fill, consecutive_leaves_consumed)

    def ways_to_miss_last_day(self):
        days_to_fill = self.no_of_academic_days - 1
        consecutive_leaves_consumed = 1
        return self._number_of_ways(days_to_fill, consecutive_leaves_consumed)

    def probability_to_miss_grad_ceremony(self):
        miss_last_day = self.ways_to_miss_last_day()
        total_ways_to_attend_classes = self.ways_to_attend_classes()
        return f"{miss_last_day}/{total_ways_to_attend_classes}"
