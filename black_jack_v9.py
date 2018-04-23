class recCardInHand():
    card_num = 0
    x = 0
    y = 0
    visible = False

class recCards():
    image_file = ""
    value = 0

class buttonImage():
    image_file = ""
    x = 0
    y = 0
    visible = False



###############---------------START FUNCTION DEFINITIONS---------------###############
###############---------------START FUNCTION DEFINITIONS---------------###############
###############---------------START FUNCTION DEFINITIONS---------------###############
def get_user_input():
    local_user_in = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            local_user_in = -999
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            local_user_in = -999
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_coords = pygame.mouse.get_pos()
            local_user_in = -1
            if mouse_coords[0] > hit_image.x:
                if mouse_coords[0] < hit_image.x + hit_image.image_file.get_width():
                    if mouse_coords[1] > hit_image.y:
                        if mouse_coords[1] < hit_image.y + hit_image.image_file.get_height():
                            local_user_in = 1
            if mouse_coords[0] > stand_image.x:
                if mouse_coords[0] < stand_image.x + stand_image.image_file.get_width():
                    if mouse_coords[1] > stand_image.y:
                        if mouse_coords[1] < stand_image.y + stand_image.image_file.get_height():
                            local_user_in = 2
            if mouse_coords[0] > play_game_image.x:
                if mouse_coords[0] < play_game_image.x + play_game_image.image_file.get_width():
                    if mouse_coords[1] > play_game_image.y:
                        if mouse_coords[1] < play_game_image.y + play_game_image.image_file.get_height():
                            local_user_in = 3
    return local_user_in


def make_deck():
    #Start the outer loop - we need to loop through the initialisation for each suit
    suit = ['club', 'diamond', 'heart', 'spade']
    #Each iteration through we'll create a temporary record then assign values to it
    #for the next record in the array.
    for s in suit:
        #Create a temporary record 
#        temp_card = recCards()
 #       temp_card.image_file = pygame.image.load('cards/cardback.gif')
  #      temp_card.value = None
   #     cards.append(temp_card)

        temp_card = recCards()
        temp_card.image_file = pygame.image.load('cards/' + s + 'ace.gif')
        temp_card.value = 11
        cards.append(temp_card)
        i = 2
        while i < 11:
            temp_card = recCards()
            temp_card.image_file = pygame.image.load('cards/' + s + str(i) + '.gif')
            temp_card.value = i
            cards.append(temp_card)
            i = i + 1

        #Create the jack, queen and king
        temp_card = recCards()
        temp_card.image_file = pygame.image.load('cards/' + s + 'jack.gif')
        temp_card.value = 10
        cards.append(temp_card)

        temp_card = recCards()
        temp_card.image_file = pygame.image.load('cards/' + s + 'queen.gif')
        temp_card.value = 10
        cards.append(temp_card)

        temp_card = recCards()
        temp_card.image_file = pygame.image.load('cards/' + s + 'king.gif')
        temp_card.value = 10
        cards.append(temp_card)
    
def initialise_buttons_with_values():
    hit_image.image_file = pygame.image.load("hit.jpg")
    hit_image.x = 140
    hit_image.y = 400
    stand_image.image_file = pygame.image.load("stand.jpg")
    stand_image.x = 410
    stand_image.y = 400
    play_game_image.image_file = pygame.image.load("play_game.jpg")
    play_game_image.x = 680
    play_game_image.y = 400


def blit_the_screen():
    screen.fill((0, 100, 0))  
    #make string for player's and dealer's score
    player_has_string = "Player has: " + str(player_score)
    dealer_has_string = "Dealer has: " + str(dealer_score)
    #set the fonts
    big_font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    #create the labels
    label_screen_title = big_font.render("MR THILL'S BLACK JACK PROGRAM",1,(255,0,0))
    label_players_hand = big_font.render("Player's Hand", 1, (255,0,0))
    label_dealers_hand = big_font.render("Dealer's Hand",1, (255,0,0))  
    label_player_has = small_font.render(player_has_string,1,(255,255,255))
    label_dealer_has = small_font.render(dealer_has_string,1,(255,255,255))
    #blit the text and images
    screen.blit(label_screen_title, ((screen_width/2 - label_screen_title.get_width()/2), 10))
    screen.blit(label_players_hand, (200, 130))
    screen.blit(label_dealers_hand, (700, 130))
    screen.blit(label_dealer_has, (650, 300))
    screen.blit(label_player_has,(150,300))
    if hit_image.visible == True:
        screen.blit(hit_image.image_file, (hit_image.x, hit_image.y))
    if stand_image.visible == True:
        screen.blit(stand_image.image_file, (stand_image.x, stand_image.y))

    #blit the player's and dealer's hands
    i = 0
    while i < 5:
        if player_hand[i].visible == True:
            screen.blit(cards[player_hand[i].card_num].image_file,(player_hand[i].x,player_hand[i].y))
        else:
            screen.blit(card_back.image_file, (player_hand[i].x,player_hand[i].y))
        if dealer_hand[i].visible == True:
            screen.blit(cards[dealer_hand[i].card_num].image_file, (dealer_hand[i].x, dealer_hand[i].y))
        else:
            screen.blit(card_back.image_file,(dealer_hand[i].x,dealer_hand[i].y))    
        i = i + 1


def blit_the_pre_game_screen():
    screen.fill((0, 100, 0))  
    #set the fonts
    big_font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    #create the labels
    label_screen_title = big_font.render("MR THILL'S BLACK JACK PROGRAM",1,(255,0,0))
    label_players_hand = big_font.render("Player's Hand", 1, (255,0,0))
    label_dealers_hand = big_font.render("Dealer's Hand",1, (255,0,0))  
    #blit the text and images
    screen.blit(label_screen_title, ((screen_width/2 - label_screen_title.get_width()/2), 10))
    screen.blit(label_players_hand, (200, 130))
    screen.blit(label_dealers_hand, (700, 130))
    screen.blit(play_game_image.image_file, (play_game_image.x, play_game_image.y))
    #blit the player's and dealer's hands
    i = 0
    while i < 5:
        screen.blit(card_back.image_file, (player_hand[i].x,player_hand[i].y))
        screen.blit(card_back.image_file,(dealer_hand[i].x,dealer_hand[i].y))    
        i = i + 1

def set_card_positions_on_table():
    i = 0
    while i < 5:
        temp_card_pos = recCardInHand()
        temp_card_pos.x = (i * 75) + 100
        temp_card_pos.y = 200
        player_hand.append(temp_card_pos)
        temp_card_pos = recCardInHand()
        temp_card_pos.x = (i * 75) + 600
        temp_card_pos.y = 200
        dealer_hand.append(temp_card_pos)
        i = i + 1

def deal_cards():
    deck_pointer = 1
    temp_count = 0        
    while deck_pointer < 10:
        player_hand[temp_count].card_num = deck_pointer
        deck_pointer = deck_pointer + 1
        dealer_hand[temp_count].card_num = deck_pointer
        deck_pointer = deck_pointer + 1
        temp_count = temp_count + 1


###############---------------FINISH FUNCTION DEFINITIONS---------------###############
###############---------------FINISH FUNCTION DEFINITIONS---------------###############
###############---------------FINISH FUNCTION DEFINITIONS---------------###############




#import libraries and intialise them

#Set the off-set for the screen on the computer's monitor. 
#MUST be run before initialising pygame
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "100,50"

import pygame
import ctypes
import random
pygame.init()

#INITIALISE DATA STRUCTURES

#Make the cardback
card_back = recCards()
card_back.image_file = pygame.image.load('cards/cardback.gif')

#initialise screen size variables and create screen object
screen_width = 1100
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
#initialise array of records to hold deck of cards
cards = []
make_deck()
#make the hit, stand, play_again buttons
hit_image = buttonImage()
stand_image = buttonImage()
play_game_image = buttonImage()
initialise_buttons_with_values()

clock = pygame.time.Clock()
running = True
while running == True:
    clock.tick(50)
    game_over = True
    player_sitting = False

    #initialise player and dealer lists and set coords of cards on table
    player_hand = []
    dealer_hand = []
    set_card_positions_on_table()

    num_player_cards = 2
    num_dealer_cards = 1
    blit_the_pre_game_screen()
    user_in = get_user_input()    
  
    pygame.display.flip()
    if user_in:
        if user_in == 3: #if user choses to start game
            game_over = False
            
            i = 0
            while i < len(cards):
                tempRecord = recCards()
                rand_num = random.randrange(0,51)
                tempRecord = cards[i]
                cards[i] = cards[rand_num]
                cards[rand_num] = tempRecord
                i = i + 1
  
            #deal the cards
            deal_cards()
            #uncover the first cards & make hit and stand buttons visible  
            player_hand[0].visible = True
            player_hand[1].visible = True
            dealer_hand[0].visible = True
            hit_image.visible = True
            stand_image.visible = True
        elif user_in == -999:
            running = False

    dealer_score = 0
    player_score = 0
    #game loop starts here
    while game_over == False and running == True:
        clock.tick(50)


       #run the dealer's turn
        if player_sitting == True:
            if dealer_score < 17:
                ctypes.windll.user32.MessageBoxW(0,"Dealer takes another card...", "Dealer's Turn",0)
                dealer_hand[num_dealer_cards].visible = True
                num_dealer_cards = num_dealer_cards + 1


        #get user input
        user_in = get_user_input()
        if user_in:
            if user_in == -999: #if user chooses to exit
                running = False
            elif user_in == 3: #if user chooses to play game
                game_over = True
            elif player_sitting == False:
                if user_in == 1: #if user chooses to hit
                    if num_player_cards < 5:
                        num_player_cards = num_player_cards + 1
                        player_hand[num_player_cards - 1].visible = True        
                elif user_in == 2: #if user chooses to stand
                    player_sitting = True
                    hit_image.visible = False
                    stand_image.visible = False
          
              
        if player_score > 21: #player busts
            ctypes.windll.user32.MessageBoxW(0,"Busted...", "Sorry - Game Over",0)
            game_over = True
        
        if dealer_score > 21: #dealer busts
            ctypes.windll.user32.MessageBoxW(0, "You Win!", "Dealer BUSTS",0)
            game_over = True

        if dealer_score > 16: #when dealer gets to 16
            if dealer_score < 22:
                if dealer_score > player_score:
                    ctypes.windll.user32.MessageBoxW(0,"Dealer wins", "Game Over",0)
                    game_over = True
                elif player_score > dealer_score:
                    ctypes.windll.user32.MessageBoxW(0, "You WIN!", "Game Over", 0)
                    game_over = True
                else:
                    ctypes.windll.user32.MessageBoxW(0, "It's a STAND OFF", "Game Over", 0)
                    game_over = True    

       #determine player's score 
        i = 0
        player_score = 0
        while i < num_player_cards:
            player_score = player_score + cards[player_hand[i].card_num].value
            i = i + 1

        #determine dealer's score
        i = 0
        dealer_score = 0
        while i < num_dealer_cards:
            dealer_score = dealer_score + cards[dealer_hand[i].card_num].value
            i = i + 1
    
        blit_the_screen()
        pygame.display.flip()


  
    

pygame.display.quit()

