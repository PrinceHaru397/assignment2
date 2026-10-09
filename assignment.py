import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cartoon Adventure")

font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()

backgrounds = ["Forest", "Ocean", "Space"]
characters = ["Cat", "Robot", "Alien"]

bg_choice = 0
char_choice = 0

player = pygame.Rect(375, 400, 50, 50)
star = pygame.Rect(random.randint(0, 770), 100, 25, 25)

score = 0
game_started = False
running = True


def draw_text(text, x, y):
    image = font.render(text, True, (255, 255, 255))
    screen.blit(image, (x, y))


while running:
    screen.fill((20, 20, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_started and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bg_choice = (bg_choice - 1) % 3
            if event.key == pygame.K_RIGHT:
                bg_choice = (bg_choice + 1) % 3
            if event.key == pygame.K_UP:
                char_choice = (char_choice - 1) % 3
            if event.key == pygame.K_DOWN:
                char_choice = (char_choice + 1) % 3
            if event.key == pygame.K_RETURN:
                game_started = True

    if not game_started:
        draw_text("CARTOON ADVENTURE", 230, 100)
        draw_text("LEFT / RIGHT: Background", 200, 200)
        draw_text("UP / DOWN: Character", 200, 250)
        draw_text("Background: " + backgrounds[bg_choice], 200, 330)
        draw_text("Character: " + characters[char_choice], 200, 380)
        draw_text("Press ENTER to play!", 250, 470)

    else:
        if bg_choice == 0:
            screen.fill((40, 150, 70))
        elif bg_choice == 1:
            screen.fill((30, 130, 210))
        else:
            screen.fill((15, 15, 45))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= 4
        if keys[pygame.K_RIGHT]:
            player.x += 4
        if keys[pygame.K_UP]:
            player.y -= 4
        if keys[pygame.K_DOWN]:
            player.y += 4

        player.clamp_ip(screen.get_rect())

        if char_choice == 0:
            pygame.draw.circle(screen, (255, 180, 120),
                               player.center, 25)
            pygame.draw.circle(screen, (0, 0, 0),
                               (player.x + 17, player.y + 18), 4)
            pygame.draw.circle(screen, (0, 0, 0),
                               (player.x + 33, player.y + 18), 4)
            pygame.draw.arc(screen, (0, 0, 0),
                            (player.x + 15, player.y + 20, 20, 15),
                            3.14, 6.28, 2)

        elif char_choice == 1:
            pygame.draw.rect(screen, (180, 190, 210), player)
            pygame.draw.circle(screen, (0, 255, 255),
                               (player.x + 15, player.y + 18), 5)
            pygame.draw.circle(screen, (0, 255, 255),
                               (player.x + 35, player.y + 18), 5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (player.x + 15, player.y + 33, 20, 4))

        else:
            pygame.draw.circle(screen, (180, 70, 240),
                               player.center, 25)
            pygame.draw.circle(screen, (255, 255, 255),
                               (player.x + 17, player.y + 18), 7)
            pygame.draw.circle(screen, (255, 255, 255),
                               (player.x + 33, player.y + 18), 7)
            pygame.draw.circle(screen, (0, 0, 0),
                               (player.x + 17, player.y + 18), 3)
            pygame.draw.circle(screen, (0, 0, 0),
                               (player.x + 33, player.y + 18), 3)

        pygame.draw.polygon(screen, (255, 220, 0), [
            (star.x + 12, star.y),
            (star.x + 17, star.y + 9),
            (star.x + 25, star.y + 10),
            (star.x + 19, star.y + 17),
            (star.x + 21, star.y + 25),
            (star.x + 12, star.y + 20),
            (star.x + 4, star.y + 25),
            (star.x + 5, star.y + 16),
            (star.x, star.y + 10),
            (star.x + 9, star.y + 9)
        ])

        if player.colliderect(star):
            score += 1
            star.x = random.randint(0, 770)
            star.y = random.randint(50, 550)

        draw_text("Score: " + str(score), 20, 20)
        draw_text("Collect the stars!", 20, 55)

    pygame.display.update()
    clock.tick(60)

pygame.quit()