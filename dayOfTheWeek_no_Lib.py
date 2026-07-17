class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Days sequence starting from Friday (since Jan 1, 1971 is Friday)
        days_of_week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        
        # Days in each month (Index 0 is placeholder, Index 1 is January...)
        months_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        total_days = 0
        
        # 1. Count days from full years passed since 1971
        for y in range(1971, year):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                total_days += 366
            else:
                total_days += 365
                
        # 2. Count days from full months passed in the current year
        for m in range(1, month):
            if m == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                total_days += 29
            else:
                total_days += months_days[m]
                
        # 3. Add the days of the current month (minus 1 because Jan 1 itself is day 0)
        total_days += day - 1
        
        # 4. Map the modulo result to our weekday array
        return days_of_week[total_days % 7]
