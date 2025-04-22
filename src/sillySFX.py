#My final Project
import pygame
import sys


def main():
    
    pygame.init()
    pygame.display.set_caption('Silly SFX')
    txtFont= pygame.font.SysFont('cambria',18)
    resolution =((500,500))
    bg_color = pygame.Color(54,24,56)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)

    #color Pallette for buttons
    #-------------------------------------------------------------------
    pal_red=(227,68,86)
    pal_orange=(236,136,90)
    pal_lightyellow =(218,241,123)
    pal_green=(122,213,104)
    pal_blue=(55,164,232)
    pal_magenta=(176,62,154)
    pal_purple=(122,49,151)
    pal_violet=(76,57,123)
    pal_lightblue =(59,207,236)
    pal_lightgreen=(62,153,97)
    #-------------------------------------------------------------------
    
    #Button Object
    class Button:
        def __init__(self,text,x_pos,y_pos,color,enabled):
            self.text =text
            self.x_pos =x_pos
            self.y_pos =y_pos
            #self.rect = self.get_rect(center=(self.x_pos,self.y_pos))
            self.color = color
            self.enabled = enabled
            self.draw()

        def draw(self):
            if self.check_click():
                button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(95,95))
                button_txt = txtFont.render(self.text, True,'dark gray')
            else:
                button_txt = txtFont.render(self.text, True, 'black')
                button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(100,100))
            
            
            pygame.draw.rect(screen ,self.color, button_rect, 0,5)
            screen.blit(button_txt, (self.x_pos +3, self.y_pos +20))

        def check_click(self):
            mouse_pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]
            button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(100,100))
            if click and button_rect.collidepoint(mouse_pos) and self.enabled:
                return True
            else:
                return False

    #-------------------------------------------------------------------
    #This is where you choose the sound effect files to place per button(mp3,wav,aiff)
    channel = pygame.mixer.Channel(0)
    sfx1 = pygame.mixer.Sound('Flapjack_Scream.mp3')
    sfx2 = pygame.mixer.Sound('Vine_Boom.mp3')
    #-------------------------------------------------------------------

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(bg_color)
        button01 = Button('Scream', 80,110,pal_red,True)
        button02 = Button('Thud', 200,110,pal_orange,True)
        button03 = Button('sfx3',320,110,pal_lightyellow,True)

        button04 = Button('sfx4',80,230,pal_lightgreen,True)
        button05 = Button('sfx5',200,230,pal_green,True)
        button06 = Button('sfx6',320,230,pal_lightblue,True)
        
        button07 = Button('sfx7',80,350,pal_blue,True)
        button08 = Button('sfx8',200,350,pal_magenta,True)
        button09 = Button('sfx9',320,350,pal_purple,True)
        #Code for the sounds to play
        #---------------------------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button01.check_click():
                channel.play(sfx1)
            if button02.check_click():
                channel.play(sfx2)
        #---------------------------------------------
       
        #Code for the Keyboard Shortcuts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            channel.play(sfx1)
        if keys[pygame.K_2]:
            channel.play(sfx2)

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()