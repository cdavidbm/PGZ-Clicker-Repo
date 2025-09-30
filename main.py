#pgzero

WIDTH = 600
HEIGHT = 400
TITLE = "Clicker animal"
FPS = 30

# Objetos
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
play = Actor("play", (300, 100))

# Variables
count = 0
mode = "menu"

def draw():
    if mode == "game":
        background.draw()
        animal.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("+1$ cada 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text("PRECIO: 15$", center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+15$ cada 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text("PRECIO: 200$", center=(450, 210), color="black", fontsize = 20)
    elif mode == "menu":
        background.draw()
        play.draw()

def on_mouse_down(button, pos):
    global count
    if button == mouse.LEFT and animal.collidepoint(pos):
        count += 1
        animal.y = 200
        animate(animal, tween="bounce_end", duration=0.3, y=250)
    elif button == mouse.LEFT and bonus_1.collidepoint(pos):
        if count >= 15:
            schedule_interval(for_bonus_1, 2)
            count -= 15
    elif button == mouse.LEFT and bonus_2.collidepoint(pos):
        if count >= 200:
            schedule_interval(for_bonus_2, 2)
            count -= 200
 
def for_bonus_1():
    global count
    count += 1

def for_bonus_2():
    global count
    count += 15
