# Pygame
import pygame


class Main:
    screen_width = 800
    screen_height = 600
    fps = 60

    @classmethod
    def run(cls):
        # Game loop
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((cls.screen_width, cls.screen_height))
        pygame.display.set_caption("My Game")
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update game state

            # Render game graphics
            screen.fill((0, 0, 0))  # Fill the screen with black
            # Add your drawing code here

            # Update the screen
            pygame.display.flip()

            clock.tick(cls.fps)

        # Quit the game
        pygame.quit()


if __name__ == '__main__':
    Main.run()
