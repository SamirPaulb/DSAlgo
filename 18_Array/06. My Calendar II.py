# https://leetcode.com/problems/my-calendar-ii/
# https://youtu.be/_7B_HzJUE6E

'''
class MyCalendarTwo:
    
    def __init__(self):
        self.dct = {}
    
    def book(self, start: int, end: int) -> bool:
        self.dct[start] = self.dct[start] + 1 if start in self.dct else 1
        self.dct[end] = self.dct[end] - 1 if end in self.dct else -1
        
        arr = sorted(self.dct.keys())
        s = 0
        for i in arr:
            s += self.dct[i]
            if s >= 3:
                self.dct[start] -= 1
                self.dct[end] += 1
                return False
            
        return True
        
        
# Time: O(N log(N))
# Space: O(N)
'''



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

