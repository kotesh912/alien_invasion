import sys
import  pygame
from settings import Settings
from ship import Ship

class AlienInvansion:
    """overall class to manage game asserts and behavior"""

    def __init__(self):
        """initialize the game and create the game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("mokshith the don")

        self.ship = Ship(self)

        # set backgroud color
        #self.bg_color = (255,0,0)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loo p.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run game
    ai =AlienInvansion()
    ai.run_game()