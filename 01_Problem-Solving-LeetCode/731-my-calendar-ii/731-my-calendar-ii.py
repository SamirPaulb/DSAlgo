class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if s < end and start < e: return False
        
        for s, e in self.calendar:
            if s < end and start < e:
                self.overlaps.append([max(s, start), min(e, end)])
        
        self.calendar.append([start, end])
        return True


# Time: O(N)
# Space: O(N)