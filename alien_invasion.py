import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
# from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import sound_effects as se 
 

class AlienInvasion:

   def run_game():    

   #Initialize game and create a screen object.
      pygame.init()
      screen = pygame.display.set_mode((1200, 800))

      ai_settings = Settings()
      screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
      ai_settings.bullet_color = ('white')
      pygame.display.set_caption("Alien Invasion")

      # Make the Play button.
      play_button = Button(ai_settings, screen, "Play")
      se.bg_sound.play()


      # Create an instance to store game statistics and create a scoreboard.
      stats = GameStats(ai_settings)
      sb = Scoreboard(ai_settings, screen, stats)

      # Set the background color.

      ship = Ship(ai_settings, screen)
      # Make a group to store bullets in.
      bullets = Group()
      aliens = Group()

      # Create the fleet of aliens.
      gf.create_fleet(ai_settings, screen, ship, aliens)

      # alien = Alien(ai_settings, screen)


   # Start the main loop for the game.
      while True:

         gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

         gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
   # Watch for keyboard and mouse events.
         
         if stats.game_active:
            
            ship.update()
         
         #   print(len(bullets))
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
         
   run_game()