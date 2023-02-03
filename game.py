[20:24] Lucas Klumper
import pygame
import random
# initialize pygame
pygame.init()
# set up window
screen = pygame.display.set_mode((600, 400))
# game variables
clock = pygame.time.Clock()
player_x = 300
player_y = 300
player_speed = 10
resources = 0
raft_built = False
game_over = False
score = 0
# load player skins
player_images = {
    "skin1": pygame.image.load("player_skin1.png"),
    "skin2": pygame.image.load("player_skin2.png"),
    "skin3": pygame.image.load("player_skin3.png"),
}
# set default player skin
player_image = player_images["skin1"]
# load resources and obstacles
resource_image = pygame.image.load("resource.png")
obstacle_image = pygame.image.load("obstacle.png")
# load music and sound effects
pygame.mixer.music.load("background_music.mp3")
resource_sound = pygame.mixer.Sound("resource_sound.wav")
game_over_sound = pygame.mixer.Sound("game_over_sound.wav")
# play background music
pygame.mixer.music.play(-1)
# list of resources and obstacles
resources_list = [(random.randint(0, 600), random.randint(0, 400)) for i in range(10)]
obstacles = [(random.randint(0, 600), random.randint(0, 400)) for i in range(5)]
# function to handle player skin change
def change_skin(skin):
    global player_image
    player_image = player_images[skin]
# game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                change_skin("skin1")
            elif event.key == pygame.K_2:
                change_skin("skin2")
            elif event.key == pygame.K_3:
                change_skin("skin3")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    for resource in resources_list:
        if (player_x, player_y) == resource:
            resources += 1
            resources_list.remove(resource)
            score += 10
            resource_sound.play()
    for obstacle in obstacles:
        if (player_x, player_y) == obstacle:
            game_over = True
            game_over_sound.play()
    screen.fill((255, 255, 255))

