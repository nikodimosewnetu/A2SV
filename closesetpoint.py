class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points_distance = []
        for point in points:
            distance = pow(point[0],2) + pow(point[1],2)
            point.insert(0,distance)
            points_distance.append(point) 
        
        points_distance = sorted(points_distance,key= lambda x : x[0])
        nearest = []
        for point_ in points_distance:
            if k > 0:
                nearest.append(point_[1:])
                k -=1
            else:
                break
        return nearest
