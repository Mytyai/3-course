

class Settings():
    """Класс для хранения настроек игры."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        
        self.screen_widht = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.background_image = 'images/background.bmp'
        self.background_rect = None

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (135, 206, 235)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 30
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует динамические настройки игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 1.5

        self.fleet_direction = 1

        self.alien_points = 50
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

