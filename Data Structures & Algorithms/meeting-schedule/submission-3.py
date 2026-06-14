"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        for i in range(len(intervals)):
            
            curr = intervals[i]

            for y in range(i+1, len(intervals)):    
                
                compared = intervals[y]

                #curr in compared
                if (compared.start <= curr.start < compared.end or compared.start < curr.end <= compared.end):
                    return False
                #compared in curr
                if (curr.start <= compared.start < curr.end or curr.start < compared.end <= curr.end):
                    return False
                
            
        return True