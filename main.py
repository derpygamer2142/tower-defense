import pygame, random
from Enemy import Enemy

#homework: towers and shooting

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


enemies.append(Enemy(map))
print(enemies[0].x, enemies[0].y)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((176, 78, 25, 255))

    accumulator += 1

    if ((accumulator % 35) == 0 and random.randint(0, 100) < 35): enemies.append(Enemy(map))
    for e in enemies:
        if ((accumulator % 35) == 0): 
            e.update(map, health, enemies)

    gridwidth = WIDTH/len(map[0])
    gridheight = HEIGHT/len(map)

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
        pygame.draw.rect(screen, (255, 0, 255, 255), (e.x*gridwidth + gridwidth*0.25, e.y*gridheight + gridheight*0.25, gridwidth*0.5, gridheight*0.5))
    color = (255, 0, 0, 255)
    if (health[0] < 10): color = (255, 0, 0, 255)
    elif (health[0] < 25): color = (255, 119, 0, 255)
    elif (health[0] < 50): color = (255, 204, 0, 255)
    elif (health[0] < 75): color = (153, 255, 0, 255)
    else: color = (21, 189, 2, 255)
    pygame.draw.rect(screen, (209, 64, 27, 255), (WIDTH*0.04, HEIGHT*0.94 - (HEIGHT*0.075/2), WIDTH*0.27, HEIGHT*0.12))
    pygame.draw.rect(screen, color, (WIDTH*0.05, HEIGHT*0.95 - (HEIGHT*0.075/2), WIDTH*0.25*(health[0]/100), HEIGHT*0.075))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()