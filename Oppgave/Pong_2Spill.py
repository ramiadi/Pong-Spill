
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)
import random
# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1000
VINDU_HOYDE  = 600
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


class Spiller:
  #For å representere rektangelet(spilleren) 
  def __init__(self, x, y, farge, bredde, høyde, xFart, yFart, key_up, key_down):
    self.x = x
    self.y = y
    self.farge = farge
    self.bredde = bredde
    self.høyde = høyde
    self.xFart = xFart
    self.yFart = yFart
    self.key_up = key_up
    self.key_down = key_down
  
  def tegn(self):
    #Tegner hinder
    pg.draw.rect(vindu, self.farge, (self.x, self.y, self.bredde, self.høyde))

  def flytt(self, taster):
    #flytte spilleren (hinder)
    if taster[self.key_up] and self.y > 2:  # Legger til en verdi for å hindre spilleren i å gå over øvre kant av vinduet
        self.y -= 1
    elif taster[self.key_down] and self.y + self.høyde < VINDU_HOYDE - 2:  # Legger til en verdi for å hindre spilleren i å gå under nedre kant av vinduet
        self.y += 1

        


class Ball:
    def __init__(self, farge, radius):
        self.radius = radius
        self.x = VINDU_BREDDE / 2
        self.y = VINDU_HOYDE / 2
        self.xfart = random.choice([-0.5, 0.5])
        self.yfart = self.xfart
        self.farge = farge
        self.score1 = 0
        self.score2 = 0
        self.score_font = pg.font.SysFont(None, 100)

    def tegn_sirkel(self):
        pg.draw.circle(vindu, (self.farge), (self.x, self.y), self.radius)

    
    def flytt(self):
        #denne if-testen holder ballen innenfor skjermens høyde
        if self.y - self.radius <= 0 or self.y + self.radius >= VINDU_HOYDE:
            self.yfart = -self.yfart

        if self.x - self.radius <= 0:
            self.score2 += 1
            self.x = VINDU_BREDDE / 2
            self.y = VINDU_HOYDE / 2 
            self.xfart = 0.5
            self.yfart = random.uniform(-1, 1)

        if self.x + self.radius >= VINDU_BREDDE:
            self.score1 += 1
            self.x = VINDU_BREDDE / 2
            self.y = VINDU_HOYDE / 2
            self.xfart = -0.5
            self.yfart = random.uniform(-1, 1)
            
        self.x += self.xfart
        self.y += self.yfart
        self.player1_score = self.score_font.render(str(self.score1), True, self.farge)
        self.player2_score = self.score_font.render(str(self.score2), True, self.farge)
    
    def tegn_score(self):
        vindu.blit(self.player1_score,(VINDU_BREDDE / 4, VINDU_HOYDE / 8))
        vindu.blit(self.player2_score,(VINDU_BREDDE - 250, VINDU_HOYDE / 8))


    def sjekk_kollisjon(self, spiller, spiller2):
        if (self.x + self.radius > spiller.x and
            self.x - self.radius < spiller.x + spiller.bredde and
            self.y + self.radius > spiller.y and
            self.y - self.radius < spiller.y + spiller.høyde):
                self.xfart = -self.xfart
                if self.y < spiller.y + spiller.høyde/2:
                    self.yfart -= 0.1 
                else:
                    self.yfart += 0.1  
                self.xfart *= 1.1
                self.yfart *= 1.1

        if (self.x + self.radius > spiller2.x and
            self.x - self.radius < spiller2.x + spiller2.bredde and
            self.y + self.radius > spiller2.y and
            self.y - self.radius < spiller2.y + spiller2.høyde):
                self.xfart = -self.xfart
                if self.y < spiller2.y + spiller2.høyde/2:
                    self.yfart -= 0.1  
                else:
                    self.yfart += 0.1  
                self.xfart *= 1.1
                self.yfart *= 1.1
    
# Lager et Spiller-objekt
spiller = Spiller(5, VINDU_HOYDE - 400, (255, 255, 255), 10, 175, 1, 0, K_w, K_s)
spiller2 = Spiller(VINDU_BREDDE - 15, VINDU_HOYDE - 400, (255, 255, 255), 10, 175, 1, 0, K_UP, K_DOWN)
#Ball objekt
ball1 = Ball((255, 255, 255), 10)

#Sett tittel og bilde
pg.display.set_caption("Pong spill")
icon = pg.image.load("pong_bilde.jpg")
pg.display.set_icon(icon)


# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen svart
    vindu.fill((0, 0, 0))

    # Tegner og flytter spiller og hinder
    spiller.tegn()
    spiller.flytt(trykkede_taster)
    spiller2.tegn()
    spiller2.flytt(trykkede_taster)
    ball1.tegn_sirkel()
    ball1.flytt()
    ball1.sjekk_kollisjon(spiller, spiller2)

    # -- Feltet --#
    pg.draw.line(vindu, (255, 255, 255), (VINDU_BREDDE /2, 0), (VINDU_BREDDE / 2, VINDU_HOYDE))
    pg.draw.circle(vindu, (255, 255, 255), (VINDU_BREDDE // 2, VINDU_HOYDE // 2), 80, 1)
    ball1.tegn_score()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()