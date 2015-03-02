class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print self.time

class Clock2(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print time


class Clock3(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print self.time


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__ (obj1 , obj2):
        return (obj1.getX() == obj2.getX()) & (obj1.getY() == obj2.getY())

    def __repr__(obj1):
        return 'Coordinate('+str(obj1.getX())+','+str(obj1.getY())+')'
        
