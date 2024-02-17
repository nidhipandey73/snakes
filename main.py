import pygame
import random

x = pygame.init()

# creating a window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes")
pygame.display.update()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, list, size):
    for x, y in list:
        pygame.draw.rect(gamewindow, (255, 255, 255), [x, y, size, size])

# game loop
def game_loop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    vel_x = 0
    vel_y = 0
    snake_size = 20
    fps = 30  # frame per second
    snk_list = []
    snk_len = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)
    score = 0
    clock = pygame.time.Clock()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill((0, 0, 0))
            text_screen("Game Over! Press enter to continue", (255, 0, 0), 70, screen_height//2 )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x += 7
                        vel_y = 0
                    if event.key == pygame.K_LEFT:
                        vel_x += -7
                        vel_y = 0
                    if event.key == pygame.K_UP:
                        vel_y += -7
                        vel_x = 0
                    if event.key == pygame.K_DOWN:
                        vel_y += 7
                        vel_x = 0
            snake_x += vel_x
            snake_y += vel_y
            if abs(snake_x - food_x) < 18 and abs(snake_y - food_y) < 18:
                score += 10
                snk_len +=1
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                if score>int(hiscore):
                    hiscore = score
            gameWindow.fill((0, 0, 0))
            text_screen("Score: " + str(score) + " Hiscore:" +str(hiscore),(255, 0, 0), 5, 5)
            pygame.draw.rect(gameWindow, (255, 0, 0), [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_len:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
            if snake_x<0 or snake_x>screen_width or snake_y< 0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, (255, 255, 255), snk_list, snake_size)
        clock.tick(fps)
        pygame.display.update()


game_loop()