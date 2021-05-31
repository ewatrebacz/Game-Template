import pygame
import time
import random
import os

pygame.init()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)
blue = (102, 179, 225)
brown = (153, 102, 51)
color_light = (170,170,170) 
color_dark = (100,100,100) 
            

#game parametrs
screen_width = 600
screen_height = 500
snake_part = 10 
snake_velocity = 15
font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('comicsans', 35)
smallfont = pygame.font.SysFont('comicsans',35) 
bigfont = pygame.font.SysFont('comicsans', 60)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

#images
image = pygame.image.load('IMG/author.jpg')
author_text = pygame.image.load('IMG/author_text.png')
snake_image = pygame.image.load('IMG/snake_image.jpg')
background = pygame.image.load('IMG/snake_back_image.jpg')
top10_image = pygame.image.load('IMG/top10_image.jpg')
easy_rules_image = pygame.image.load('IMG/easy_rules.png')
hard_rules_image = pygame.image.load('IMG/hard_rules.png')
game_over_image = pygame.image.load('IMG/game_over.jpg')

#sounds
eat_sound = pygame.mixer.Sound('Sounds/eat.wav')
lost_life_sound =  pygame.mixer.Sound('Sounds/lost_life.wav')
game_over_sound = pygame.mixer.Sound('Sounds/game_over.wav')

def snake(snake_part, whole_snake):
    """Draws snake.
@param snake_part:(inf) size of one snake's part

@param whole_snake:(list) list of all snake's parts"""
    for i in whole_snake:
        pygame.draw.rect(screen, green, [i[0], i[1], snake_part, snake_part])

def game_over_screen():
    """Draws game over screen, paly again button, back to menu button and quit button,
    makes buttons lighter when mouse points on them. """
    screen.blit(game_over_image,(0,0))

    back = smallfont.render('back to menu', True ,black)
    play_again = smallfont.render('play again' ,True ,black)
    quit_button = smallfont.render('quit', True, black)

    mouse = pygame.mouse.get_pos()
            
    if 0 <= mouse[0] <= 120 and 0 <= mouse[1] <= 50: 
        pygame.draw.rect(screen,color_light,[0,0,170,40])
        pygame.draw.rect(screen,color_dark,[25,screen_height-60,180,40])
        pygame.draw.rect(screen,color_dark,[screen_width-125,screen_height-60,100,40])
    elif 25 <= mouse[0] <= 205 and screen_height-60 <= mouse[1] <= screen_height-20:
        pygame.draw.rect(screen,color_dark,[0,0,170,40])
        pygame.draw.rect(screen,color_light,[25,screen_height-60,180,40])
        pygame.draw.rect(screen,color_dark,[screen_width-125,screen_height-60,100,40])
    elif screen_width-125 <= mouse[0] <= screen_width-25 and screen_height-60 <= mouse[1] <= screen_height-20:
        pygame.draw.rect(screen,color_dark,[0,0,170,40])
        pygame.draw.rect(screen,color_dark,[25,screen_height-60,180,40])
        pygame.draw.rect(screen,color_light,[screen_width-125,screen_height-60,100,40])
    else:
        pygame.draw.rect(screen,color_dark,[0,0,170,40])
        pygame.draw.rect(screen,color_dark,[25,screen_height-60,180,40])
        pygame.draw.rect(screen,color_dark,[screen_width-125,screen_height-60,100,40])

    screen.blit(back , (5,5))
    screen.blit(play_again, (50, screen_height-55))
    screen.blit(quit_button, (screen_width-100, screen_height-55))

    pygame.display.update()

def show_score(score):
    """Shows score on the screen.
@param score:(int) Player's score"""
    show = score_font.render(f"Your score: {str(score)}", True, blue)
    screen.blit(show, [0, 0])

def show_life(life):
    """Shows how many lives Player's has.

@param life:(int) number of lives (1, 2 or 3)"""
    start_x = screen_width - 15
    start_y = 15
    if life == 3:
        points1 = [(start_x,start_y), (start_x-5,start_y-5),(start_x-10,start_y),(start_x,start_y+10),(start_x+10,start_y),(start_x+5,start_y-5)]
        points2 = [(start_x-25,start_y), (start_x-30,start_y-5),(start_x-35,start_y),(start_x-25,start_y+10),(start_x-15,start_y),(start_x-20,start_y-5)]
        points3 = [(start_x-50,start_y), (start_x-55,start_y-5),(start_x-60,start_y),(start_x-50,start_y+10),(start_x-40,start_y),(start_x-45,start_y-5)]
        pygame.draw.polygon(screen,red,points1,0)
        pygame.draw.polygon(screen,red,points2,0)
        pygame.draw.polygon(screen,red,points3,0)
    elif life == 2:
        points1 = [(start_x,start_y), (start_x-5,start_y-5),(start_x-10,start_y),(start_x,start_y+10),(start_x+10,start_y),(start_x+5,start_y-5)]
        points2 = [(start_x-25,start_y), (start_x-30,start_y-5),(start_x-35,start_y),(start_x-25,start_y+10),(start_x-15,start_y),(start_x-20,start_y-5)]
        pygame.draw.polygon(screen,red,points1,0)
        pygame.draw.polygon(screen,red,points2,0)
    else:
        points1 = [(start_x,start_y), (start_x-5,start_y-5),(start_x-10,start_y),(start_x,start_y+10),(start_x+10,start_y),(start_x+5,start_y-5)]
        pygame.draw.polygon(screen,red,points1,0)

def start_screen():
    """Shows main menu on the screen, makes buttons lighter when mouse points on them."""
    screen.blit(background,(0,0))

    text1 = smallfont.render('quit' , True , black)
    text2 = smallfont.render('about author', True, black) 
    text3 = smallfont.render('start', True, black)
    text4 = smallfont.render('best scores', True, black)

    mouse = pygame.mouse.get_pos()
    
    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-20 <= mouse[1] <= screen_height/2+20: 
        pygame.draw.rect(screen,color_light,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-90,screen_height/2-65,180,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-80,screen_height/2+25,160,40])

    elif screen_width/2-90 <= mouse[0] <= screen_width+90 and screen_height/2-65 <= mouse[1] <= screen_height/2-25:
        pygame.draw.rect(screen,color_light,[screen_width/2-90,screen_height/2-65,180,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-80,screen_height/2+25,160,40]) 

    elif screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-140 <= mouse[1] <= screen_height/2-70:
        pygame.draw.rect(screen,color_light,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-90,screen_height/2-65,180,40]) 
        pygame.draw.rect(screen,color_dark,[screen_width/2-80,screen_height/2+25,160,40])

    elif screen_width/2-80 <= mouse[0] <= screen_width/2+80 and screen_height/2+25 <= mouse[1] <= screen_height/2+65:
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-90,screen_height/2-65,180,40]) 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_light,[screen_width/2-80,screen_height/2+25,160,40])

    else: 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-90,screen_height/2-65,180,40]) 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-80,screen_height/2+25,160,40])
      
    screen.blit(text1 , (screen_width/2-25,screen_height/2-15)) 
    screen.blit(text2, (screen_width/2-75,screen_height/2-60))
    screen.blit(text3 , (screen_width/2-30,screen_height/2-105)) 
    screen.blit(text4 , (screen_width/2-65,screen_height/2+30)) 

    pygame.display.update()

def author_screen():
    """Shows photo of the author and a note from the author about the game,
    draws back to menu button and make it lighter when mouse points on it."""
    screen.fill(white)
    screen.blit(image, (screen_width/2-60, 40))
    screen.blit(author_text, (110, 170))
    back = smallfont.render('back to menu' , True , black)
    mouse = pygame.mouse.get_pos()
            
    if 0 <= mouse[0] <= 120 and 0 <= mouse[1] <= 50: 
        pygame.draw.rect(screen,color_light,[0,0,170,40])
    else:
        pygame.draw.rect(screen,color_dark,[0,0,170,40])
    screen.blit(back , (5,5))

    pygame.display.update()

def difficulty_screen():
    """Shows menu to choose the level of difficulty, shows image of snake,
    draws back to menu button and make it lighter when mouse points on it."""

    choose = bigfont.render('Choose level of difficulty' , True , black)
    back = smallfont.render('back to menu' , True , black)
    text1= smallfont.render('easy' , True , black)
    text2 = smallfont.render('hard', True, black) 
    text3 = smallfont.render('duo', True, black)

    screen.fill(white)
    screen.blit(choose , (screen_width/2-250, 75)) 
    screen.blit(snake_image, (screen_width/2-90, screen_height-160))

    mouse = pygame.mouse.get_pos()

    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-20 <= mouse[1] <= screen_height/2+20: 
        pygame.draw.rect(screen,color_light,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-65,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40]) 
        pygame.draw.rect(screen,color_dark,[0,0,170,40]) 

    elif screen_width/2-90 <= mouse[0] <= screen_width+90 and screen_height/2-65 <= mouse[1] <= screen_height/2-25:
        pygame.draw.rect(screen,color_light,[screen_width/2-50,screen_height/2-65,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[0,0,170,40])  

    elif screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-140 <= mouse[1] <= screen_height/2-70:
        pygame.draw.rect(screen,color_light,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-65,100,40]) 
        pygame.draw.rect(screen,color_dark,[0,0,170,40]) 
            
    elif 0 <= mouse[0] <= 120 and 0 <= mouse[1] <= 50: 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-65,100,40]) 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_light,[0,0,170,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-65,100,40]) 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[0,0,170,40]) 

    screen.blit(text1 , (screen_width/2-30,screen_height/2-105)) 
    screen.blit(text2, (screen_width/2-30,screen_height/2-60))
    screen.blit(text3 , (screen_width/2-25,screen_height/2-15)) 
    screen.blit(back , (5,5))

    pygame.display.update()

def scores_screen():
    """Shows top 10 scores on the screen, draws back to menu button,
    draws back to menu button and make it lighter when mouse points on it. """
    back = smallfont.render('back to menu' , True , black)

    screen.blit(top10_image,(0,0))
    

    mouse = pygame.mouse.get_pos()

    if 0 <= mouse[0] <= 170 and 0 <= mouse[1] <= 40:
        pygame.draw.rect(screen,color_light,[0,0,170,40])
    else:
        pygame.draw.rect(screen,color_dark,[0,0,170,40])

    screen.blit(back , (5,5))

    top10_list = []

    with open('scores.txt') as f:
        scores = eval(f.readlines()[0])
        scores.sort(reverse=True)
        top10_list = scores[0:10]
    
    sc1 = bigfont.render(f' #1   {top10_list[0]}' , True , black)
    sc2 = bigfont.render(f' #2   {top10_list[1]}' , True , black)
    sc3 = bigfont.render(f' #3   {top10_list[2]}' , True , black)
    sc4 = bigfont.render(f' #4   {top10_list[3]}' , True , black)
    sc5 = bigfont.render(f' #5   {top10_list[4]}' , True , black)
    sc6 = bigfont.render(f' #6   {top10_list[5]}' , True , black)
    sc7 = bigfont.render(f' #7   {top10_list[6]}' , True , black)
    sc8 = bigfont.render(f' #8   {top10_list[7]}' , True , black)
    sc9 = bigfont.render(f' #9   {top10_list[8]}' , True , black)
    sc10 = bigfont.render(f'#10   {top10_list[9]}' , True , black)

    screen.blit(sc1 , (screen_width/2-20,50))
    screen.blit(sc2 , (screen_width/2-20,90))
    screen.blit(sc3 , (screen_width/2-20,130))
    screen.blit(sc4 , (screen_width/2-20,170))
    screen.blit(sc5 , (screen_width/2-20,210))
    screen.blit(sc6 , (screen_width/2-20,250))
    screen.blit(sc7 , (screen_width/2-20,290))
    screen.blit(sc8 , (screen_width/2-20,330))
    screen.blit(sc9 , (screen_width/2-20,370))
    screen.blit(sc10 , (screen_width/2-20,410))

    pygame.display.update()

def rules_screen(rules_image):
    """Shows the screen with the rules of chosen level of difficulty.
    
@param rules_image:(str) file with rules"""
    screen.blit(rules_image, (0,0))
    start_text = smallfont.render('start' , True , black)
    mouse = pygame.mouse.get_pos()

    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and 320 <= mouse[1] <= 360: 
        pygame.draw.rect(screen,color_light,[screen_width/2-50,320,100,40])
    else:
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,320,100,40])

    screen.blit(start_text , (screen_width/2-30,325))

    pygame.display.update()

def easy_mode():
    """Draws the game and guides the course of the game after choosing easy level of difficulty. 

@return:(bool, int) Flase when the game is over and player's score"""
    apple_x = round(random.randrange(0, screen_width - snake_part) / 10) * 10
    apple_y = round(random.randrange(30, screen_height - snake_part) / 10) * 10
    x = screen_width / 2
    y = screen_height / 2
    delta_x = 0
    delta_y = 0
    whole_snake = []
    snake_length = 1
    score = 0
    easy = True

    while easy:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -snake_part
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = snake_part
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -snake_part
                elif event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = snake_part

        screen.fill(brown)    
        pygame.draw.rect(screen, red, [apple_x, apple_y, snake_part, snake_part]) 
        x += delta_x
        y += delta_y   

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            easy = False
            game_over_sound.play()

        snake_new_element = []
        snake_new_element.append(x)
        snake_new_element.append(y)
        whole_snake.append(snake_new_element)

        if len(whole_snake) > snake_length:
            del whole_snake[0]     

        for i in whole_snake[:-1]:
            if i == snake_new_element:
               easy = False
               game_over_sound.play()
    
        if x == apple_x and y == apple_y: 
            apple_x = round(random.randrange(0, screen_width - snake_part) / 10) * 10
            apple_y = round(random.randrange(0, screen_height - snake_part) / 10) * 10
            snake_length += 1
            score += 1
            eat_sound.play()
                        
        snake(snake_part, whole_snake)
        show_score(score)
        clock.tick(snake_velocity)
        pygame.display.update()

    return False, score

def hard_mode():
    """Draws the game and guides the course of the game after choosing hard level of difficulty. 

@return:(bool, int) Flase when the game is over and player's score"""
    apple_x = round(random.randrange(0, screen_width - snake_part) / 10) * 10
    apple_y = round(random.randrange(30, screen_height - snake_part) / 10) * 10
    x = screen_width / 2
    y = screen_height / 2
    delta_x = 0
    delta_y = 0
    whole_snake = []
    snake_length = 1
    score = 0
    hard = True
    life = 3
    poison_loctions = []

    for i in range(0,20):
        poison_loctions.append((round(random.randrange(0, screen_width - snake_part) / 10) * 10, round(random.randrange(30, screen_height - snake_part) / 10) * 10))
    
    while hard:    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -snake_part
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = snake_part
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_x = 0
                    delta_y = -snake_part
                elif event.key == pygame.K_DOWN:
                    delta_x = 0
                    delta_y = snake_part

        x += delta_x
        y += delta_y

        screen.fill(brown)
        pygame.draw.rect(screen, red, [apple_x, apple_y, snake_part, snake_part])

        for i in poison_loctions:
            pygame.draw.rect(screen, black, [i[0], i[1], snake_part, snake_part])

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            hard = False
            game_over_sound.play()
                
        snake_new_element = []
        snake_new_element.append(x)
        snake_new_element.append(y)
        whole_snake.append(snake_new_element)

        if len(whole_snake) > snake_length:
            del whole_snake[0]
                
        for i in whole_snake[:-1]:
            if i == snake_new_element:
                hard = False
                game_over_sound.play()

        if x == apple_x and y == apple_y: 
            apple_x = round(random.randrange(0, screen_width - snake_part) / 10) * 10
            apple_y = round(random.randrange(0, screen_height - snake_part) / 10) * 10
            snake_length += 1
            score += 1
            eat_sound.play()

        if (x, y) in poison_loctions:
            life -= 1
            lost_life_sound.play()
                
        if life == 0:
            hard = False
            game_over_sound.play()
                
        if (apple_x, apple_y) in poison_loctions:
            apple_x = round(random.randrange(0, screen_width - snake_part) / 10) * 10
            apple_y = round(random.randrange(0, screen_height - snake_part) / 10) * 10

        snake(snake_part, whole_snake)
        show_score(score)
        show_life(life)
        pygame.display.update()

        clock.tick(snake_velocity)
    return False, score

def game_run():
    """Function responsible for running the game."""
    running = True
    start = True
    close = False
    author = False
    easy = False
    difficulty = False
    hard = False
    best_scores = False
    easy_rules = False
    hard_rules = False

    while running:

        while start == True:

            start_screen()
            
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-20 <= mouse[1] <= screen_height/2+20: 
                        start = False
                        running = False 
                    if screen_width/2-90 <= mouse[0] <= screen_width/2+90 and screen_height/2-65 <= mouse[1] <= screen_height/2-25:
                        start = False
                        author = True
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-110 <= mouse[1] <= screen_height/2-70:
                        start = False
                        difficulty = True
                    if screen_width/2-80 <= mouse[0] <= screen_width/2+80 and screen_height/2+25 <= mouse[1] <= screen_height/2+65:
                        start = False
                        best_scores = True

        while best_scores == True:

            scores_screen()

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if 0 <= mouse[0] <= 170 and 0 <= mouse[1] <= 40: 
                        best_scores = False
                        start = True

        while author == True:

            author_screen()
            
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        author = False
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if 0 <= mouse[0] <= 170 and 0 <= mouse[1] <= 40: 
                        author = False
                        start = True

        while close == True:

            game_over_screen()
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if 0 <= mouse[0] <= 120 and 0 <= mouse[1] <= 50: 
                        close = False
                        start = True
                    if 25 <= mouse[0] <= 205 and screen_height-60 <= mouse[1] <= screen_height-20:
                        close = False
                        difficulty = True
                    if screen_width-125 <= mouse[0] <= screen_width-25 and screen_height-60 <= mouse[1] <= screen_height-20:
                        close = False
                        running = False
            
        while difficulty == True:

            difficulty_screen()

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-20 <= mouse[1] <= screen_height/2+20: 
                        difficulty = False
                        duo = True
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-65 <= mouse[1] <= screen_height/2-25:
                        difficulty = False
                        hard_rules = True
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-110 <= mouse[1] <= screen_height/2-70:
                        difficulty = False
                        easy_rules = True
                    if 0 <= mouse[0] <= 170 and 0 <= mouse[1] <= 40: 
                        difficulty = False
                        start = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        difficulty = False

        while easy_rules == True:

            rules_screen(easy_rules_image)

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and 320 <= mouse[1] <= 360:
                        easy_rules = False
                        easy = True

        while hard_rules == True:

            rules_screen(hard_rules_image)

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and 320 <= mouse[1] <= 360:
                        hard_rules = False
                        hard = True

        score = 0
        all_scores = []

        while easy == True: 

            game = easy_mode()
            score = game[1]

            with open('scores.txt') as f:
                old_scores = f.readlines()
                score_list = eval(old_scores[0])
                score_list.append(score)
                all_scores = score_list
                
            with open('scores.txt', 'w') as f:
                f.write(str(all_scores))

            easy = game[0]
            close = True

        while hard == True:

            game = hard_mode()
            score = game[1]

            with open('scores.txt') as f:
                old_scores = f.readlines()
                score_list = eval(old_scores[0])
                score_list.append(score)
                all_scores = score_list
                
            with open('scores.txt', 'w') as f:
                f.write(str(all_scores))
                
            hard = game[0]
            close = True

    pygame.quit()
    quit()

game_run()
