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

def snake(snake_part, whole_snake):
    """Draws snake.
@param snake_part:(inf) size of one snake's part

@param whole_snake:(list) list of all snake's parts"""
    for i in whole_snake:
        pygame.draw.rect(screen, green, [i[0], i[1], snake_part, snake_part])

def text(text, color):
    """Shows message on the screen.
@param text:(str) Text to show

@param color:(tuple) color of text in html"""
    message = font_style.render(text, True, color)
    screen.blit(message, [screen_width / 6, screen_height / 3])

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

    mouse = pygame.mouse.get_pos()
    
    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-20 <= mouse[1] <= screen_height/2+20: 
        pygame.draw.rect(screen,color_light,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-90,screen_height/2-65,180,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40]) 

    elif screen_width/2-90 <= mouse[0] <= screen_width+90 and screen_height/2-65 <= mouse[1] <= screen_height/2-25:
        pygame.draw.rect(screen,color_light,[screen_width/2-90,screen_height/2-65,180,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40]) 

    elif screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-140 <= mouse[1] <= screen_height/2-70:
        pygame.draw.rect(screen,color_light,[screen_width/2-50,screen_height/2-110,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-90,screen_height/2-65,180,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-20,100,40])
        pygame.draw.rect(screen,color_dark,[screen_width/2-90,screen_height/2-65,180,40]) 
        pygame.draw.rect(screen,color_dark,[screen_width/2-50,screen_height/2-110,100,40]) 
      
    screen.blit(text1 , (screen_width/2-25,screen_height/2-15)) 
    screen.blit(text2, (screen_width/2-75,screen_height/2-60))
    screen.blit(text3 , (screen_width/2-30,screen_height/2-105)) 

    pygame.display.update()

def author_screen():
    """Shows photo of the author and a note from the author about the game,
    draws back to menu button and make it lighter when mouse points on it."""
    screen.fill(white)
    screen.blit(image, (screen_width/2-60, 40))
    screen.blit(author_text, (110, 170))
    text3= smallfont.render('back to menu' , True , black)
    mouse = pygame.mouse.get_pos()
            
    if 0 <= mouse[0] <= 120 and 0 <= mouse[1] <= 50: 
        pygame.draw.rect(screen,color_light,[0,0,170,40])
    else:
        pygame.draw.rect(screen,color_dark,[0,0,170,40])
    screen.blit(text3 , (5,5))

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

        snake_new_element = []
        snake_new_element.append(x)
        snake_new_element.append(y)
        whole_snake.append(snake_new_element)

        if len(whole_snake) > snake_length:
            del whole_snake[0]     

        for i in whole_snake[:-1]:
            if i == snake_new_element:
               easy = False
    
        if x == apple_x and y == apple_y: 
            apple_x = round(random.randrange(0, screen_width - snake_part) / 10) * 10
            apple_y = round(random.randrange(0, screen_height - snake_part) / 10) * 10
            snake_length += 1
            score += 1
                        
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
                
        snake_new_element = []
        snake_new_element.append(x)
        snake_new_element.append(y)
        whole_snake.append(snake_new_element)

        if len(whole_snake) > snake_length:
            del whole_snake[0]
                
        for i in whole_snake[:-1]:
            if i == snake_new_element:
                hard = False

        if x == apple_x and y == apple_y: 
            apple_x = round(random.randrange(0, screen_width - snake_part) / 10) * 10
            apple_y = round(random.randrange(0, screen_height - snake_part) / 10) * 10
            snake_length += 1
            score += 1

        if (x, y) in poison_loctions:
            life -= 1
                
        if life == 0:
            hard = False
                
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

    while running:

        while start == True:

            start_screen()
            
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-20 <= mouse[1] <= screen_height/2+20: 
                        start = False
                        runnig = False 
                        pygame.quit()
                    if screen_width/2-90 <= mouse[0] <= screen_width/2+90 and screen_height/2-65 <= mouse[1] <= screen_height/2-25:
                        start = False
                        author = True
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-110 <= mouse[1] <= screen_height/2-70:
                        start = False
                        difficulty = True

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

            screen.fill(white)
            text("Game over! Press Q to quit or P to play again.", red)
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        close = False
                    if event.key == pygame.K_p:
                        game_run()
            
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
                        hard = True
                    if screen_width/2-50 <= mouse[0] <= screen_width/2+50 and screen_height/2-110 <= mouse[1] <= screen_height/2-70:
                        difficulty = False
                        easy = True
                    if 0 <= mouse[0] <= 170 and 0 <= mouse[1] <= 40: 
                        difficulty = False
                        start = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        difficulty = False

        score = 0

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
