import pygame
import sys
import math
from random import randint, choice

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OOP Assignment: Superheroes and Vehicles")

# Colors
BACKGROUND = (20, 30, 50)
TEXT_COLOR = (220, 220, 220)
HIGHLIGHT = (255, 215, 0)

# Fonts
font_large = pygame.font.SysFont("Arial", 32, bold=True)
font_medium = pygame.font.SysFont("Arial", 24)
font_small = pygame.font.SysFont("Arial", 18)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Assignment 1: Superhero Class with Inheritance
class Superhero:
    def __init__(self, name, secret_identity, power_level, color, x, y):
        self.name = name
        self.secret_identity = secret_identity
        self.power_level = power_level
        self.color = color
        self.x = x
        self.y = y
        self.size = 60
        self.speed = 2
        self.direction = 1

    def use_power(self):
        return f"{self.name} uses their power at level {self.power_level}!"

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.size, 2)
        
        # Draw emblem
        pygame.draw.polygon(surface, (255, 255, 0), [
            (self.x, self.y - 15),
            (self.x - 10, self.y + 10),
            (self.x + 10, self.y + 10)
        ])
        
        # Draw name
        text = font_small.render(self.name, True, TEXT_COLOR)
        surface.blit(text, (self.x - text.get_width() // 2, self.y + self.size + 5))

    def move(self):
        self.x += self.speed * self.direction
        if self.x > WIDTH - self.size or self.x < self.size:
            self.direction *= -1

# Inherited class
class TechHero(Superhero):
    def __init__(self, name, secret_identity, power_level, color, x, y, gadget):
        super().__init__(name, secret_identity, power_level, color, x, y)
        self.gadget = gadget
        self.size = 50

    def use_power(self):
        return f"{self.name} uses {self.gadget} at technological level {self.power_level}!"

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x - self.size, self.y - self.size, self.size * 2, self.size * 2), 0, 10)
        pygame.draw.rect(surface, (200, 200, 200), (self.x - self.size, self.y - self.size, self.size * 2, self.size * 2), 3, 10)
        
        # Draw tech emblem
        pygame.draw.circle(surface, (0, 150, 255), (self.x, self.y), 15, 3)
        pygame.draw.circle(surface, (0, 150, 255), (self.x, self.y), 10, 2)
        
        # Draw name
        text = font_small.render(self.name, True, TEXT_COLOR)
        surface.blit(text, (self.x - text.get_width() // 2, self.y + self.size + 5))

# Assignment 2: Polymorphism with Vehicles
class Vehicle:
    def __init__(self, name, x, y, color):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.speed = randint(2, 5)

    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

    def draw(self, surface):
        raise NotImplementedError("Subclasses must implement draw()")

class Car(Vehicle):
    def __init__(self, x, y):
        super().__init__("Car", x, y, (220, 50, 50))

    def move(self):
        self.x += self.speed
        if self.x > WIDTH + 50:
            self.x = -50

    def draw(self, surface):
        # Car body
        pygame.draw.rect(surface, self.color, (self.x - 30, self.y - 15, 60, 30), 0, 5)
        pygame.draw.rect(surface, (50, 50, 50), (self.x - 20, self.y - 20, 40, 10), 0, 3)
        
        # Wheels
        pygame.draw.circle(surface, (30, 30, 30), (self.x - 15, self.y + 15), 8)
        pygame.draw.circle(surface, (30, 30, 30), (self.x + 15, self.y + 15), 8)
        
        # Draw vehicle name
        text = font_small.render(self.name, True, TEXT_COLOR)
        surface.blit(text, (self.x - text.get_width() // 2, self.y - 40))

class Airplane(Vehicle):
    def __init__(self, x, y):
        super().__init__("Airplane", x, y, (180, 180, 180))

    def move(self):
        self.x += self.speed
        if self.x > WIDTH + 100:
            self.x = -100

    def draw(self, surface):
        # Airplane body
        pygame.draw.ellipse(surface, self.color, (self.x - 40, self.y - 10, 80, 20))
        pygame.draw.polygon(surface, self.color, [
            (self.x + 30, self.y),
            (self.x + 50, self.y - 10),
            (self.x + 50, self.y + 10)
        ])
        
        # Wings
        pygame.draw.polygon(surface, (150, 150, 150), [
            (self.x, self.y),
            (self.x - 10, self.y - 20),
            (self.x + 10, self.y - 20)
        ])
        
        # Draw vehicle name
        text = font_small.render(self.name, True, TEXT_COLOR)
        surface.blit(text, (self.x - text.get_width() // 2, self.y - 40))

class Boat(Vehicle):
    def __init__(self, x, y):
        super().__init__("Boat", x, y, (100, 80, 40))

    def move(self):
        self.x += self.speed - 1  # Boats are slower
        if self.x > WIDTH + 80:
            self.x = -80

    def draw(self, surface):
        # Boat body
        pygame.draw.polygon(surface, self.color, [
            (self.x - 40, self.y + 10),
            (self.x + 40, self.y + 10),
            (self.x + 30, self.y - 10),
            (self.x - 30, self.y - 10)
        ])
        
        # Mast
        pygame.draw.rect(surface, (80, 80, 80), (self.x - 3, self.y - 25, 6, 25))
        
        # Sail
        pygame.draw.polygon(surface, (220, 220, 220), [
            (self.x, self.y - 25),
            (self.x, self.y - 5),
            (self.x + 20, self.y - 15)
        ])
        
        # Draw vehicle name
        text = font_small.render(self.name, True, TEXT_COLOR)
        surface.blit(text, (self.x - text.get_width() // 2, self.y - 50))

# Create superheroes
superheroes = [
    Superhero("Superman", "Clark Kent", 95, (0, 100, 200), 200, 150),
    Superhero("Wonder Woman", "Diana Prince", 90, (200, 20, 20), 400, 150),
    Superhero("Batman", "Bruce Wayne", 85, (40, 40, 40), 600, 150),
    TechHero("Iron Man", "Tony Stark", 92, (200, 50, 50), 800, 150, "Repulsor Rays")
]

# Create vehicles
vehicles = [
    Car(100, 450),
    Airplane(300, 450),
    Boat(500, 450)
]

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Display power usage when space is pressed
                for hero in superheroes:
                    print(hero.use_power())
    
    # Clear the screen
    screen.fill(BACKGROUND)
    
    # Draw title
    title = font_large.render("OOP Assignment: Superheroes and Vehicles", True, HIGHLIGHT)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
    
    # Draw section headers
    superhero_header = font_medium.render("Superheroes (Assignment 1)", True, (70, 170, 255))
    screen.blit(superhero_header, (WIDTH // 2 - superhero_header.get_width() // 2, 70))
    
    poly_header = font_medium.render("Polymorphism Challenge (Assignment 2)", True, (70, 170, 255))
    screen.blit(poly_header, (WIDTH // 2 - poly_header.get_width() // 2, 350))
    
    # Draw instructions
    instructions = font_small.render("Press SPACE to see superhero powers in the console", True, TEXT_COLOR)
    screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT - 40))
    
    # Update and draw superheroes
    for hero in superheroes:
        hero.move()
        hero.draw(screen)
    
    # Update and draw vehicles
    for vehicle in vehicles:
        vehicle.move()
        vehicle.draw(screen)
    
    # Draw movement labels
    for i, vehicle in enumerate(vehicles):
        move_type = "Driving" if isinstance(vehicle, Car) else "Flying" if isinstance(vehicle, Airplane) else "Sailing"
        move_text = font_small.render(f"move(): {move_type}", True, (150, 255, 150))
        screen.blit(move_text, (50 + i * 250, 520))
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(60)