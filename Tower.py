import pygame, math

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.time = 0
        self.bullets = []

    def update(self, enemies):
        self.time += 1
        if (self.time%50 == 0):
            enemy = None
            d = 9999999
            for e in enemies:
                held = math.sqrt(e.x-self.x ** 2 + e.y-self.y ** 2)
                if held < d:
                    d = held
                    enemy = e
            

            self.bullets.append([self.x, self.y, enemy])

        for b in self.bullets:
            d = math.sqrt(self.x-b[2].x ** 2 + self.y-b[2].y ** 2)
            bvx = (self.x - b[2].x)/d
            bvy = (self.y - b[2].y)/d

            b[0] += bvx/3
            b[1] += bvy/3

    
    def rectCircle(cx, cy, rx, ry, rw, rh):
        pass