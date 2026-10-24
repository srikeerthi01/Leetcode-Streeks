from datetime import datetime
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        a1 = datetime.strptime(arriveAlice, "%m-%d")
        a2 = datetime.strptime(leaveAlice, "%m-%d")
        b1 = datetime.strptime(arriveBob, "%m-%d")
        b2 = datetime.strptime(leaveBob, "%m-%d")

        start = max(a1, b1)
        end = min(a2, b2)

        return max(0, (end - start).days + 1)
        