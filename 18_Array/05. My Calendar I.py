# https://leetcode.com/problems/my-calendar-i/

class MyCalendar:

    def __init__(self):
        self.booked = set()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.booked:
            if s < end and start < e: return False
        self.booked.add((start, end))
        return True
      
      
