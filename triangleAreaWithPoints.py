
class TriangleAreaWithPoints():
    def __init__(self, xa,ya,xb,yb,xc,yc):
        self.__xa=xa
        self.__ya=ya
        self.__xb=xb
        self.__yb=yb
        self.__xc=xc
        self.__yc=yc

    def matrixDet(self):
        d=(self.__xa * self.__yb + self.__xb*self.__yc+self.__xc*self.__ya)-(self.__ya * self.__xb + self.__yb*self.__xc+self.__yc*self.__xa)
        return abs(d)
    
    def area(self):
        return self.matrixDet()/2
    
example=TriangleAreaWithPoints(0,2,-4,1,2,3)
print(example.area())