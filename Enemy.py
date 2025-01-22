import pygame, math, numpy

class Enemy:
    def __init__(self, map):
        self.following = "2"
        self.xd = 0
        self.yd = 0
        self.x = 0
        self.y = 0

        flat = numpy.array(map).flatten().tolist()
        index = flat.index("1")
        x, y = self.getPos(index, map)

        self.x = x
        self.y = y
        self.getDirection(map)

    def getPos(self, index, map):
        return [index % len(map[0]), index // len(map[0])]
    
    def getIndex(self, map):
        return self.x + (self.y*len(map[0]))
    
    def getDirection(self, map):
        flat = numpy.array(map).flatten().tolist()
        index = 0
        try:
            index = flat.index(self.following)
        except:
            return
        x = index % len(map[0])
        y = index // len(map[0])

        self.xd = x - self.x 
        self.yd = y - self.y
        mag = math.sqrt(self.xd**2 + self.yd**2)

        # self.xd /= mag
        # self.yd /= mag
        self.xd = round(self.xd/mag)
        self.yd = round(self.yd/mag)
    
    def update(self, map, health, enemies):
        i = self.getIndex(map)
        index = -1
        try:
            flat = numpy.array(map).flatten().tolist()
            index = flat.index(self.following)
        except:
            health[0] -= 15
            enemies.remove(self)
        if (i == index):
            self.following = str(int(self.following)+1)
            self.getDirection(map)
        
        self.x += self.xd
        self.y += self.yd


