import pygame, math

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.time = 0
        self.bullets = []

    def update(self, enemies):
        self.time += 1
        if (self.time%3 == 0):
            enemy = None
            d = 9999999
            for e in enemies:
                held = math.sqrt((e.x-self.x) ** 2 + (e.y-self.y) ** 2)
                if held < d:
                    d = held
                    enemy = e
                

            if (enemy != None): self.bullets.append([self.x, self.y, enemy])

        for b in self.bullets:
            
            if (not b[2]):
                self.bullets.remove(b)
                b[2].alive = False
                return
            x, y = b[2].renderPosition()
            x -= b[2].gridwidth*0.25
            y -= b[2].gridheight*0.25
            d = math.sqrt((x-b[0]) ** 2 + (y-b[1]) ** 2)
            bvx = (x- b[0])/d
            bvy = (y - b[1])/d

            b[0] += bvx*100
            b[1] += bvy*100

            if (self.rectCircle(b[0], b[1], 30, x+b[2].gridwidth*0.25, y+b[2].gridheight*0.25, b[2].gridwidth*0.5, b[2].gridheight*0.5) and b[2].alive):
                self.bullets.remove(b)
                b[2].alive = False

    
    def rectCircle(self, cx, cy, cr, rx, ry, rw, rh):
        tx = cx
        ty = cy
        if (cx < rx):         tx = rx
        elif (cx > rx+rw): tx = rx+rw

        if (cy < ry):         ty = ry
        elif (cy > ry+rh): ty = ry+rh

        return math.sqrt(((cx-tx)**2) + ((cy-ty)**2)) < cr