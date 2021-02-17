from os import supports_effective_ids


class Settings:
    """A class to store all of our setting for Alien Invasion."""

    def __init__(self):
        """Initializes the game's STATIC settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 230, 230)
        # Ship settings 
        self.ship_limit = 3
        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 5
        # Alien settings
        self.fleet_drop_speed = 10
        self.alien_points = 100 # Scoring
        # How quickly the game speeds up 
        self.speedup_scale = 1.1
        # How quickly the alien pints increase in value
        self.score_scale = 1.5

        self.initialize_dynamic_settings() 

    def initialize_dynamic_settings(self):
        """Initialize settings that will change"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.5

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1 

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

