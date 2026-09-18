class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for start,end in nums:
            for i in range(start,end+1): #we add the integgers between the start,end+1 
                points.add(i)
        return len(points)
    #the question asks for the unique intersection of the car, -> we return the len of a variable, that variable consists the all the elements from the range start,end of the car parking
        