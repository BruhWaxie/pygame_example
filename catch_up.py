from pygame import *

#створи вікно гри
WIDTH, HEIGHT = 800, 600
FPS = 360

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Доганялки')
clock = time.Clock() #game timer
#задай фон сцени
bg = image.load("background.png")

sprite1_img = image.load('sprite1.png')
sprite2_img = image.load('sprite2.png')

bg = transform.scale(bg, (WIDTH, HEIGHT)) #resize bg

#створи 2 спрайти та розмісти їх на сцені
class GameSprite:
    def __init__(self, sprite_image, width=60, height=60, x=100, y=250):
        self.image = transform.scale(sprite_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, self.rect)
sprite1 = GameSprite(sprite1_img)
sprite2 = GameSprite(sprite2_img, x=400, y=250)

while True:
#оброби подію «клік за кнопкою "Закрити вікно"»
    for e in event.get():
        if e.type == QUIT:
            quit()

    keys = key.get_pressed()
    if keys[K_w]:
        sprite1.rect.y -= 1
    if keys[K_s]:
        sprite1.rect.y += 1
    if keys[K_a]:
        sprite1.rect.x -= 1
    if keys[K_d]:
        sprite1.rect.x += 1    

    if keys[K_UP]:
        sprite2.rect.y -= 1
    if keys[K_DOWN]:
        sprite2.rect.y += 1
    if keys[K_LEFT]:
        sprite2.rect.x -= 1
    if keys[K_RIGHT]:
        sprite2.rect.x += 1

    window.blit(bg, (0,0))
    sprite1.draw(window)
    sprite2.draw(window)

    display.update()
    clock.tick(FPS)
    