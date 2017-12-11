# imports
import pygame

# litir sem eru notaðir
red = (255,0,0)
green = (0,255,0)
blue = (0,160,255)
white = (255,255,255)
black = (0,0,0)

gateColor = red # setur rauðan lit á útganginn
# breytur fyrir score og hve marga defusers maður er með
score = 2
defuserCount = 0
# class fyrir playerinn
class Player(object):
    #býr til player rect
    def __init__(self):
        self.rect = pygame.Rect(0, 248, 20, 16)
    #hreyfir playerinn
    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        # global breytur
        global defuserCount
        global score
        global gateColor
        # Hreyfir playerinn
        self.rect.x += dx
        self.rect.y += dy
        # Passar að playerinn kemst ekki í gegnum veggi
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                if dx > 0:
                    self.rect.right = brick.rect.left
                if dx < 0:
                    self.rect.left = brick.rect.right
                if dy > 0:
                    self.rect.bottom = brick.rect.top
                if dy < 0:
                    self.rect.top = brick.rect.bottom
        #checkar hvort playerinn tekur upp defuser, tekur hann af mappinu og lækkar score-ið
        for defuser in defusers:
            if self.rect.colliderect(defuser.rect):
                if score > 1:
                    defusers.remove(defuser)
                    defuserCount += 1
                    score -= 2
                    pygame.display.flip()
        # breytir litnum á leiðinni út eftir hvort maður komist út
        if score >= 15:
            gateColor = green
        else:
            gateColor = red
# Class sem er notaður til að búa til veggina
class Brick(object):

    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 20, 16)
# Býr til sprengjuvarnir
class Defuser(object):

    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0],pos[1],20,16)
# Býr til sprengjur
class Bomb(object):

    def __init__(self,pos):
        self.rect = pygame.Rect(pos[0],pos[1],20,16)
# Kveikir á pygame og fontinu
pygame.init()
pygame.font.init()

# býr til displayið
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((640, 520))
screen_r = screen.get_rect()

# kveikir á klukku sem er notað til að telja niður
clock = pygame.time.Clock()
frame_count = 0
frame_rate = 60
start_time = 90

bricks = list()    # Listi sem heldur utan um veggina
defusers = list() #listi sem heldur utan um sprengjuvarnir
bombs = list() #listi til að halda utan um sprengjur
player = Player()   # býr til playerinn



font = pygame.font.SysFont('arial', 30) # breyta sem við notum fyrir fontið
# Textar sem eru notaðir í leiknum
gameInfo = font.render('Collect Defusers to defuse bombs to make it to the end!', 1, white)
startGame = font.render('Press any key to start', 1, white)
playerLost = font.render('Game Over!',1,red)
playerWon = font.render('Congratulations!, You won',1,green)
# Býr til maze, # eru veggir, - er gönguleið, X er sprengjur, O eru sprengjuvarnir, E er útgönguleið
maze = [
"################################",
"#--------------X#---------#----#",
"#-#####-#-#####-#######-#-####-#",
"#-#---#-#---#O#-#---#X--#------#",
"#-#-#-#-###-#-#-#-#-#-##########",
"#O#-#-#---#-#-#-#-#-#----------#",
"###-#-###-#-#-#-#-#-#-########-#",
"#---#---#O#-#-#---#-#O#----#---#",
"#-#####-##--#-#####-###-##-#-###",
"#-#---#-#--##-----------##-#---#",
"#-###-X-##--##############-###-#",
"#----#-####-#-----#----------#-#",
"####-#-#----#-#-#-##########-#-#",
"---O-#-#-####-###-#---#---#--#-#",
"#####--#-#----#-#---#---#--#-#-#",
"#-----#--#-####-##########-#-#-#",
"#-#####-#---#-----#X--#----#-#-#",
"#-#-----#-#####-#-###-#-####-#-#",
"#-#-#-#-#-#-----#-----#-#O-#-#-#",
"#-#-#-###-#-#####-#####-##-#-#-#",
"#-#-#-#---#----#--#O----#--#-#-#",
"#-#-###-#-##-#-#-#-######-##-#-#",
"#-#-----#X---#-#----O#----#----#",
"#-#-#####-##-#-########-######-#",
"#-#--------#-#--------#----#---#",
"#-##########-########-####-#-###",
"#-#-------#O-#--------#----#-#-#",
"#-#-#####-####-########-####-#-#",
"#----#---------#---------------#",
"##############################E#",
]

x = 0 #x hnitin sem við notum fyrir allt í maze-inu
y = 40 #y hnitin sem við notum fyrir allt í maze-inu
for row in maze: #fyrir hverja röð í arrayinum
    for col in row: # fyrir hvern staf í röðinni
        if col == "#":
            bricks.append(Brick((x, y)))
        if col == "E":
            end_rect = pygame.Rect(x, y, 20, 16)
        if col == "O":
            defusers.append(Defuser((x,y)))
        if col == "X":
            bombs.append(Bomb((x,y)))
        x += 20# fer hægri um eitt item
    y += 16#fer niður um eina línu
    x = 0# fer í fyrsta plássið

#While loop breytur sem heldur þeim gangandi
start = True
running = False
lost = False
win = False
while start:#start screen með lýsingu á leiknum
    screen.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            start = False
            running = False
        if e.type == pygame.KEYDOWN:
            start = False
            running = True
        if e.type == pygame.MOUSEBUTTONDOWN:
            start = False
            running = True
    screen.blit(gameInfo, (15,200))
    screen.blit(startGame, (205,230))
    pygame.display.flip()
while running:#leikurinn sjálfur
    for e in pygame.event.get():#checkar hvort þú lokar glugganum
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # hreyfir þig eftir hvaða takka þú ýtir á
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-4, 0)
    if key[pygame.K_RIGHT]:
        player.move(4, 0)
    if key[pygame.K_UP]:
        player.move(0, -4)
    if key[pygame.K_DOWN]:
        player.move(0, 4)

    # Ef þú ferð í útganginn með allavega 15 stig þá vinnuru
    if player.rect.colliderect(end_rect) and score >= 15:
        running = False
        win = True
    for bomb in bombs: # fyrir hverja sprengu í listanum af sprengjunum
        if player.rect.colliderect(bomb.rect) and defuserCount == 0: #ef þú snertir sprengju og ert ekki með sprengjuvörn þá deyrðu
            running = False
            lost = True
        elif player.rect.colliderect(bomb.rect) and defuserCount > 0: #ef þú snertir sprengju og ert með sprengjuvörn þá hverfur sprengjan og þú færð 5 stig
            bombs.remove(bomb)
            defuserCount -= 1
            score += 5
            pygame.display.flip()

    screen.fill(white)
    displayScore = font.render('Score: ' + str(score)+ ' Defusers: ' + str(defuserCount),1, black)
    screen.blit(displayScore, (0,0))#Sýnir stigin
    # every brick in the walls is drawn
    for brick in bricks:
        pygame.draw.rect(screen, black, brick.rect)#teiknar veggina
    for defuser in defusers:
        pygame.draw.rect(screen, blue, defuser.rect)#teiknar sprengjuvarnir
    for bomb in bombs:
        pygame.draw.rect(screen, red, bomb.rect)#teiknar sprengjur


    pygame.draw.rect(screen, gateColor, end_rect)#teiknar útganginn
    pygame.draw.rect(screen, (130, 0, 200), player.rect)#teiknar playerinn
    player.rect.clamp_ip(screen_r)#festir playerinn á skjánum
    #Telur niður í eina og hálfa mínútu
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    time_string = "Time: {0:02}:{1:02}".format(minutes,seconds)
    if minutes == 0 and seconds <= 30:#textinn verður rauður þegar það er hálf mínúta eftir
        time_left = font.render(time_string,1,red)
    else:#annars er hann svartur
        time_left = font.render(time_string,1,black)

    if minutes == 0 and seconds == 0:#ef tíminn er búinn þá tapar þú
        running = False
        lost = True
    screen.blit(time_left, (500,0))#sýnir hvað er mikið eftir
    frame_count += 1
    clock.tick(frame_rate)
    pygame.display.flip()
while win:#það sem kemur ef maður vinnur
    screen.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            win = False
        if e.type == pygame.KEYDOWN:
            win = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            win = False
    screen.blit(playerWon, (180,200))
    pygame.display.flip()
while lost:#það sem kemur ef maður tapar
    screen.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            lost = False
        if e.type == pygame.KEYDOWN:
            lost = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            lost = False
    screen.blit(playerLost, (240,200))
    pygame.display.flip()
