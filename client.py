import pygame
from network import Network

width = 800
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, window):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.draw.rect(window, self.color, self.rect)
            
        if keys[pygame.K_w]:
            pygame.draw.rect(window, self.color, self.rect)

        if keys[pygame.K_e]:
            pygame.draw.rect(window, self.color, self.rect)

        if keys[pygame.K_r]:
            pygame.draw.rect(window, self.color, self.rect)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.vel
            
        if keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_s]:
            self.y += self.vel

        if keys[pygame.K_d]:
            self.x += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(pos_str):
    pos = pos_str.split(",")
    return int(pos[0]), int(pos[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def main():
    running = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)  # Cap at 60 frames

        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        p.move()
        redrawWindow(window, p, p2)

main()