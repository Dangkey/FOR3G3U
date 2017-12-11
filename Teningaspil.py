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


class makeDice(object):

    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0],pos[1], 80,80)

throw_die = Dice()
player_dice_thrower = DiceThrower()
opponent_dice_thrower = DiceThrower()

player_dice = player_dice_thrower.throw()
opponent_dice = opponent_dice_thrower.throw()

show_player_score = 0
player_dice_list = list()
opponent_dice_list = list()
x = 80
y = 100
for die in opponent_dice:
    opponent_dice_list.append(makeDice((x,y)))
    x += 100
x = 80
y = 300
for die in player_dice:
    player_dice_list.append(makeDice((x,y)))
    x += 100
play = pygame.Rect(285,210, 120,50)

throw_all = pygame.Rect(60,400, 120, 50)
throw_one = pygame.Rect(460,400, 120, 50)
restart = pygame.Rect(260,400, 120, 50)
#While loop breytur sem heldur þeim gangandi
for i in range(0,4):
    show_player_score += player_dice[i]
playAgain = False
throwAll = False
throwOne = False
running = False
start = True
end = False
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
            if throw_one.collidepoint(mouse_pos):
                throwOne = True
            if throw_all.collidepoint(mouse_pos):
                player_dice = player_dice_thrower.throw()
                throwAll = True
            if restart.collidepoint(mouse_pos):
                show_player_score = 0
                player_dice = player_dice_thrower.throw()
                opponent_dice = opponent_dice_thrower.throw()
                throwAll = False
                throwOne = False
                playAgain = True
                for i in range(0,4):
                    show_player_score += player_dice[i]
    screen.fill(green)

    for dice in opponent_dice_list:
        pygame.draw.rect(screen, red, dice.rect)
    for dice in player_dice_list:
        pygame.draw.rect(screen, red, dice.rect)
    x = 110
    y = 120
    for die in opponent_dice:
        screen.blit(font.render(str(die),1,white),(x,y))
        x += 100
    x = 110
    y = 320
    if throwOne == True:
        for die in player_dice:
            screen.blit(font.render(str(die),1,white),(x,y))
            x += 100
        if sum(player_dice) > sum(opponent_dice):
            screen.blit(font.render("Congratulations! You Won",1,black),(150,190))
        elif sum(player_dice) == sum(opponent_dice):
            screen.blit(font.render("It was a Tie!",1,black),(150,190))
        else:
            screen.blit(font.render("Unfortunately you lost..",1,black),(150,190))
        show_score = font.render("Player's score : "+ str(sum(player_dice)) + " Opponent's score: "+ str(sum(opponent_dice)),1,black)
        pygame.draw.rect(screen,white,restart)
        screen.blit(font.render('Spila Aftur?',1,black),restart)
    if throwAll == True:
        throwOne = False
        for die in player_dice:
            screen.blit(font.render(str(die),1,white),(x,y))
            x += 100
        if sum(player_dice) > sum(opponent_dice):
            screen.blit(font.render("Congratulations! You Won",1,black),(150,190))
        elif sum(player_dice) == sum(opponent_dice):
            screen.blit(font.render("It was a Tie!",1,black),(150,190))
        else:
            screen.blit(font.render("Unfortunately you lost..",1,black),(150,190))
        show_score = font.render("Player's score : "+ str(sum(player_dice)) + " Opponent's score: "+ str(sum(opponent_dice)),1,black)
        pygame.draw.rect(screen,white,restart)
        screen.blit(font.render('Spila Aftur?',1,black),restart)
    if playAgain == True:
        for die in player_dice:
            screen.blit(font.render(str(die),1,white),(x,y))
            x += 100
        if sum(player_dice) > sum(opponent_dice):
            screen.blit(font.render("Congratulations! You Won",1,black),(150,190))
        elif sum(player_dice) == sum(opponent_dice):
            screen.blit(font.render("It was a Tie!",1,black),(150,190))
        else:
            screen.blit(font.render("Unfortunately you lost..",1,black),(150,190))
        show_score = font.render("Player's score : "+ str(sum(player_dice)) + " Opponent's score: "+ str(sum(opponent_dice)),1,black)
        playAgain = False
    if throwAll == False and throwOne == False:
        for die in player_dice[:-1]:
            screen.blit(font.render(str(die),1,white),(x,y))
            x += 100
        show_score = font.render("Player's score : "+ str(show_player_score) + " Opponent's score: "+ str(sum(opponent_dice)),1,black)
    pygame.draw.rect(screen,white,throw_one)
    screen.blit(font.render('Kasta einum',1,black),throw_one)
    pygame.draw.rect(screen,white,throw_all)
    screen.blit(font.render('Kasta öllum',1,black),throw_all)

    screen.blit(show_score,(150,220))
    pygame.display.flip()
