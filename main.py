import pygame, random
from Enemy import Enemy
from Tower import Tower

#homework: limit towers somehow and game end, new towers

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

health = [100]
map = []
enemies = []
towers = []

accumulator = 0

file = open("map.txt", "r")
for line in file:
    l = list(line)
    if l[len(l)-1] == "\n": l = l[:-1]
    map.append(l)

gridwidth = WIDTH/len(map[0])
gridheight = HEIGHT/len(map)

enemies.append(Enemy(map, gridwidth, gridheight))
towers.append(Tower(WIDTH/2, HEIGHT/2))

last = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((176, 78, 25, 255))

    accumulator += 1

    if ((accumulator % 35) == 0 and random.randint(0, 100) < 35): enemies.append(Enemy(map, gridwidth, gridheight))
    for e in enemies:
        if (not e.alive): enemies.remove(e)
        if ((accumulator % 35) == 0): 
            e.update(map, health, enemies)

    for t in towers:
        if ((accumulator % 35) == 0): 
            t.update(enemies)

    pos = pygame.mouse.get_pos()
    pos = [(pos[0] // gridwidth) * gridwidth, (pos[1] // gridheight) * gridheight]
    mousedown = pygame.mouse.get_pressed()[0]

    
    if (mousedown and not last):
        check = list(filter(lambda t: t.x == int(pos[0] + gridwidth/2) and t.y == int(pos[1] + gridheight/2), towers))
        if (len(check) < 1):
            towers.append(Tower(int(pos[0] + gridwidth/2), int(pos[1] + gridheight/2)))
    
    for y, line in enumerate(map):
        for x, box in enumerate(line):
            color = (0, 0, 0, 0)
            match box:
                case "0":
                    # color = (255, 0, 0, 255)
                    continue
                case "p":
                    color = (0, 255, 0, 255)
                case _:
                    color = (0, 0, 255, 255)
            
            pygame.draw.rect(screen, color, (x*gridwidth, y*gridheight, gridwidth, gridheight))

    for e in enemies:
        x, y = e.renderPosition()
        pygame.draw.rect(screen, (255, 0, 255, 255), (x, y, gridwidth*0.5, gridheight*0.5))

    for t in towers:
        pygame.draw.rect(screen, (0, 255, 0, 255), (t.x - 25, t.y - 25, 50, 50))
        for b in t.bullets:
            pygame.draw.circle(screen, (255, 0, 0, 255), (b[0], b[1]), 15)

    
    pygame.draw.rect(screen, (100, 100, 100, 100), (pos[0], pos[1], gridwidth, gridheight))

    color = (255, 0, 0, 255)
    if (health[0] < 10): color = (255, 0, 0, 255)
    elif (health[0] < 25): color = (255, 119, 0, 255)
    elif (health[0] < 50): color = (255, 204, 0, 255)
    elif (health[0] < 75): color = (153, 255, 0, 255)
    else: color = (21, 189, 2, 255)
    pygame.draw.rect(screen, (209, 64, 27, 255), (WIDTH*0.04, HEIGHT*0.94 - (HEIGHT*0.075/2), WIDTH*0.27, HEIGHT*0.12))
    pygame.draw.rect(screen, color, (WIDTH*0.05, HEIGHT*0.95 - (HEIGHT*0.075/2), WIDTH*0.25*(health[0]/100), HEIGHT*0.075))

    last = mousedown

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()