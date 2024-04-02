import pygame
import sys

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FONT = pygame.font.Font(None, 36)

def draw_text(surface, text, color, x, y):
    text_surface = FONT.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Bounceing Ball Game')

    clock = pygame.time.Clock()

    paddle_image = pygame.image.load('paddle.png')
    paddle_rect = paddle_image.get_rect()
    paddle_rect.centerx = SCREEN_WIDTH // 2
    paddle_rect.bottom = SCREEN_HEIGHT - 20

    ball_image = pygame.image.load('ball.png')
    ball_rect = ball_image.get_rect()
    ball_rect.center = paddle_rect.midtop

    ball_velocity = [6, -8] # Changes the balls speed in the x and y.

    bounce_count = 0

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_rect.left > 0:
            paddle_rect.x -= 5
        if keys[pygame.K_RIGHT] and paddle_rect.right < SCREEN_WIDTH:
            paddle_rect.x += 5

        # Moves the ball.
        ball_rect.x += ball_velocity[0]
        ball_rect.y += ball_velocity[1]

        # Bouncec the ball off the walls.
        if ball_rect.left < 0 or ball_rect.right > SCREEN_WIDTH:
            ball_velocity[0] = -ball_velocity[0]
        if ball_rect.top < 0:
            ball_velocity[1] = -ball_velocity[1]

        # Bounces the ball off the paddle.
        if ball_rect.colliderect(paddle_rect):
            if ball_velocity[1] > 0: 
                ball_velocity[1] = -ball_velocity[1]
            bounce_count += 1

        # Checks to see if the ball hits the ground.
        if ball_rect.bottom > SCREEN_HEIGHT:
            draw_text(screen, "Game Over", BLACK, 350, 250)
            draw_text(screen, f"Bounces: {bounce_count}", BLACK, 350, 300)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        # Draws the paddle and the ball as rectangles. 
        screen.blit(paddle_image, paddle_rect)
        screen.blit(ball_image, ball_rect)

        # Draws the number of bounces counter in text.
        draw_text(screen, f"Bounces: {bounce_count}", BLACK, 10, 10)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main() 