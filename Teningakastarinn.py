# imports
import pygame
import random

# litir sem eru notaðir
red = (90,0,0)
green = (0,80,0)
blue = (0,160,255)
white = (255,255,255)
black = (0,0,0)



# Kveikir á pygame og fontinu
pygame.init()
pygame.font.init()

# býr til displayið
pygame.display.set_caption("Teningaspil!")
screen = pygame.display.set_mode((640, 480))
screen_r = screen.get_rect()
font = pygame.font.SysFont('arial', 26) # breyta sem við notum fyrir fontið


class Dice:
    def __init__(self):
        self.number = 0
	# the throw function assumes a six-sided dice
	# containing numbers(dots) from 1 to and including 6
    def throw(self):
        self.number = random.randint(1,6)
        return self.number

class DiceThrower:
    def __init__(self, how_many=5):	# default number of dice is 5
        self.number_of_dice = how_many
        self.dice = Dice()
        self.dice_list = [-1 for i in range(self.number_of_dice)]

	# throws all the dice contained within dice_list
    def throw(self):
        for x in range(0, self.number_of_dice):
            self.dice_list[x] = self.dice.throw()
        return self.dice_list

	# rethrows the dice contained in the rethrow_list
    def rethrow(self, rethrow_list=[]):
        if 0 < len(rethrow_list) <= self.number_of_dice:
            if min(rethrow_list) >= 0 and max(rethrow_list) <= self.number_of_dice - 1:
                for item in rethrow_list:
                    self.dice_list[item] = self.dice.throw()
            return self.dice_list
        else:
            return self.throw()

x = 80
y = 100
die1 = pygame.Rect(190,100, 140,140)
die2 = pygame.Rect(340,100, 140,140)
die3 = pygame.Rect(110,250, 140,140)
die4 = pygame.Rect(260,250, 140,140)
die5 = pygame.Rect(410,250, 140,140)
throw_die = Dice()
player_dice_thrower = DiceThrower()
player_dice = player_dice_thrower.throw()
rethrow_dice = list()
throw_all = pygame.Rect(60,400, 120, 50)
restart = pygame.Rect(260,400, 120, 50)
throw_selected = pygame.Rect(460,400, 120, 50)
play = pygame.Rect(285,210, 120,50)
start = True
running = False
throwAll = False
rethrow_allowed = True
number_of_throws = 0
while start:
    for e in pygame.event.get():#checkar hvort þú lokar glugganum
        if e.type == pygame.QUIT:
            start = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            start = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play.collidepoint(mouse_pos):
                start = False
                running = True

    screen.fill(green)
    pygame.draw.rect(screen,white,play)
    screen.blit(font.render('Spila',1,black),(320,220))
    pygame.display.flip()
while running:#leikurinn sjálfur
    for e in pygame.event.get():#checkar hvort þú lokar glugganum
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if die1.collidepoint(mouse_pos):
                rethrow_dice.append(0)
            if die2.collidepoint(mouse_pos):
                rethrow_dice.append(1)
            if die3.collidepoint(mouse_pos):
                rethrow_dice.append(2)
            if die4.collidepoint(mouse_pos):
                rethrow_dice.append(3)
            if die5.collidepoint(mouse_pos):
                rethrow_dice.append(4)
            if throw_all.collidepoint(mouse_pos):
                player_dice = player_dice_thrower.throw()
                number_of_throws += 1
            if throw_selected.collidepoint(mouse_pos):
                user_dice = player_dice_thrower.rethrow(rethrow_dice)
                del rethrow_dice[:]
                number_of_throws += 1
            if restart.collidepoint(mouse_pos):
                player_dice = player_dice_thrower.throw()
                rethrow_allowed = True
                number_of_throws = 0

    screen.fill(green)
    x = 110
    y = 120
    i = 0

    pygame.draw.rect(screen, white, die1)
    pygame.draw.rect(screen, white, die2)
    pygame.draw.rect(screen, white, die3)
    pygame.draw.rect(screen, white, die4)
    pygame.draw.rect(screen, white, die5)
    screen.blit(font.render(str(player_dice[0]),1,black),(250,150))
    screen.blit(font.render(str(player_dice[1]),1,black),(400,150))
    screen.blit(font.render(str(player_dice[2]),1,black),(170,300))
    screen.blit(font.render(str(player_dice[3]),1,black),(320,300))
    screen.blit(font.render(str(player_dice[4]),1,black),(470,300))
    if number_of_throws == 2:
        rethrow_allowed = False
    if rethrow_allowed == True:
        pygame.draw.rect(screen,white,throw_all)
        screen.blit(font.render('Kasta öllum',1,black),throw_all)
        pygame.draw.rect(screen,white,throw_selected)
        screen.blit(font.render('Kasta aftur',1,black),throw_selected)
    else:
        pygame.draw.rect(screen,white,restart)
        screen.blit(font.render('Spila Aftur?',1,black),restart)
    pygame.display.flip()
