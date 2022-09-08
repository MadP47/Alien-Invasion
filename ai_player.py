from alien_invasion import AlienInvasion
import pygame

class AIPlayer:

    def __init__(self, ai_game):                                        # 1
        """Automatic player for Alien Invasion."""

        # Need a reference to the game object.
        self.ai_game = ai_game                                          # 2

    def run_game(self):                                                 # 3
        """Replaces the original run_game(), so we can interject our own
        controls.
        """

        # Start out in an active state.
        self.ai_game.stats.game_active = True                         # 4
        pygame.mouse.set_visible(False)  

        # Start the main loop for the game.
        while True:                                                     # 5
            # Still call ai_game._check_events(), so we can use keyboard to
            #   quit.
            self.ai_game._check_events()

             # Sweep the ship right and left continuously.
            ship = self.ai_game.ship                                    # 1
            screen_rect = self.ai_game.screen.get_rect()

            if not ship.moving_right and not ship.moving_left:          # 2
                # Ship hasn't started moving yet; move to the right.
                ship.moving_right = True
            elif (ship.moving_right
                        and ship.rect.right > screen_rect.right - 10):  # 3
                # Ship about to hit right edge; move left.
                ship.moving_right = False
                ship.moving_left = True
            elif ship.moving_left and ship.rect.left < 10:              # 4
                ship.moving_left = False
                ship.moving_right = True

            if self.ai_game.stats.game_active:
                self.ai_game.ship.update()
                self.ai_game._update_bullets()
                self.ai_game._update_aliens()
                self.ai_game._fire_bullet()  

            self.ai_game._update_screen()

if __name__ == '__main__':
    ai_game = AlienInvasion()

    ai_player = AIPlayer(ai_game)
    ai_player.run_game()