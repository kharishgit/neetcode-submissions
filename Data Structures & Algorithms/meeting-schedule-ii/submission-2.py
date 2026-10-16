"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events=[]
        for interval in intervals:
            events.append((interval.start,+1))
            events.append((interval.end,-1))
        events.sort()

        counter = max_rooms = 0
        for time, change in events:
            counter+=change
            max_rooms= max(counter,max_rooms)
        return max_rooms

        