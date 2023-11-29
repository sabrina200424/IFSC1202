import math

# make class type for Triangle, type, perimeter, area, and angles 

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)
    
    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2:
            return "Isosceles"
        elif self.s1 == self.s3:
            return "Isosceles"
        elif self.s2 == self.s3:
            return "Isoceles"
        else:
            return "Scalene"
    
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
    
    def angles(self):
        #arcoss has no attribute use acos
        # ** = exponent value
        angle1 = math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)))
        angle2 = math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)))
        angle3 = math.degrees(math.acos((self.s1**2 + self.s2**2 - self.s3**2) / (2 * self.s1 * self.s2)))
        return angle1, angle2, angle3


TriangleList = []
numberslist = open("Exam Three Triangles.txt", "r")
for line in numberslist:
        sides = line.strip().split(", ")
        triangle = Triangle(sides[0], sides[1], sides[2])
        TriangleList.append(triangle)


#print("{:<12s} {:<12s} {:<12s} {:<12s} {:<12s} {:<12s} {:<12s} {:<12s} {:<12s}").format("Type", "Side 1", "Side 2", "Side 3", "Perimeter","Area", "Angle 1", "Angle 2", "Angle 3")
# 12 pushes string out to dif line
print("{:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s}".format("Type", "Side 1", "Side 2", "Side 3", "Perimeter", "Area", "Angle 1", "Angle 2", "Angle 3"))
for triangle in TriangleList:
    angles = triangle.angles()
    print("{:>10s} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f} {:>10.3f}".format(triangle.type(), triangle.s1, triangle.s2, triangle.s3, triangle.perimeter(), triangle.area(), angles[0], angles[1], angles[2]))
    # .3 for three floating values