
#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution(object):
    def checkStraightLine(self, coordinates):
        y1=coordinates[0][1]
        y2=coordinates[-1][1]
        x1=coordinates[0][0]
        x2=coordinates[-1][0]
        c=0
        for i,j in coordinates:
                if (x2-x1)*j!=(y2-y1)*(i-x1)+y1*(x2-x1):
                    return False
        return True
